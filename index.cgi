#!/usr/bin/perl

require './certbot-lib.pl';
require '../webmin/webmin-lib.pl';	#for OS detection

# Check if config file exists
if (! -r $config{'certbot_config'}) {
	&ui_print_header(undef, $text{'index_title'}, "", "intro", 1, 1);
	print &text('index_econfig', "<tt>$config{'certbot_config'}</tt>",
		    "$gconfig{'webprefix'}/config.cgi?$module_name"),"<p>\n";
	&ui_print_footer("/", $text{"index"});
	exit;
}

if(-f "$module_root_directory/setup.cgi"){
	&redirect("setup.cgi?mode=checks");
	exit;
}

my %version = get_certbot_version();

&ui_print_header("AcuGIS ES<sup>&copy</sup> by <a href='https://www.acugis.com' target='blank'>AcuGIS</a>.  Cited, Inc. 2017 ", $text{'index_title'}, "", "intro", 1, 1, 0,
	&help_search_link("certbot", "lets encrypt", "man", "ssl", "google"), undef, undef,
	"$version{'type'} $version{'number'}");

push(@links, "edit_manual.cgi");
push(@titles, $text{'manual_title'});
push(@icons, "images/edit.png");

push(@links, "edit_options.cgi");
push(@titles, $text{'options_title'});
push(@icons, "images/console.png");

push(@links, "edit_certificates.cgi");
push(@titles, $text{'certificates_title'});
push(@icons, "images/certificates.png");

if(-d get_certbot_logdir() ){	#show log tab only if dir exists
	push(@links, "/syslog/save_log.cgi?oidx=0&omod=certbot&view=1");
	push(@titles, $text{'logs_title'});
	push(@icons, "images/logs.png");
}

push(@links, "edit_hooks.cgi");
push(@titles, $text{'hooks_title'});
push(@icons, "images/hooks.png");

push(@links, "edit_plugins.cgi");
push(@titles, $text{'plugins_title'});
push(@icons, "images/plugins.png");

&icons_table(\@links, \@titles, \@icons, 4);

#do some automation option checks
my %opts_ini = ();
read_file_cached('/etc/letsencrypt/cli.ini', \%opts_ini);

if(!$opts_ini{'agree-tos'} || $opts_ini{'agree-tos'} eq 'false'){
	print 'Option <b>--agree-tos</b> must be enabled. Use <a href="edit_options.cgi">CLI Options</a> to fix this.<br>';
}
if(!$opts_ini{'email'}){
	print 'Option <b>--email</b> must be enabled. Use <a href="edit_options.cgi">CLI Options</a> to fix this.<br>';
}
if((!$opts_ini{'no-eff-email'} && !$opts_ini{'eff-email'}) ||	#one of the options has to appear in cli.ini
	  $opts_ini{'no-eff-email'} eq $opts_ini{'eff-email'} ){	#they can't be equal
	print 'Option <b>--no-eff-email</b> must be set. Use <a href="edit_options.cgi">CLI Options</a> to fix this.<br>';
}

&ui_print_footer("/", $text{"index_return"});
