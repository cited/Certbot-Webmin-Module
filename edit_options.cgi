#!/usr/bin/perl

require './certbot-lib.pl';

sub add_certbot_logrotate(){
	open($fh, '>'.$config{'certbot_logrotate'}) or die $!;
	print $fh "/var/log/letsencrypt/*.log {\n";
  print $fh "\trotate 12\n";
  print $fh "\tweekly\n";
  print $fh "\tcompress\n";
  print $fh "\tmissingok\n";
	print $fh "}\n";
  close($fh);
}

sub get_certbot_logrotate(){

	my $lref = &read_file_lines($config{'certbot_logrotate'});
	foreach my $line (@$lref) {
		if($line =~ /\s+rotate\s(\d+)$/){		#the rotate line
			return $1;
		}
	}
	return 0;
}

my %opts = get_certbot_options();
my %opts_ini = ();
read_file_cached('/etc/letsencrypt/cli.ini', \%opts_ini);

&ui_print_header(undef, $text{'options_title'}, "");

if(! -f $config{'certbot_logrotate'}){	#if we have a logrotate file
	add_certbot_logrotate();
}

$opts_ini{'max-log-backups'} = get_certbot_logrotate();
if(&indexof($opts_ini{'max-log-backups'}, $opts{'max-log-backups'}) < 0){	#if value is not in default values
	push(@{%opts{'max-log-backups'}}, $opts_ini{'max-log-backups'});
}


#show options
print &ui_form_start("save_options.cgi", "post");
print $text{'options_desc'}.'<br><br>';

my %gr_opts = get_certbot_group_options();
foreach my $gr_key (sort keys %gr_opts){


	my @tds = ();
	print &ui_columns_start(['Description', 'Options', 'CLI ref.'], undef, 0, \@tds, '<b>'.$gr_key.'</b>');

	foreach my $key (sort @{$gr_opts{$gr_key}}){	#for each option

		my $html_key = $key;
		$html_key =~ tr /-/_/;

		my @cols = ();
		if(	($opts{$key}[0] eq 'true') ||
				($opts{$key}[0] eq 'false')		){	#if option is boolean
			my $cur_val = '';
			if(!$opts_ini{$key}){	#if key is not found in ini file
					$cur_val = $opts{$key}[0];	#set default value
			}else{
				if($opts_ini{$key} eq 'yes'){
					$cur_val = 'true';	#if ini file uses yes, instead of true
					}elsif($opts_ini{$key} eq 'no'){
						$cur_val = 'false';	#if ini file uses yes, instead of true
					}else{
						$cur_val = $opts_ini{$key};
					}
			}
			@cols = ($text{$key}, &ui_yesno_radio($html_key, $cur_val, 'true', 'false'), "<i>(--$key)</i>");

		}elsif(	$opts{$key}[0] eq 'textbox'){
			@cols = ($text{$key}, &ui_textbox($html_key, $opts_ini{$key}, 20), "<i>(--$key)</i>");
		}else{
			my @sel_opts = @{$opts{$key}};
			@cols = ($text{$key}, &ui_select($html_key, $opts_ini{$key}, \@sel_opts, 1, 0), "<i>(--$key)</i>");
		}
			print &ui_columns_row(\@cols, \@tds);
	}
	print &ui_columns_end();
}
print &ui_form_end([ [ "", $text{'options_save'} ] ]);

&ui_print_footer("", $text{'index_return'});
