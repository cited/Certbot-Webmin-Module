#!/usr/bin/perl

require './certbot-lib.pl';

&ReadParse();

&ui_print_header(undef, $text{'certificates_title'}, "");
my $name = $in{'name'};
my $mode = $in{'mode'} || 'control';

my $href = get_cert_info($name);
if(!$href){
	error('Certificate '.$name.' not found!');
	&ui_print_footer("edit_certificates.cgi", $text{'index_return'});
	exit();
}


my @tabs = (	[ "control", $text{'cert_tab_control'}, "view_certificate.cgi?mode=control" ],
		  				[ "details", $text{'cert_tab_details'}, "view_certificate.cgi?mode=details" ]
					);

print &ui_tabs_start(\@tabs, "mode", $mode, 1);

#Control tab
print &ui_tabs_start_tab("mode", "control");
print &ui_table_start($text{'cert_tbl_info'}, "width=100%", 2);
	print &ui_table_row($text{'cert_name'}, $href->{'name'}, 2);

	my $dom_links = '';
	my @cert_doms = split(',',$href->{'domains'});
	for my $dom (@cert_doms){
		$dom_links .= '<a target="_blank" href="https://'.$dom.'/">'.$dom.'</a><br>';
	}
	print &ui_table_row($text{'cert_domains'}, $dom_links, 2);
	print &ui_table_row($text{'cert_file'}, 		$href->{'cert_path'}, 2);
	print &ui_table_row($text{'cert_keyfile'}, 	$href->{'key_path'}, 2);

	my %vconf = find_cert_usedin($href);
	my @cert_vconf = ();
	foreach my $vidx (sort keys %vconf){
		if($vconf{$vidx} =~ m/nginx/){
			push(@cert_vconf, $vconf{$vidx});
		}else{
			push(@cert_vconf, "<a href=/apache/manual_form.cgi?virt=$vidx>".$vconf{$vidx}."</a>");
		}
	}
	print &ui_table_row($text{'cert_usedin'}, join("<br>", @cert_vconf), 2);

print &ui_table_end();
	&ui_buttons_start();
		my @ops = ('revoke', 'renew', 'test');

		if($href->{'revoked'} eq 'yes'){	#you can only delete a revoked cert
			@ops = ('delete');
		}elsif(scalar(@cert_doms) != scalar(@cert_vconf)){
			unshift(@ops, 'install');
		}


		foreach $op (@ops){
			print ui_buttons_row('cert_'.$op.'.cgi?name='.$href->{'name'}, $text{'cert_'.$op}, $text{'cert_'.$op.'_msg'});
		}
	&ui_buttons_end();
print &ui_tabs_end_tab();

#Details tab
print &ui_tabs_start_tab("mode", "details");
	#show cert details from OpenSSL
	print &ui_table_start($text{'cert_header'}.':<tt>'.$href->{'cert_path'}.'</tt>',"width=100%", 1);
		my $out = &backquote_command('openssl x509 -in '.$href->{'cert_path'}.' -text -noout');
		print &ui_textarea('cert_info', $out, 100, 1, 'soft', 1);
	print &ui_table_end();
print &ui_tabs_end_tab();


print &ui_tabs_end_tab();

&ui_print_footer("edit_certificates.cgi", $text{'index_return_certs'});
