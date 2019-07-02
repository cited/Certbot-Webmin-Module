#!/usr/bin/perl

require './certbot-lib.pl';

&ReadParse();

&ui_print_header(undef, $text{'hooks_title'}, "");
print $text{'hooks_desc'};

my @hook_files = get_certboot_hooks();
my $hooks_dir = get_hooks_dir();
my $file = $in{'file'} || @hook_files[0];
my $mode = $in{'mode'} || 'edit';
my @subdirs = ('pre', 'deploy', 'post');

my @tabs = (	[ "edit",   $text{'hooks_tab_edit'},   "edit_hooks.cgi?mode=edit" ],
		  				[ "create", $text{'hooks_tab_create'}, "edit_hooks.cgi?mode=create" ]
					);

print &ui_tabs_start(\@tabs, "mode", $mode, 1);

#edit tab
print &ui_tabs_start_tab("mode", "edit");

print &ui_form_start("edit_hooks.cgi");
print "<b>$text{'hooks_file'}</b>\n";
print &ui_select("file", $file, [ map { [ $_ ] } @hook_files ], 1, 0),"\n";
print &ui_submit($text{'manual_ok'});
print &ui_form_end();

# Show the file contents
print &ui_form_start("save_hooks.cgi", "form-data");
	print &ui_hidden("file", $file),"\n";
	my $data = &read_file_contents($hooks_dir.'/'.$file);
	print &ui_textarea("data", $data, 20, 80);
print &ui_form_end([ [ "save", $text{'save'} ] ]);
print &ui_tabs_end_tab();

#create tab
print &ui_tabs_start_tab("mode", "create");

print &ui_form_start("save_hooks.cgi", "form-data");
	print &ui_hidden("mode", 'create');
	print "<b>$text{'hooks_type'}</b>";
	print &ui_select("subdir", @subdirs[0], [ map { [ $_ ] } @subdirs ], 1, 0);
	print "<b>$text{'hooks_file'}</b>";
	print &ui_textbox('hookname', '', 20);
print &ui_form_end([ [ "create", $text{'hook_create_ok'} ] ]);

print &ui_tabs_end_tab();

&ui_print_footer("", $text{'index_return'});
