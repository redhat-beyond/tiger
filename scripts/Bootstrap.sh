#!/bin/bash
dnf -y update
dnf -y install python3-pip
pip3 install --user Flask

python3 /vagrant/scripts/app.py
