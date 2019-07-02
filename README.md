# Info
Certbot module for Webmin

Copyright Cited, Inc. 2017

# How to install
Archive module

	$ git clone http://git.sh8.eu/LymonHead/certbot.git
	$ tar -cvzf certbot.wbm.gz certbot/

Upload from Webmin->Webmin Configuration->Webmin Modules

# Authenticated theme Issues
	- save_cfg.cgi - redirect() hides the Webmin menu!

# Links
- [certbot User Guide](https://certbot.eff.org/docs/using.html)
- [certbot config file](https://certbot.eff.org/docs/using.html#config-file)

#TODO
- Shadow max-log-backups in 'CLI Options', if wehave a logrotate.d certbot file
- Options in cli.ini with spaces (var = value), are not respected from our editor!
- Add Nginx plugins for CertBot in setup.cgi

# Notes
- CentOS has more Certbot plugins
- Apache vconf is not updated, after deleting a certificate!
