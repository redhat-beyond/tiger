#!/usr/bin/env bash
os=$(awk -F= '/^NAME/{print $2}' /etc/os-release)
echo $os
if [ $os == '"Ubuntu"' ] 
then
    echo "im ubuntu"
    apt-get update
    # !----------! Setting MySQL root user password root/root !----------!
    debconf-set-selections <<< 'mysql-server mysql-server/root_password password LoginPass@@11223344'
    debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password LoginPass@@11223344'
    # !----------! install python and mysql !----------!
    apt-get -y install python3-pip mysql-server mysql-client
    


else
    echo "im fedora"
    cp /vagrant/mysql-community.repo /etc/yum.repos.d/
    dnf -y update
    dnf -y install python3-pip mysql-community-server


    old_pw=$(grep 'temporary password' /var/log/mysqld.log | awk '{print $NF}')
    new_pw='LoginPass@@11223344'
    mysqladmin -u root -p"$old_pw" password "$new_pw"

fi
pip3 install -r /vagrant/requirements.txt
    systemctl enable mysql
    systemctl start mysql
    new_pw='LoginPass@@11223344'
    mysql -u root -p"$new_pw" <<MYSQL_SCRIPT
    CREATE DATABASE tiger;
    USE tiger;
    CREATE TABLE users(username VARCHAR(20), password VARCHAR(100) NOT NULL, create_date TIMESTAMP NOT NULL, PRIMARY KEY(username));
    CREATE TABLE messages(username VARCHAR(20),create_date TIMESTAMP NOT NULL,content VARCHAR(100) NOT NULL,FOREIGN KEY(username) REFERENCES users(username));
    SHOW TABLES;
    DESCRIBE users;
    DESCRIBE messages;
MYSQL_SCRIPT
   
    chmod 755 /vagrant/app.py
    nohup python3 /vagrant/app.py > /dev/null 2>&1 &