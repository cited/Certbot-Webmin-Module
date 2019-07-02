#!/usr/bin/perl

require './certbot-lib.pl';

&ReadParse();

&ui_print_header(undef, $text{'certificates_title'}, "");

my $name = $in{'name'};

my $href = get_cert_info($name);
if(!$href){
	error('Certificate'.$name.' not found!');

}elsif($href->{'revoked'} eq 'no'){
	error('Can\'t delete a certificate that is not revoked!');

}else{ #delete
	my $cmd = get_certbot_cmd().' delete -n';
	$cmd .= ' --cert-name '.$href->{'name'};
	$cmd .= ' 2>&1';	#output goes to stderr!

	my $out = &backquote_command($cmd);
	foreach my $line (split('\n', $out)){
		print &html_escape($line)."<br>";
	}
}
&ui_print_footer("edit_certificates.cgi", $text{'index_return_certs'});
