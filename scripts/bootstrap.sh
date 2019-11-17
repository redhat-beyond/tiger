#!/usr/bin/env bash
dnf -y update
dnf -y install python3-pip
pip3 install --user Flask

chmod 755 /vagrant/app.py
/vagrant/app.py
