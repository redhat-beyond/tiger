#!/usr/bin/env bash
cp /vagrant/mysql-community.repo /etc/yum.repos.d/
dnf -y update
dnf -y install python3-pip mysql-community-server
systemctl enable mysqld.service
systemctl start mysqld.service
pip3 install -r /vagrant/requirements.txt

old_pw=$(grep 'temporary password' /var/log/mysqld.log | awk '{print $NF}')
new_pw='LoginPass@@11223344'
mysqladmin -u root -p"$old_pw" password "$new_pw"
mysql -u root -p"$new_pw" <<MYSQL_SCRIPT
CREATE DATABASE tiger;
USE tiger;
CREATE TABLE users(username VARCHAR(20), password VARCHAR(100) NOT NULL, create_date TIMESTAMP NOT NULL, PRIMARY KEY(username));
CREATE TABLE messages(username VARCHAR(20),create_date TIMESTAMP NOT NULL,content VARCHAR(100) NOT NULL,FOREIGN KEY(username) REFERENCES users(username));
MYSQL_SCRIPT

chmod 755 /vagrant/app.py
nohup python3 /vagrant/app.py > /dev/null 2>&1 &
