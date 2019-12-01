#!/usr/bin/env bash
mv /vagrant/mysql-community.repo /etc/yum.repos.d/
dnf -y update
dnf -y install python3-pip mysql-community-server
systemctl enable mysqld.service
systemctl start mysqld.service
pip3 install -r /vagrant/requirements.txt

chmod 755 /vagrant/app.py
nohup python3 /vagrant/app.py > /dev/null 2>&1 &
