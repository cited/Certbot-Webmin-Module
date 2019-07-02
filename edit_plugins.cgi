#!/usr/bin/perl

require './certbot-lib.pl';
foreign_require('software', 'software-lib.pl');
foreign_require('webmin', 'webmin-lib.pl');

sub get_plugin_pkgs{
	my $cmd_out='';
	my $cmd_err='';
	my $out = '';
	my $cmd = &has_command('dnf') || &has_command('yum') || &has_command('apt-cache') || undef;

	if($cmd){
		$out = &execute_command($cmd." search certbot-", undef, \$cmd_out, \$cmd_err, 0, 0);
	}

	if($cmd_err ne ""){
		&error("Error: $cmd: $cmd_err");
	}

	my %pkgs;
	my @lines = split /\n/, $cmd_out;
	foreach my $line (@lines){
		#python2-certbot-dns-cloudflare.noarch : Cloudflare DNS Authenticator plugin for Certbot
		if($line =~ /^(python[2-9]?-certbot-[a-z0-9\-_]+)(\.noarch)?\s[:\-]\s([A-Za-z \t_0-9\-]+)\splugin.*/i){
			if(substr($1, -4) ne '-doc'){
				$pkgs{$1} = $3;
			}
		}
	}
	return %pkgs;
}

sub get_packages_installed_yum{
	my $href = $_[0];

	my $pkg_list = "";
	foreach my $pkg (keys %$href){
		$pkg_list .= " $pkg";
	}

	my $cmd_out='';
	my $cmd_err='';
	local $out = &execute_command("rpm -q --queryformat \"%{NAME}\n\" $pkg_list", undef, \$cmd_out, \$cmd_err, 0, 0);

	my %pkgs;
	my @lines = split /\n/, $cmd_out;
	foreach my $line (@lines){
		if($line =~ /^package\s+([a-z0-9_\.-]+)\s/i){	#package pgdg96-centos is not installed
			$pkgs{$1} = 0;
		}else{
			$pkgs{$line} = 1;
		}
	}
	return %pkgs;
};

sub get_packages_installed_apt{
	my $href = $_[0];	#package names

	my $cmd_out='';
	my $cmd_err='';
	local $out = &execute_command("dpkg -l '*-certbot-*'", undef, \$cmd_out, \$cmd_err, 0, 0);

	if($cmd_err ne ""){
		&error("Error: dpkg: $cmd_err");
	}

	my %pkgs;

	#set all packages to not installed, since dpkg won't list them
	foreach my $name (keys %$href){
		$pkgs{$name} = 0;
	}

	my @lines = split /\n/, $cmd_out;
	foreach my $line (@lines){
		if($line =~ /^(..)\s+(python[2-9]-certbot-[a-z0-9\._-]*)/i){
			my $pkg = $2;
			if($1 =~ /[uirph]i/){
				$pkgs{$pkg} = 1;
			}
		}
	}
	return %pkgs;
};

sub update_packages{
	my $pkgs_install = $_[0];
	my $pkgs_remove  = $_[1];	#\@lref

	if($pkgs_install ne ""){
		$pkgs_install =~ s/\s+$//;
		software::update_system_install($pkgs_install, undef);
	}

	if(@$pkgs_remove){
		print "<br><p>Removing packages</p>";
		my %opts = ('depstoo'=>1);
		my $error = "";
		if (defined(&delete_packages)) {
			$error = software::delete_packages($pkgs_remove, \%opts, undef);
		}else{
			foreach my $pkg (@$pkgs_remove){
				$error .= software::delete_package($pkg, \%opts, undef)
			}
		}

		if($error ne ""){
			&error($error);
		}else{
			foreach my $pkg (@$pkgs_remove){
				print "<tt>Deleted $pkg</tt><br>"
			}
		}

	}
}

&ui_print_header(undef, $text{'plugins_title'}, "", "intro", 1, 1);
print $text{'plugins_desc'};
&ReadParse();

my %pkgs = get_plugin_pkgs();
my %pkgs_installed;

my %osinfo = &webmin::detect_operating_system();
if( $osinfo{'os_type'} =~ /redhat/i){	#other redhat

		%pkgs_installed = get_packages_installed_yum(\%pkgs);

}elsif( $osinfo{'os_type'} =~ /debian/i){

		%pkgs_installed = get_packages_installed_apt(\%pkgs);
}

#find what was changed
my @pkgs_remove;
my $pkgs_install="";
foreach my $pkg (sort keys %pkgs_installed){
	if($in{$pkg.'_status'} != $pkgs_installed{$pkg}){
		if($in{$pkg.'_status'} == 1){
			$pkgs_install .= "$pkg ";
		}elsif($in{$pkg.'_status'}){
			push(@pkgs_remove, $pkg);
		}
	}
}

#Check what is updated
if ($pkgs_install or @pkgs_remove) {	#if pkgs were edited
	update_packages($pkgs_install, \@pkgs_remove);
}else{
	print &ui_form_start("edit_plugins.cgi", "post");

	my @tds = ();
	print &ui_columns_start([	'<b>Name</b>','<b>Installed?</b>','<b>Description</b>'], undef, 0, \@tds, $text{'plugins_tbl_title'});
	foreach my $pkg (sort keys %pkgs){
		my @cols;
		my $short_pkg = $pkg;
		$short_pkg =~ s/python[2-9]?-certbot-//;
		push(@cols, $short_pkg);
		push(@cols, ui_yesno_radio($pkg.'_status', $pkgs_installed{$pkg}));
		push(@cols, $pkgs{$pkg});

		print &ui_columns_row(\@cols, \@tds);
	}
	print &ui_columns_end();
	print &ui_form_end([ [ "", $text{'plugins_ok'} ] ]);
}

&ui_print_footer("", $text{'index_return'});
