FROM debian:stretch

MAINTAINER henryk.iwaniuk@posteo.de version 1.0

RUN apt-get update && apt-get install -y apache2 && apt-get install -y git && apt-get install python3-venv;
RUN cd /opt; git clone https://github.com/SNDjango/server.git; cd server; git checkout docker;
RUN mkdir /root/install/; cp /opt/server/docker/setup.sh /root/install/setup.sh; chmod +x /root/install/setup.sh;

