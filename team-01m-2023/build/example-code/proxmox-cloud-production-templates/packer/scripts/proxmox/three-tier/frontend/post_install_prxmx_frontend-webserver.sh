#!/bin/bash

# Install and prepare frontend web server - Example for ExpressJS/NodeJS

sudo apt-get update
sudo apt-get install -y curl rsync
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-setuptools
sudo apt-get install -y python3-pip
sudo apt-get install -y gunicorn
sudo apt-get install -y default-libmysqlclient-dev
sudo apt-get install -y python3-django python3-django-allauth python3-mysqldb
sudo apt-get install -y python3-whitenoise
pip install whitenoise
sudo apt-get install -y python3 -m pip install -U channels

# Service File to Django to Start at Boot
cp /home/vagrant/team-01m-2023/code/services/django.service /etc/systemd/system
sudo systemctl enable django.service

# Navigate to djgano code folder and install superuser
cd /home/vagrant/team-01m-2023/code/google
python3 manage.py collectstatic
sudo systemctl restart django.service
# Skip creating the superuser for now and do it manually
# python3 manage.py createsuperuser --noinput

###############################################################################
# Using Find and Replace via sed to add in the secrets to connect to MySQL
# There is a .env file containing an empty template of secrets -- essentially
# this is a hack to pass environment variables into the vm instances
###############################################################################

sudo sed -i "s/FQDN/$FQDN/" /home/vagrant/team-01m-2023/code/google/google/settings.py
sudo sed -i "s/DBUSER/$DBUSER/" /home/vagrant/team-01m-2023/code/google/google/settings.py
sudo sed -i "s/DBPASS/$DBPASS/" /home/vagrant/team-01m-2023/code/google/google/settings.py
sudo sed -i "s/DATABASENAME/$DATABASENAME/" /home/vagrant/team-01m-2023/code/google/google/settings.py

#Make database migrations
#python3 manage.py makemigrations
#python3 manage.py migrate
# Skip creating the superuser for now and do it manually
#python3 manage.py createsuperuser --noinput
#sudo systemctl restart django.service