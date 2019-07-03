#!/usr/bin/perl
# Update a manually edited config file

require './certbot-lib.pl';

&error_setup($text{'manual_err'});

&ReadParseMime();

my $certbot_etc = '/etc/letsencrypt';

# Work out the file
my @files = ($certbot_etc.'/cli.ini');
&indexof($in{'file'}, @files) >= 0 || &error($text{'manual_efile'});
$in{'data'} =~ s/\r//g;
$in{'data'} =~ s/ = /=/g; #replace spaces in key = value
$in{'data'} =~ /\S/ || &error($text{'manual_edata'});

# Write to it
&open_lock_tempfile(DATA, ">$in{'file'}");
&print_tempfile(DATA, $in{'data'});
&close_tempfile(DATA);

&webmin_log("manual", undef, $in{'file'});
&redirect("");
