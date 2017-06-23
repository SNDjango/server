#!/bin/bash

echo "Setup"
service start apache2
service start postgresql
service status apache2
service status postgresql
