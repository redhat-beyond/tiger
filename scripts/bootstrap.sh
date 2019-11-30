#!/usr/bin/env bash

dnf -y update
dnf -y install python3-pip
pip3 install -r /vagrant/requirements.txt



chmod 755 /vagrant/app.py
nohup python3 /vagrant/app.py > /dev/null 2>&1 &
