#!/bin/bash
yum -y update
yum -y install python3-pip
pip3 install --user Flask
python3 /home/vagrant/tiger.sync/scripts/f_hw.py
