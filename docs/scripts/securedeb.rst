**********************
Securing Debian
**********************

To enable basic security for Debian distributions, you can use our included file.

This file is located under /scripts/secure-debian.sh

.. warning::
    The script will disable root login, create a minimally privilaged user, and IP table rules.  Proceed with caution.
    
Once file is run, the user and updated root password will be displayed as well as saved to /root/auth.txt


The script can be executed, as root, using below

.. code-block:: xml
   :linenos:
 
      cp /usr/share/webmin/geohelm/scripts/secure-debian.txt /root/secure-debian.sh
      cp /root
      chmod +x secure-debian.sh
      ./secure-debian.sh
      
 
 

Be sure to note new passwords.
 
  



 
  

