.. This is a comment. Note how any initial comments are moved by
   transforms to after the document title, subtitle, and docinfo.

.. demo.rst from: http://docutils.sourceforge.net/docs/user/rst/demo.txt

.. |EXAMPLE| image:: static/yi_jing_01_chien.jpg
   :width: 1em

**********************
GeoServer
**********************

.. contents:: Table of Contents
Overview
==================

GeoHelm installs the latest, stable version of GeoServer.

The GeoServer tab checks that GeoServer is installed.

.. image:: _static/geoserver-tab.png

If not, it can be installed using the "Install Now" button.

This will install the latest, stable version of GeoServer.

Important: GeoServer is an optional component on the GeoHelm Java Version.

If you do not wish to install it, simply do not do so.

Location
================== 

By default, GeoServer is installed at /home/tomcat/apache-tomcat-<version>/webapps/geoserver

To make upgrading easier, you should always change the GeoServer Data Directory location.

To install GeoServer extensions, see our guide

As we can see above, the creation of our NewReports Directory has been added to the directory structure.  This is true for all directories and sub directories added.

Geoserver Extensions
====================

GeoServer Extensions can be installed as below.

Below, we are installing the MapFish Print Module via SSH.

1. Switch to user tomcat

.. code-block:: console
   :linenos:

   su - tomcat
   

2. Change to the GeoServer /lib directory (adjust for your own file path)

.. code-block:: console
   :linenos:

   cd /home/tomcat/apache-tomcat-8.5.15/webapps/geoserver/WEB-INF/lib
   

3. Download the desired extension, making sure to match the version to your GeoServer version

.. code-block:: console
   :linenos:

   wget http://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/extensions/geoserver-2.16.2-printing-plugin.zip


4. Unzip the downloaded file

.. code-block:: console
   :linenos:

   unzip -q geoserver-2.16.2-printing-plugin.zip


5. Remove the zip file

.. code-block:: console
   :linenos:

   rm -f geoserver-2.16.2-printing-plugin.zip

6. Restart Tomcat for the extension to take effect.

.. Note:: Some components, such as GDAL, require additional configuration. 


Data Directory
==============

To make GeoServer more portable and easier to upgrade, you should change the GeoServer data directory.

Follow the instructions below, substituting your own paths and file names.

1. Stop Tomcat

2. Connect via SSH and move the data directory as below: (Important: the target directory - 'geo_data' below - should not exist.)

.. code-block:: console
   :linenos:

   mv /home/tomcat/apache-tomcat-8.5.15/webapps/geoserver/data/ /var/lib/geo_data/ 

3. Add the following to your GeoServer web.xml file:

.. code-block:: console
   :linenos:

   <context-param>
       <param-name>GEOSERVER_DATA_DIR</param-name>
       <param-value>/var/lib/geo_data</param-value>
   </context-param>
 
   <context-param>
      <param-name>GEOSERVER_REQUIRE_FILE</param-name>
      <param-value>/var/lib/geo_data/global.xml</param-value>
   </context-param>   

4. Start Tomcat

You should log into GeoServer and verify that your workspaces, etc.. are accesible.    

