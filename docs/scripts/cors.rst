**********************
Enable CORS
**********************

To enable CORS for your Tomcat instance, you can use our included file.

This file is located under /scripts/cors.txt

The contents should be added to the line just before </web-app> in your /home/tomcat/apache-tomcat-{version}/conf/web.xml

.. warning::
      Be sure to create a backup of your web.xml file before making any changes.
      

The file Contents are below

.. code-block:: xml
   :linenos:
   
   
            <filter>
            <filter-name>CorsFilter</filter-name>
            <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>
            <init-param>
                  <param-name>cors.allowed.origins</param-name>
                  <param-value>*</param-value>
            </init-param>
            <init-param>
                  <param-name>cors.allowed.methods</param-name>
                  <param-value>GET,POST,HEAD,OPTIONS,PUT</param-value>
            </init-param>  
            </filter>
            <filter-mapping>
            <filter-name>CorsFilter</filter-name>
            <url-pattern>/*</url-pattern>
            </filter-mapping>
      
You must restart Tomcat for the changes to register.
 
.. note:: The above script is very permissive.  You should refine your CORS filter to reflect usage.
