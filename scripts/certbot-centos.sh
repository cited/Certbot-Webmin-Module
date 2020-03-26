#!/bin/bash -e
# Certbot Module Installation Script
# Usage: 
# wget 
# chmod +x certbot-centos.sh
# ./certbot-centos.sh

function download_certbot_module(){
	pushd /tmp/
	wget https://github.com/AcuGIS/Certbot-Webmin-Module/archive/master.zip
	unzip master.zip
	mv Certbot-Webmin-Module-master certbot
	tar -czf /opt/certbot.wbm.gz certbot
	rm -rf certbot master.zip
	popd
	
}

function install_certbot_module(){
	pushd /opt/
	/usr/libexec/webmin/install-module.pl certbot.wbm.gz
	popd
	echo -e "Certbot is now installed.  Please go to Servers > Certbot to complete installation"
	
}
yum -y install wget unzip bzip2
download_certbot_module;
install_certbot_module;
