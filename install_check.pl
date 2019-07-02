# install_check.pl

do 'certbot-lib.pl';

# is_installed(mode)
# For mode 1, returns 2 if the server is installed and configured for use by
# Webmin, 1 if installed but not configured, or 0 otherwise.
# For mode 0, returns 1 if installed, 0 if not
sub is_installed
{
  if($mode == 1){
      if(-r $config{'certbot_config'} && has_command('certbot')){
        return 2;
      }elsif(-r $config{'certbot_config'}){
        return 1;
      }else{
        return 0;
      }
  }

  if($mode == 0){
      return (-r $config{'certbot_config'}) ? 1:0;
  }
}
