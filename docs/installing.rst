************
Installation
************

Installation can be done using the instalr.sh script or via GIT.

Using the Install Script
=======================

Get the script, make it executable and run the script:

.. code-block:: console
   :linenos:
   
   wget https://raw.githubusercontent.com/AcuGIS/GeoHelm/master/scripts/install.sh
   chmod +x pre-install.sh
   ./pre-install.sh
    
The above will the Certbot module.

When the script completes, you will see the message below:

.. code-block:: console
   :linenos:

   ~
   /opt ~
   Installed CertBot in /usr/share/webmin/certbot (336 kb)
   ~
   Certbot is now installed. Go to Servers > GeoHelm to complete installation


.. note::
    Following above, you will need to log in to Webmin to complete installation using the install :ref:`wizard-label`.



Via Git or Download
===================

You can use Git to build module for an existing Webmin installation:

.. code-block:: console
   :linenos:

    git clone https://github.com/cited/Certbot-Webmin-Module
    mv Certbot-Webmin-Module-Master certbot
    tar -cvzf certbot.wbm.gz certbot/

    
.. note::
    Following above, you will need to log in to Webmin to complete installation using the install :ref:`wizard-label`.   
    


