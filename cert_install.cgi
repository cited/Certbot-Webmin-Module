#!/usr/bin/perl

require './certbot-lib.pl';

&ReadParse();

&ui_print_header(undef, $text{'certificates_title'}, "");

my $name = $in{'name'};
my $mode = $in{'mode'} || 'select';

my $href = get_cert_info($name);
if(!$href){
	error('Certificate'.$name.' not found!');

}elsif($mode eq 'select'){	#user selects domains

	print $text{'cert_install_desc'}.'<br><br>';

	#TODO: only do this, if we have multiple domains ?
	print &ui_form_start("cert_install.cgi", "post");
	print &ui_hidden('mode', 'install');
	print &ui_hidden('name', $name);
	print &ui_table_start($text{'cert_tbl_install'}, "width=100%", 2);
		print &ui_table_row($text{'cert_name'}, $href->{'name'}, 2);

		#TODO: exclude domains already enabled!
		my @cert_domains = split(',', $href->{'domains'});
		print &ui_table_row($text{'cert_domains'}, &ui_select('test_domain', $cert_domains[0], \@cert_domains, 4, 1, undef, undef, 'id="test_domain"'), 2);
		print &ui_table_row($text{'www_redirect'}, &ui_yesno_radio('www_redirect', 'false', 'true', 'false'), 2);

	print &ui_table_end();
	print &ui_form_end([ [ "", $text{'cert_install'} ] ]);

}else{ #real install
	my $cmd = 'certbot install --cert-name '.$href->{'name'};
	$cmd .= ($in{'www_redirect'} eq 'true') ? ' --redirect' : ' --no-redirect';
	$cmd .= ' 2>&1';	#output goes to stderr!

	my $out = &backquote_command($cmd);
	foreach my $line (split('\n', $out)){
		print &html_escape($line)."<br>";
	}
}
&ui_print_footer("edit_certificates.cgi", $text{'index_return_certs'});
