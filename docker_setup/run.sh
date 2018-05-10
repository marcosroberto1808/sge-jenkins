#!/bin/bash

#Checar diretorios
if [ ! -d /AppData/logs ]; then
    mkdir -p /AppData/logs
fi

if [ ! -d /AppData/repositorios ]; then
    mkdir -p /AppData/repositorios
fi

# run uwsgi in background
DOMAIN=`cat /.django` 

source /AppEnv/bin/activate ; uwsgi --ini /AppConfig/django.ini --uid 1000 --gid 1000 &

# start nginx
exec nginx & 

# start sshd
/usr/sbin/sshd -D