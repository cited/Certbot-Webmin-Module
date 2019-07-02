#!/usr/bin/perl

require './certbot-lib.pl';

&ReadParse();

&ui_print_header(undef, $text{'certificates_title'}, "");

my $name = $in{'name'};
my $mode = $in{'mode'} || 'select';

my $href = get_cert_info($name);
if(!$href){
	error('Certificate'.$name.' not found!');

}elsif($href->{'revoked'} eq 'yes'){
		error('Can\'t renew a certificate that is revoked!');

}elsif($mode eq 'select'){	#user selects options
	print $text{'cert_renew_desc'}.'<br>';
	print &ui_form_start("cert_renew.cgi", "post");
	print &ui_hidden('mode', 'renew');
	print &ui_hidden('name', $name);
	print &ui_table_start($text{'cert_tbl_renew'}, "width=100%", 2);
		print &ui_table_row($text{'cert_name'}, $href->{'name'}, 2);
		print &ui_table_row($text{'cert_no_directory_hooks'},	&ui_yesno_radio('renew_hooks', 'false', 'true', 'false'), 2);
		print &ui_table_row($text{'cert_no_renew_updates'},		&ui_yesno_radio('renew_updates', 'false', 'true', 'false'), 2);
		print &ui_table_row($text{'cert_no_hook_validation'},	&ui_yesno_radio('renew_validation', 'false', 'true', 'false'), 2);

	print &ui_table_end();
	print &ui_form_end([ [ "", $text{'cert_renew'} ] ]);

}else{ #real renew
	my $cmd = get_certbot_cmd().' renew -n';
	if($in{'renew_hooks'} eq 'true'){
		$cmd .= ' --no-directory-hooks';
	}
	if($in{'renew_updates'} eq 'true'){
		$cmd .= ' --disable-renew-updates';
	}

	if($in{'renew_validation'} eq 'true'){
		$cmd .= ' --disable-hook-validation';
	}
	$cmd .= ' 2>&1';	#output goes to stderr!

	my $out = &backquote_command($cmd);
	foreach my $line (split('\n', $out)){
		print &html_escape($line)."<br>";
	}
}
&ui_print_footer("edit_certificates.cgi", $text{'index_return_certs'});
