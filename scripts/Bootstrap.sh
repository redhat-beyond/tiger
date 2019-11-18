#!/usr/bin/env bash
dnf -y update
dnf -y install python3-pip
pip3 install Flask

chmod 755 /vagrant/app.py
/vagrant/app.py
