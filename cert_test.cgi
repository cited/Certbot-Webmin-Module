#!/usr/bin/perl

require './certbot-lib.pl';

&ReadParse();

&ui_print_header(undef, $text{'certificates_title'}, "");

print $text{'cert_test_desc'}.'<br><br>';

print <<EOF;
<script type="text/javascript">
function testFunc(){
	var certSel  = document.getElementById('test_domain');
	var cert_dom = certSel.options[certSel.selectedIndex].value;
	window.open('https://www.ssllabs.com/ssltest/analyze.html?d='+cert_dom);
}
</script>
EOF

my $name = $in{'name'};

my $href = get_cert_info($name);
if(!$href){
	error('Certificate'.$name.' not found!');
	&ui_print_footer("edit_certificates.cgi", $text{'index_return'});
	exit();
}

print &ui_table_start($text{'cert_tbl_test'}, "width=100%", 2);
	print &ui_table_row($text{'cert_name'}, $href->{'name'}, 2);

	my @cert_domains = split(',', $href->{'domains'});
	print &ui_table_row($text{'cert_domains'}, &ui_select('test_domain', $cert_domains[0], \@cert_domains, 1, 0, undef, undef, 'id="test_domain"'), 2);
print &ui_table_end();
print &ui_button($text{'cert_test'}, 'cert_test_btn', undef, 'onClick="testFunc()"');

&ui_print_footer("edit_certificates.cgi", $text{'index_return_certs'});
