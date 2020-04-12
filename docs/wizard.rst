.. _wizard-label:

************
Wizard
************

Once the module is installed, the Wizard is used to configure the components.

Go to Servers > Geohelm:

.. image:: _static/3.png

The main Wizard screen will a link for completing each step.

While most steps are self-explanatory, we will cover Tomcat and JDK selection below:

**Install Java/JDK:**

.. image:: _static/4-java.png

Select the JDK you wish to use.  We have tested with JDK 8

.. image:: _static/5-java.png

Geohelm has been tested with OpenJDK 8 and Oracle JDK 8.


**Apache Tomcat:**  

.. image:: _static/8-tomcat.png

Geohelm has been tested with Apache Tomcat 8.x and 9.x:

.. image:: _static/9-tomcat.png


**Complete Installation:**

Once each step of the Wizard is completed, the Wizard can be removed:

.. image:: _static/19-donei.png


With the Wizard completed, your module should appear as below:

.. image:: _static/start-geohelm.png

.. note::
    The Wizard may state that GeoServer is not deployed.  This is due to Tomcat not starting automatically.  Simply complete        installation and start Tomcat to deploy the GeoServer war.
    

About Haveged
===================

Haveged is an entropy generator that will provide markedly faster JVM startup times.
The caveat is that it will use much higher CPU load (although for shorter duration due
to decreased JVM start up time).  Bear this in mind if deploying on VM with limited CPU
or other critical applications.

