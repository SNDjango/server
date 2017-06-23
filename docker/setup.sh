#!/bin/bash

echo "SNDjango setup"

echo "sndjangocore" > /etc/hostname

cd /opt/server/

echo "Setting up python environment"
pyvenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

