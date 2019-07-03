#!/usr/bin/perl

require './certbot-lib.pl';

sub update_certbot_logrotate{
	my $rotate_val = $_[0];

	my $lref = &read_file_lines($config{'certbot_logrotate'});
	my $lnum = 0;

	foreach my $line (@$lref) {
		if($line =~ /rotate /){		#the rotate line

			@{$lref}[$lnum] = "\trotate ". $rotate_val;
			flush_file_lines($config{'certbot_logrotate'});

			last;
		}
		$lnum++;
	}
}

&ReadParse();

my %opts = get_certbot_options();
my %opts_ini = ();
read_file_cached('/etc/letsencrypt/cli.ini', \%opts_ini);

#save options
my $flag_changed = 0;
foreach my $key (keys %opts){	#for each option
	my $html_key = $key;
	$html_key =~ tr /-/_/;

	#save only if its not default option
	if(	($in{$html_key} ne $opts{$key}[0]) 	&&
			($in{$html_key} ne $opts_ini{$key})	){	#if key is not default or is different than ini

		if(	($opts{$key}[0] eq 'textbox')	 ||									#if option is entered by user
				(&indexof($in{$html_key}, @{$opts{$key}}) >= 0)){	#if value is in allowed values

			if(($key eq 'max-log-backups') && -f $config{'certbot_logrotate'}){	#if we have a logrotate file
				update_certbot_logrotate($in{$html_key});												#save --max-log-backups value there
			}else{
				$opts_ini{$key} = $in{$html_key};	#save value
				$flag_changed = 1;
			}
		}
	}
}

if($flag_changed == 1){
	write_file('/etc/letsencrypt/cli.ini', \%opts_ini);
}

&redirect("/certbot/edit_options.cgi");
