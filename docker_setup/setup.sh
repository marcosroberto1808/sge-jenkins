#!/bin/bash

## SETUP INICIAL
__setup_app() {

if [ -z ${DOMAIN} ]; then
    echo "Error - Nome de domínio vazio!"
    exit 1
fi
# Ajustes dos arquivos de configuração
HOST=`echo ${DOMAIN} | cut -f1 -d '.'`
sed -i "s/DOMAIN/${DOMAIN}/g" /${DOMAIN}/cfg/*
sed -i "s/HOST/${HOST}/g" /${DOMAIN}/cfg/*
sed -i "s/PORT/${PORT}/g" /${DOMAIN}/cfg/*
sed -i "s/APPNAME/${APPNAME}/g" /${DOMAIN}/cfg/*
sed -i "s/SSH_USER/${SSH_USER}/g" /${DOMAIN}/cfg/*

# Ajustes do arquivo .ENV
sed -i "s/DB_USER/${DB_USER}/g" /${DOMAIN}/cfg/.env
sed -i "s/DB_PASS/${DB_PASS}/g" /${DOMAIN}/cfg/.env
sed -i "s/DB_HOST/${DB_HOST}/g" /${DOMAIN}/cfg/.env
sed -i "s/DB_NAME/${DB_NAME}/g" /${DOMAIN}/cfg/.env
sed -i "s/DOMAIN/${DOMAIN}/g" /${DOMAIN}/cfg/.env

# Configurar local para o uwsgi socket
mkdir /${DOMAIN}/run/
chown ${SSH_USER}:nginx /${DOMAIN}/run/
chmod 775 /${DOMAIN}/run/

echo "O código do projeto está em: /${DOMAIN}/code/${HOST}/" 

# Salvar nome de domínio usado 
echo "${DOMAIN}" > /.django
}

# Mover e ajustar diretórios do código
__move_dir() {
mv /${DOMAIN}/codigo /${DOMAIN}/code/${HOST}
mv /${DOMAIN}/cfg/.env /${DOMAIN}/code/${HOST}/
unzip /${DOMAIN}/cfg/static.zip -d /${DOMAIN}/code/${HOST}/app/
chown -R ${SSH_USER}:nginx /${DOMAIN}/code/${HOST}/
chmod +x /${DOMAIN}/code/
}

# Instalar requirementes.txt
__install_requirements() {
HOST=`echo ${DOMAIN} | cut -f1 -d '.'`
echo "Executando a instalacao: pip install requirements.txt" 
source /AppEnv/bin/activate ; pip install -r /${DOMAIN}/code/${HOST}/require*.txt
}

## Chamar Funcoes
__setup_app
__move_dir
__install_requirements