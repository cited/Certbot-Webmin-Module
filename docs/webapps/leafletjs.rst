.. This is a comment. Note how any initial comments are moved by
   transforms to after the document title, subtitle, and docinfo.

.. demo.rst from: http://docutils.sourceforge.net/docs/user/rst/demo.txt

.. |EXAMPLE| image:: static/yi_jing_01_chien.jpg
   :width: 1em

**********************
LeafletJS
**********************

.. contents:: Table of Contents

Demo App
========

A simple LeafletJS demo app using OpenLayers and GeoServer is available via the Home Page.

Click the LeafletJS link on the home page or navigate to:

https://yourdomain.com/LeafletDemo.html


Structure and Code
==================

.. code-block:: html
   :linenos:
   
   
   	<html lang="en">
  	<head>
    	<meta charset="utf-8">
    	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    	<meta name="viewport" content="initial-scale=1,user-scalable=no,maximum-scale=1,width=device-width">
    	<title>Example Leaflet</title>
   	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.1.0/dist/leaflet.css"
   	integrity="sha512-wcw6ts8Anuw10Mzh9Ytw4pylW8+NAD4ch3lqm9lzAsTxg0GFeJgoAtxuCLREZSC5lUXdVyo/7yfsqFjQ4S+aKw=="
   	crossorigin=""/>

    	<script src="https://unpkg.com/leaflet@1.1.0/dist/leaflet.js"
   	integrity="sha512-mNqn2Wg7tSToJhvHcqfzLMU6J4mkOImSPTxVZAdo+lcPlk+GhZmYgACEe0x35K7YzW1zJ7XyJV/TT1MrdXvMcA=="
   	crossorigin=""></script>
  	</head> 
  	<style>
    	body {
      	padding: 0;
      	margin: 0;
    	}
    	html, body, #map {
      	height: 100%;
    	}
  	</style>
	<body>
    	<div id="map"></div>    
    	<script>
    	var map = L.map('map').setView([0, 0], 2);        
    	var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  	var osmAttrib='Data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
  	var osm = new L.TileLayer(osmUrl, {minZoom: 2, maxZoom: 8, attribution: osmAttrib});
    	map.addLayer(osm);
	//change localhost below to your IP or hostname
    	var wmsLayer= L.tileLayer.wms("http://localhost/geoserver/wms", {
        layers: 'topp:states',
        format: 'image/png',
        transparent: true
    	});
    	map.addLayer(wmsLayer);    
    	</script>
	</html>
	
Version
=======

By default, the latest version of LeafletJS is installed by the Wizard


Troubleshooting
===============

If the included LeafletJS demo does not render, or renders only the base map, check the following:

1. Be sure you have the correct IP or hostname in the /var/www/html/Leaflet.html page

2. Be sure you have started GeoServer

3. If both of above are eliminated, restart Apache HTTP Server


