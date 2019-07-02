
# Certbot Webmin Module

# Info
Certbot Module for Webmin.  Install and manage SSL certificates via Certbot.

# How to install via CDN

Webmin->Webmin Configuration->Webmin Modules->From ftp or http URL

URL: https://cdn.acugis.com/certbot-webmin-module/certbot.wbm.gz

md5: https://cdn.acugis.com/certbot-webmin-module/certbot.txt

Go to Servers-> Certbot (you may need to refresh page)

# How to install from GIT
Archive module

$ git clone https://github.com/AcuGIS/Certbot-Webmin-Module

$ mv Certbot-Webmin-Module certbot

$ tar -cvzf certbot.wbm.gz certbot/


Upload from Webmin->Webmin Configuration->Webmin Modules

Go to Servers-> Certbott (you may need to refresh page)

# Notes

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

## **Issues**
Please report issue here or at hello@acugis.com

Copyright
---------

* Copyright AcuGIS, 2019
* Copyright Cited, Inc., 2019
