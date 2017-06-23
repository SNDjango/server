FROM debian:stretch

MAINTAINER henryk.iwaniuk@posteo.de version 1.0

RUN apt-get update && apt-get install -y apache2 && apt-get install -y libapache2-mod-wsgi-py3 && apt-get install -y postgresql && apt-get install -y git && apt-get install -y python3-venv;
RUN cd /opt; git clone https://github.com/SNDjango/server.git; cd server; git checkout docker;
RUN mkdir /root/install/; cp /opt/server/docker/setup.sh /root/install/setup.sh; chmod +x /root/install/setup.sh;

EXPOSE 80

CMD /usr/sbin/apache2ctl -D FOREGROUND

