.. This is a comment. Note how any initial comments are moved by
   transforms to after the document title, subtitle, and docinfo.

.. demo.rst from: http://docutils.sourceforge.net/docs/user/rst/demo.txt

.. |EXAMPLE| image:: static/yi_jing_01_chien.jpg
   :width: 1em

**********************
OpenLayers
**********************

.. contents:: Table of Contents

Demo App
========

A simple OpenLayers demo app using OpenLayers and GeoServer is available via the Home Page.

Click the OpenLayers link on the home page or navigate to:

https://yourdomain.com/OpenLayersDemo.html


Structure and Code
==================

.. code-block:: HTML
   :linenos:
   
   	<html>
  	<head>
    	<title>OpenLayer Demo</title>
    
   	<link rel="stylesheet" href="OpenLayers/ol.css" type="text/css">
        
    	<script src="OpenLayers/ol.js"></script>    
    	</head>
  	<body>
    	<div id="map" class="map"></div>
    	<script>
      	var layers = [
        new ol.layer.Tile({
          source: new ol.source.OSM()
        }),
        new ol.layer.Image({
          extent: [-13884991, 2870341, -7455066, 6338219],
          source: new ol.source.ImageWMS({

            //Replace 'localhost' below with your server IP or hostname 

            url: 'http://localhost/geoserver/wms',  
            params: {'LAYERS': 'topp:states'},
            ratio: 1,
            serverType: 'geoserver'
          })
        })
      	];
      	var map = new ol.Map({
        layers: layers,
        target: 'map',
        view: new ol.View({
          center: [-10997148, 4569099],
          zoom: 4
        })
      	});
    	</script>
  	</body>
	</html>
	
Version
=======

By default, the latest version of OpenLayers is installed by the Wizard


Troubleshooting
===============

If the included OpenLayers demo does not render, or renders only the base map, check the following:

1. Be sure you have the correct IP or hostname in the /var/www/html/OpenLayersDemo.html page

2. Be sure you have started GeoServer

3. If both of above are eliminated, restart Apache HTTP Server


