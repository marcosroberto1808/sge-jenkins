#!/bin/bash

## SETUP INICIAL
__setup_app() {

if [ -z ${DOMAIN} ]; then
    echo "Error - Nome de domínio vazio!"
    exit 1
fi
# Ajustes do arquivo .ENV
mv /AppConfig/python-env /AppCode/${APPNAME}/.env
sed -i "s/DB_USER/${DB_USER}/g" /AppCode/${APPNAME}/.env
sed -i "s/DB_PASS/${DB_PASS}/g" /AppCode/${APPNAME}/.env
sed -i "s/DB_HOST/${DB_HOST}/g" /AppCode/${APPNAME}/.env
sed -i "s/DB_NAME/${DB_NAME}/g" /AppCode/${APPNAME}/.env
sed -i "s/APP_DOMINIO/${DOMAIN}/g" /AppCode/${APPNAME}/.env

# Ajustes dos arquivos de configuração
HOST=`echo ${DOMAIN} | cut -f1 -d '.'`
sed -i "s/DOMAIN/${DOMAIN}/g" /AppConfig/*
# sed -i "s/HOST/${HOST}/g" /AppConfig/*
sed -i "s/PORT/${PORT}/g" /AppConfig/*
sed -i "s/APPNAME/${APPNAME}/g" /AppConfig/*
sed -i "s/SSH_USER/${SSH_USER}/g" /AppConfig/*

echo "O código do projeto está em: /AppCode/${APPNAME}/" 

# Salvar nome de domínio usado 
echo "${DOMAIN}" > /.django
}

## Chamar Funcoes
__setup_app