**********************
Securing RHEL
**********************

To enable basic security for REHL distributions, you can use our included file.

This file is located under /scripts/secure-rhel.sh

.. warning::
    The script will disable root login, create a minimally privilaged user, and IP table rules.  Proceed with caution.
    
Once file is run, the user and updated root password will be displayed as well as saved to /root/auth.txt


The script can be executed, as root, using below

.. code-block:: xml
   :linenos:
 
      cp /usr/libexec/webmin/geohelm/scripts/secure-rhel.txt /root/secure-rhel.sh
      cp /root
      chmod +x secure-rhel.sh
      ./secure-rhel.sh
      
 
 

Be sure to note new passwords.
 
  


