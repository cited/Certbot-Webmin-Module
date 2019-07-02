#!/usr/bin/perl

require './certbot-lib.pl';

&ReadParse();

&ui_print_header(undef, $text{'certificates_title'}, "");

my $name = $in{'name'};
my $mode = $in{'mode'} || 'select';

my $href = get_cert_info($name);
if(!$href){
	error('Certificate'.$name.' not found!');

}elsif($mode eq 'select'){	#user selects options

	print &ui_form_start("cert_revoke.cgi", "post");
	print &ui_hidden('mode', 'revoke');
	print &ui_hidden('name', $name);
	print &ui_table_start($text{'cert_tbl_revoke'}, "width=100%", 2);
		print &ui_table_row($text{'cert_name'}, $href->{'name'}, 2);

		my @reasons = (['unspecified', 'Unspecified'], ['keycompromise', 'Key compromise'], ['affiliationchanged', 'Affiliation Changed'], ['superseded', 'Suspended'], ['cessationofoperation', 'Cessation of operation']);
		print &ui_table_row($text{'revoke_reasons'}, 		&ui_select('revoke_reason', $reasons[0][0], \@reasons, 1, 0), 2);
		print &ui_table_row($text{'revoke_and_delete'}, &ui_yesno_radio('revoke_and_delete', 'true', 'true', 'false'), 2);

	print &ui_table_end();
	print &ui_form_end([ [ "", $text{'cert_revoke'} ] ]);

}else{ #real revoke
	my $cmd = get_certbot_cmd().' revoke -n';
	$cmd .= ($in{'revoke_and_delete'} eq 'true') ? ' --delete-after-revoke' : ' --no-delete-after-revoke';
	$cmd .= ' --cert-path '.$href->{'cert_path'};
	$cmd .= ' 2>&1';	#output goes to stderr!

	my $out = &backquote_command($cmd);
	foreach my $line (split('\n', $out)){
		print &html_escape($line)."<br>";
	}
}
&ui_print_footer("edit_certificates.cgi", $text{'index_return_certs'});
