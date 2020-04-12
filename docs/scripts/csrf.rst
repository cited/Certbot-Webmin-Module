**********************
CSRF Whitelist
**********************

To whitelist your domain in GeoServer, you can use our included file.

This file is located under /scripts/csrf-whitelist.txt

The contents should be added to your /home/tomcat/apache-tomcat-{version}/webapps/geoserver/WEB-INF/web.xml file.


.. warning::
      Be sure to create a backup of your web.xml file before making any changes.
      
The file contents are below

.. code-block:: xml
   :linenos:      

      <context-param>
      <param-name>GEOSERVER_CSRF_WHITELIST</param-name>
      <param-value>yourdomain.com</param-value>
      </context-param>
     
     
You must restart Tomcat for the changes to register.
 
  .. note:: Be sure to replace yourdomain.com with your own domain above.

