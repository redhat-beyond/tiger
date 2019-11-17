#!/bin/bash
yum -y update
yum -y install python3-pip
pip3 install --user Flask
#python3 vagrant/scripts/app.py Still need to figure this one out. for the time being, it'll run using Vagrantfile
