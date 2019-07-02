#!/usr/bin/perl

require './certbot-lib.pl';

&ui_print_header(undef, $text{'certificates_title'}, "");

print $text{'certificates_desc'}.' <a href="/webmin/edit_ssl.cgi?mode=lets">Let\'s Encrypt form</a><br>';

my @cert_info = get_certbot_certs_info();

my @tds = ();
print &ui_columns_start([	'Name','Domains','Expiry Date', 'Flags'], undef, 0, \@tds, 'Certificates');
foreach $href (@cert_info) {

	my @cols;

	push(@cols, '<a href="view_certificate.cgi?name='.$href->{'name'}.'">'.$href->{'name'}.'</a>');

	my $dom_links = '';
	for my $dom (split(',',$href->{'domains'})){
		$dom_links .= '<a target="_blank" href="https://'.$dom.'/">'.$dom.'</a><br>';
	}
	push(@cols, $dom_links);
	push(@cols, $href->{'expiry_date'});	#TODO: Put data in red if its expired!, in yellow if it expires this week

	my @flags=();
	if($href->{'staging'} eq 'yes'){
		push(@flags,'TEST');
	}
	if($href->{'revoked'} eq 'yes'){
		push(@flags, 'REVOKED');
	}

	if($href->{'valid_for'}){
		push(@flags, 'VALID for '.$href->{'valid_for'});
	}

	push(@cols, join(',', @flags));

	print &ui_columns_row(\@cols, \@tds);
}
print &ui_columns_end();

&ui_print_footer("", $text{'index_return'});
