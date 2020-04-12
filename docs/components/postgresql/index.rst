.. _jri-label:
.. This is a comment. Note how any initial comments are moved by
   transforms to after the document title, subtitle, and docinfo.

.. demo.rst from: http://docutils.sourceforge.net/docs/user/rst/demo.txt

.. |EXAMPLE| image:: static/yi_jing_01_chien.jpg
   :width: 1em

**********************
PostgreSQL
**********************

.. contents:: Table of Contents

Repository Manager
==================

The Repository installer and manager allows you to install your selected version of the PostgreSQL Repository.

It can be access via the Pg Installer tab as shown below:

.. image:: _static/postgresql-tab.png

You can also use the manager to install and update packages as well.

As certain packages require EPEL for CentOS, the EPEL repository is installed as well when installing on CentOS.

.. image:: _static/PostgreSQL-Repo-Manager.png

File Locations
==============

On CentOS, the PostgreSQL config direcotry is located at::

   /var/lib/pgsql/12/data
   
On Ubuntu, the PostgreSQL direcotry is located at::
   
   /etc/postgresql/12/main
   
The pg_hba.conf File
====================

On installation via the Wizard, PostgreSQL is configured for use with SSL and uses md5 authentication for all users and databases.

.. code-block:: bash
   :linenos:
   
   	local	all all 							trust
   	host	all all 127.0.0.1	255.255.255.255	md5
	host	all all 0.0.0.0/0					md5
	host	all all ::1/128						md5
	hostssl all all 127.0.0.1	255.255.255.255	md5
	hostssl all all 0.0.0.0/0					md5
	hostssl all all ::1/128						md5



The postgresql.conf File
========================

On installation via the Wizard, PostgreSQL is configured to accept connections on all interfaces as well as SSL connections.

.. code-block:: bash
   :linenos:

	#------------------------------------------------------------------------------
	# CONNECTIONS AND AUTHENTICATION
	#------------------------------------------------------------------------------

	# - Connection Settings -
	
	listen_addresses = '*'
	)
	
	
	# - SSL -

	ssl = on
   
Above are excepts.

Version
=======

GeoHelm has been tested with PostgreSQL 10, 11 and 12.

Webmin PostgreSQL Module
========================

On installation, the native PostgreSQL Database Server module is also activated.

It is located under Servers > PostgreSQL Database Server

.. image:: _static/webmin-postgresql.png


