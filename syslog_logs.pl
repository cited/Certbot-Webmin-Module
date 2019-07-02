# Contains a function to supply the syslog module with extra logs

do 'certbot-lib.pl';

sub syslog_getlogs
{
  local @rv;
  my $certbot_logdir = get_certbot_logdir();

  if(! -d $certbot_logdir){
    return @rv; #return empty
  }

  opendir(DIR, $certbot_logdir) or die $!;
  my @certbot_logs = grep {
     /^[a-z0-9\.\-_]+\.log$/i     #name is .log
     && -f "$certbot_logdir/$_"   # and is a file
  } readdir(DIR);
  closedir(DIR);

  @certbot_logs = sort @certbot_logs;
  foreach my $lf (@certbot_logs){
    push(@rv,{ 'file' => $certbot_logdir.'/'.$lf,
              'desc' => $lf,
              'active' => 1,});
  }

  return @rv;
}
