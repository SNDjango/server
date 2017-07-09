FROM debian:stretch

MAINTAINER henryk.iwaniuk@posteo.de version 1.0

RUN apt-get update && apt-get install -y apache2 && apt-get install -y libapache2-mod-wsgi-py3 && apt-get install -y git && apt-get install -y python3-venv;

COPY ./ /opt/server/

RUN chmod +x /opt/server/docker/setup.sh && /opt/server/docker/setup.sh

EXPOSE 80

CMD export TUGAG_DB_PASSWORD=$(cat /etc/secrets/djangouserpw); /usr/sbin/apache2ctl -D FOREGROUND

