#!/usr/bin/env bash
mv /tmp/start-sql-config.txt /etc/yum.repos.d/mysql-community.repo
dnf -y update
dnf -y install mysql-community-server
systemctl enable mysqld.service
systemctl start mysqld.service
dnf -y install python3-pip
pip3 install -r /vagrant/requirements.txt

chmod 755 /vagrant/app.py
nohup python3 /vagrant/app.py > /dev/null 2>&1 &
