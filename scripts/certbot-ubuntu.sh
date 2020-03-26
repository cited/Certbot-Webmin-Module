#!/bin/bash -e
# Certbot Module Installation Script
# Usage: 
# wget https://raw.githubusercontent.com/cited/Certbot-Webmin-Module/master/scripts/certbot-ubuntu.sh
# chmod +x certbot-ubuntu.sh
# ./certbot-ubuntu.sh

function download_certbot_module(){
	pushd /tmp/
	wget https://github.com/cited/Certbot-Webmin-Module/archive/master.zip
	unzip master.zip
	mv Certbot-Webmin-Module-master certbot
	tar -czf /opt/certbot.wbm.gz certbot
	rm -rf certbot master.zip
	popd
	
}

function install_certbot_module(){
	pushd /opt/
	/usr/share/webmin/install-module.pl certbot.wbm.gz
	popd
	echo -e "Certbot is now installed.  Please go to Servers > Certbot to complete installation"
	
}
apt-get -y install wget unzip
download_certbot_module;
install_certbot_module;
