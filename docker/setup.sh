#!/bin/bash

echo "SNDjango setup"

echo "sndjangocore" > /etc/hostname

cd /opt/server/

echo "Setting up python environment"
pyvenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

cd snd
python manage.py migrate
cd ..


echo "setting up permissions"
chmod 664 /opt/server/snd/db.sqlite3
chmod 775 /opt/server/snd
chmod 775 -R /opt/server/snd/media

chown :www-data /opt/server/snd/db.sqlite3
chown :www-data /opt/server/snd

echo "configuring apache"
cp docker/100-sndjango.conf /etc/apache2/sites-available/
a2dissite 000-default.conf
a2ensite 100-sndjango.conf
apachectl restart

