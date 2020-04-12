************
Installation
************

Installation can be done using the pre-installer.sh script or via GIT.

Using the Pre-Installer
=======================

On a fresh CentOS 7 or Ubuntu 18 installation, the fastest method is to use the pre-installer script:

.. code-block:: console
   :linenos:
   
   wget wget https://raw.githubusercontent.com/cited/nagios-webmin-module/master/scripts/pre-install.sh
   chmod +x pre-install.sh
   ./pre-install.sh
    
The above will install Webmin, Apache HTTPD Server, and the Nagios module, as well as our (optional) Certbot Module for SSL.

When the script completes, you will see the message below:

.. code-block:: console
   :linenos:

   ~
   /opt ~
   Installed Nagios Module in /usr/share/webmin/certbot (336 kb)
   ~
   Nagios is now installed. Go to Servers > Nagios to complete installation


.. note::
    Following above, you will need to log in to Webmin to complete installation using the install :ref:`wizard-label`.



Via Git or Download
===================

You can use Git to build module for an existing Webmin installation:

.. code-block:: console
   :linenos:

    git clone https://github.com/cited/nagios-webmin-module/
    mv nagios-webmin-module-master nagios
    tar -cvzf nagios.wbm.gz nagios/

    
.. note::
    Following above, you will need to log in to Webmin to complete installation using the install :ref:`wizard-label`.   
    


