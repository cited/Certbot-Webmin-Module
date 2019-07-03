
# Certbot Webmin Module

# Info
Certbot Module for Webmin.  Install and manage SSL certificates and Certbot plugins via Webmin.

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

# Additional
- CentOS has more Certbot plugins
- Apache vconf is not updated, after deleting a certificate!

## **Issues**
Please report issue here or at hello@acugis.com

# Certbot Links
- [Certbot User Guide](https://certbot.eff.org/docs/using.html)
- [Certbot config file](https://certbot.eff.org/docs/using.html#config-file)

Copyright
---------

* Copyright AcuGIS, 2019
* Copyright Cited, Inc., 2019
