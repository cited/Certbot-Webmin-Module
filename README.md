
# Certbot Webmin Module

[![Documentation Status](https://readthedocs.org/projects/certbot-webmin-module/badge/?version=latest)](https://certbot.citedcorp.com/en/latest/?badge=latest)

# Info
Certbot Module for Webmin.  Install and manage SSL certificates and Certbot plugins via Webmin.

# Quick Install

1. Log into Webmin
2. Go to Webmin Configuration > Webmin Modules
3. Select "From HTTP or FTP Url"
4. Enter https://github.com/cited/Certbot-Webmin-Module/blob/master/scripts/certbot.wbm.gz?raw=true
5. Click the Install button.


# Install via Script

As Root:

```bash

wget https://raw.githubusercontent.com/cited/Certbot-Webmin-Module/master/scripts/pre-install.sh

chmod +x pre-install.sh

./pre-install.sh
```

When script completes. go to Servers-> Certbot to complete installation.

# How to install from GIT
Archive module

$ git clone https://github.com/cited/Certbot-Webmin-Module

$ mv Certbot-Webmin-Module-master certbot

$ tar -cvzf certbot.wbm.gz certbot/


Upload from Webmin->Webmin Configuration->Webmin Modules

Go to Servers-> Certbott (you may need to refresh page)

# CLI

You can add items to the cli.ini using below:

1. Click on the Config icon:

![config](https://user-images.githubusercontent.com/655540/210635536-59ff1641-5095-490b-b51f-a68874359ddf.jpg)

2. Add the required line(s) to the cli.ini file.

![cli](https://user-images.githubusercontent.com/655540/210635555-ac53987a-558f-479d-9460-010c8b18433a.jpg)

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

* Copyright AcuGIS, 2020
* Copyright Cited, Inc., 2020
