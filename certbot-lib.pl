#!/usr/bin/perl

BEGIN { push(@INC, ".."); };

use WebminCore;
use File::Basename;

my %wconfig = foreign_config('webmin');

init_config();

sub get_certbot_config
{
my $lref = &read_file_lines($config{'certbot_config'});
my @rv;
my $lnum = 0;
foreach my $line (@$lref) {
    my ($n, $v) = split(/\s+/, $line, 2);
    if ($n) {
      push(@rv, { 'name' => $n, 'value' => $v, 'line' => $lnum });
      }
    $lnum++;
    }
return @rv;
}

sub get_certbot_version{
  local %version;
	local $out = &backquote_command(get_certbot_cmd()." --version 2>&1");

	if ($out =~ /(certbot)\s([0-9\.]+)/i) {
		$version{'type'} = $1;
		$version{'number'} = $2;
	}else {
		$version{'type'} = 'unknown';
		$version{'number'} = 0.0;
	}

	return %version;
}

sub get_certbot_cmd(){
  my $letsencrypt_cmd = 'not-found';
  if ($wconfig{'letsencrypt_cmd'}) {
    $letsencrypt_cmd = &has_command($wconfig{'letsencrypt_cmd'});
  }else {
    $letsencrypt_cmd = &has_command("letsencrypt")      ||
                       &has_command("letsencrypt-auto") ||
                       &has_command("certbot")          ||
                       &has_command("certbot-auto")     ||
                       'not-installed';
  }
  return $letsencrypt_cmd;
}

sub get_certbot_group_options(){
  my %groups = ('Optional'     => ['max-log-backups', 'dry-run'],
                'Security'     => ['rsa-key-size', 'must-staple'],
                'Testing'      => ['staging'],
                'Automation'   => [ 'agree-tos', 'email', 'no-eff-email', 'eff-email',
                                    'disable-hook-validation', 'no-directory-hooks',
                                    'no-autorenew', 'disable-renew-updates'
                                  ]);

  return %groups;
}

sub get_certbot_options(){
  #Default option must be first in array!
  my %opts = ('rsa-key-size'	=> ['2048','4096'],
  						'dry-run'				=> ['true', 'false'],
              'max-log-backups' => ['1000', '0', '10', '20', '50', '100'],
              'staging'         => ['false', 'true'],
              'must-staple'     => ['false', 'true'],
              'agree-tos'       => ['false', 'true'],
              'no-eff-email'    => ['false', 'true'],
              'eff-email'       => ['false', 'true'],
              'disable-hook-validation' => ['false', 'true'],
              'no-directory-hooks' => ['false', 'true'],
              'no-autorenew'    => ['true', 'false'],
              'disable-renew-updates' => ['false', 'true'],
              'email'           => ['textbox']
  						);

  return %opts;
}

sub get_certbot_logdir(){
  return $config{'certbot_logdir'};
}

sub get_certbot_certs_info(){

  my @rv;
  my %cert_info;

  &open_execute_command(CMD, get_certbot_cmd().' certificates', 1);
  while(my $line = <CMD>) {

    if ($line =~ /\s+Certificate Name: (.*)/i) {
      $cert_info{'name'} = $1;
      $cert_info{'domains'} = '';
      $cert_info{'expiry_date'} = '';
      $cert_info{'staging'} = 'no';
      $cert_info{'revoked'} = 'no';
      $cert_info{'cert_path'} = '';
      $cert_info{'key_path'} = '';

    }elsif($line =~ /\s+Domains: (.*)/i){
      ($cert_info{'domains'} = $1) =~ s/ /,/g;

    }elsif($line =~ /\s+Expiry Date: ([0-9\-]+ [0-9:\+]+) \(VALID: ([0-9a-z ]+)\)?/){
      $cert_info{'expiry_date'} = $1;
      $cert_info{'valid_for'}   = $2;

    }elsif($line =~ /\s+Expiry Date: ([0-9\-]+ [0-9:\+]+) (\(INVALID:[A-Z_ ,]+\))?/){
      $cert_info{'expiry_date'} = $1;
      my $flags = $2;
      $flags =~ s/INVALID://;
      $flags =~ s/[\s\(\)]//g;
      foreach my $flag (split(',', $flags)){
        if($flag eq 'TEST_CERT'){
          $cert_info{'staging'} = 'yes';
        }
        if($flag eq 'REVOKED'){
          $cert_info{'revoked'} = 'yes';
        }
      }

    }elsif($line =~ /\s+Certificate Path: (.*)/){
      $cert_info{'cert_path'} = $1;

    }elsif($line =~ /\s+Private Key Path: (.*)/){
      $cert_info{'key_path'} = $1;
      push(@rv, {%cert_info});
    }
  }
  close(CMD);

  return @rv;
}

sub find_cert_usedin(){
  my $href = shift;
  my %rv = ();

  #TODO: support for other webservers!
  #check which certificates are installed
  if(foreign_installed('apache', 1) == 2){  #if apache is installed and configured
    foreign_require('apache', 'apache-lib.pl');
    my $conf = &apache::get_config();
    my @virt = &apache::find_directive_struct("VirtualHost", $conf);


    foreach $v (@virt) {  #for each virtual host
      my $vm = $v->{'members'};
      my $server_name = &apache::find_directive("ServerName", $vm);
      if( ($server_name eq $href->{'name'}) ||
          ($server_name eq $href->{'name'}.':443')   ){ #if its our vhost
        my $vm_cert_file = &apache::find_directive("SSLCertificateKeyFile", $vm);
        if($vm_cert_file eq $href->{'key_path'}){  #if its our cert file

          my $virt_idx = &indexof($v, @$conf);
          my ($vmembers, $vconf) = &apache::get_virtual_config($virt_idx);

          $rv{$virt_idx} = $vconf->{'file'}; #certificate is installed
        }
      }
    }
  }
  return %rv;
}

sub get_cert_info(){
  my $name = shift;
  my @cert_info = get_certbot_certs_info();
  foreach $href (@cert_info) {
    if($href->{'name'} eq $name){
      return $href;
    }
  }
  return undef;
}

sub get_hooks_dir(){
  return '/etc/letsencrypt/renewal-hooks';
}

sub get_certboot_hooks(){
  my @all_hooks = ();

  my @subdirs = ('pre', 'deploy', 'post');
  foreach $subdir (@subdirs){
    my $hooks_dir = get_hooks_dir().'/'.$subdir;
    opendir(DIR, $hooks_dir) or return @hooks;
    @hooks= grep {
      ! /^\./             	# Doesn't begins with a period
      && -f "$hooks_dir/$_" # and is a file
    } readdir(DIR);
    closedir(DIR);

    foreach $hook (@hooks){
      push(@all_hooks, $subdir.'/'.$hook);
    }
  }

  return sort @all_hooks;
}
