.. This is a comment. Note how any initial comments are moved by
   transforms to after the document title, subtitle, and docinfo.

.. demo.rst from: http://docutils.sourceforge.net/docs/user/rst/demo.txt

.. |EXAMPLE| image:: static/yi_jing_01_chien.jpg
   :width: 1em

**********************
CLI
**********************

.. contents:: Table of Contents

Installing PgRouting
==================

PgRouting can be enabled on your PostgreSQL database via the Extension tab or via Command Line.

.. Note::
	PostGIS must be enabled priort to installing PgRouting

Command Line
============

To install via command line:

1. Connect to PostgreSQL

.. code-block:: console
   :linenos:

   root@geohelm:~# su - postgres
   postgres@geohelm:~$ psql
   psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
   Type "help" for help.

   postgres=#

 

2. If you have not created a database, create one now.

.. code-block:: console
   :linenos:

   postgres=# create database geohelm;
   CREATE DATABASE
   postgres=# 

3. Connect to your database.

.. code-block:: console
   :linenos:

   postgres=# \c geohelm
   You are now connected to database "geohelm" as user "postgres".
   geohelm=#

4. Install the PostGIS extension.

.. code-block:: console
   :linenos:

   geohelm=# create extension postgis;
   CREATE EXTENSION
   geohelm=#
   
5.  Install the PgRouting extension.

.. code-block:: console
   :linenos:

   geohelm=# create extension pgrouting;
   CREATE EXTENSION
   geohelm=#

Note: GeoHelm also includes fuzzy_match_string, tiger, postgis_topology.

 
5. Verify the installation via command line or the PostgreSQL Management Page

.. code-block:: console
   :linenos:

   geohelm=# \d
               List of relations
   Schema |       Name        | Type  |  Owner
   --------+-------------------+-------+----------
   public | geography_columns | view  | postgres
   public | geometry_columns  | view  | postgres
   public | raster_columns    | view  | postgres
   public | raster_overviews  | view  | postgres
   public | spatial_ref_sys   | table | postgres
   (5 rows)

 
Extensions Tool
===============

To install using the Extension installer, click on the Extensions tab as shown below.

.. image:: _static/postgis-tab.png

1. Select the target database from the drop-down as shown below.

.. image:: _static/postgis-select-db.png 

.. Note:: You must FIRST install PostGIS prior to installing PgRouting.


2. Tick the PostGIS select button and then click the Save button as show below:

.. image:: _static/postgis-enable.png 	

 
3. Once PostGIS has been installed on a target database, you can then return to install PgRouting:

.. image:: _static/postgis-install-more.png 	
	
.. Note:: 
   You can also un-install Extensions using above. 



