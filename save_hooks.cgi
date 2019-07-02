#!/usr/bin/perl
# Update a manually edited hook file

require './certbot-lib.pl';

&error_setup($text{'manual_err'});

&ReadParseMime();

# Work out the file
if($in{'mode'} && ($in{'mode'} eq 'create')){ #creating a new file
  my @subdirs = ('pre', 'deploy', 'post');
  &indexof($in{'subdir'}, @subdirs) >= 0 || &error($text{'hooks_esubdir'});
  my $inv_name = $in{'hookname'};
  $inv_name =~ s/[A-Za-z0-9_\-\.]//g;
  if ($inv_name) {
    &error($text{'hooks_efilename'});
  }
  #just make an empty file
  my $filename = get_hooks_dir().'/'.$in{'subdir'}.'/'.$in{'hookname'};
  open(DATA, ">$filename") or die $!;
  close(DATA);

}else{  #an existing file
  my @files = get_certboot_hooks();
  &indexof($in{'file'}, @files) >= 0 || &error($text{'manual_efile'});

  $in{'data'} =~ s/\r//g;
  $in{'data'} =~ /\S/ || &error($text{'manual_edata'});

  # Write to it
  my $filename = get_hooks_dir().'/'.$in{'subdir'}.'/'.$in{'file'};
  open(DATA, ">$filename") or die $!;
  print DATA $in{'data'};
  close(DATA);
}

&redirect("edit_hooks.cgi");
