.. This is a comment. Note how any initial comments are moved by
   transforms to after the document title, subtitle, and docinfo.

.. demo.rst from: http://docutils.sourceforge.net/docs/user/rst/demo.txt

.. |EXAMPLE| image:: static/yi_jing_01_chien.jpg
   :width: 1em

**********************
Apache Tomcat
**********************

.. contents:: Table of Contents

Layout
======

For installations done using the Wizard, the Apache Tomcat (CATALINA) home directory is::

   /home/tomcat/apache-tomcat-v/
   
Where apache-tomcat-v is the version you chose to install.

The CATALINA_HOME variable is set both in the Tomcat init script as well as setenv.sh files.


Starting and Stopping
=====================

There are two ways to start/stop/restart Tomcat.

1.  Via Module, using the Stop/Start/Restart buttons as shown below::

   .. image:: _static/tomcat-functions.png

2.  Via SSH, using the following commands

.. code-block:: console
   :linenos:

    /etc/init.d/tomcat { start | stop | restart | status }
    

Init Script
===========

The Tomcat init script is located in /etc/init.d and has the following content.

.. code-block:: bash
   :linenos:



	#!/bin/bash
	### BEGIN INIT INFO
	# Provides:        tomcat
	# Required-Start:  $network
	# Required-Stop:   $network
	# Default-Start:   2 3 4 5
	# Default-Stop:    0 1 6
	# Short-Description: Start/Stop Tomcat server
	### END INIT INFO

	# Source function library.
	. /etc/environment;	#Catalina variables
	. $CATALINA_HOME/bin/setenv.sh

	RETVAL=$?

	function start(){
	echo "Starting Tomcat"
	/bin/su - tomcat $CATALINA_HOME/bin/startup.sh
	RETVAL=$?
	}

	function stop(){
	echo "Stopping Tomcat"
	/bin/su - tomcat -c "$CATALINA_HOME/bin/shutdown.sh 60 -force"
	RETVAL=$?
	}

	case "$1" in
 	start)
		start;
        ;;
 	stop)
		stop;
        ;;
 	restart)
		echo "Restarting Tomcat"
    	stop;
		start;
        ;;
 	status)

		if [ -f "${CATALINA_PID}" ]; then
			TOMCAT_PID=$(cat "${CATALINA_PID}")
			echo "Tomcat is running with PID ${TOMCAT_PID}";
			RETVAL=1
		else
			echo "Tomcat is not running";
			RETVAL=0
		fi
		;;
 	*)
        echo $"Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
	esac
	exit $RETVAL




Version
=======

GeoHelm has been tested with Tomcat 8.x and 9.x

