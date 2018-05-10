# Dockerfile by Marcos Roberto

# Variaveis de ambiente
FROM centos:centos7
LABEL author="marcos.roberto@defensoria.ce.def.br"
ENV TZ=America/Fortaleza
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ARG AMBIENTE
ARG APPNAME
ARG DB_HOST
ARG DB_NAME
ARG DB_USER
ARG DB_PASS
ENV ROOT_DOMAIN defensoria.ce.def.br
ENV DOMAIN "${APPNAME}.${ROOT_DOMAIN}"
ENV PORT 8090
RUN echo ${DOMAIN}

# Acesso SSH
ENV SSH_USER defensoria
ENV SSH_PASS dpgeceti
RUN yum -y update; yum clean all
RUN yum -y install epel-release openssh-server passwd sudo
RUN mkdir /var/run/sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' 
RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' 
RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N '' 

# Dependencias PYTHON 3.4
RUN yum -y install python34-setuptools; yum clean all
RUN yum -y install python34 python34-devel nginx gcc unzip wget git
RUN easy_install-3.4 pip

# Virtualenv
RUN pip install virtualenv
RUN virtualenv -p python3 /AppEnv

# Adicionar diretórios e arquivos de configuracao
RUN mkdir -p /AppData/logs
RUN mkdir -p /AppData/repositorios
RUN mkdir -p /AppConfig/
RUN mkdir -p /AppSocket/run

COPY ./docker_setup/. /AppConfig/

# Add Usuario SSH , permissões de SUDO e arquivos para autenticacao do GIT
RUN adduser --home=/AppCode/ -u 1000 ${SSH_USER}
RUN echo -e "$SSH_PASS\n$SSH_PASS" | (passwd --stdin ${SSH_USER})
RUN echo "${SSH_USER} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${SSH_USER} && \
chmod 0440 /etc/sudoers.d/${SSH_USER}

# Adicionar pasta do código do projeto
RUN mkdir -p /AppCode/${APPNAME}
COPY . /AppCode/${APPNAME}/
RUN source /AppEnv/bin/activate ; pip install -r /AppCode/${APPNAME}/require*.txt
RUN unzip /AppConfig/static.zip -d /AppCode/${APPNAME}/app/

# Arquivos de configuracao diversos
RUN ln -s /AppConfig/django.params /etc/nginx/conf.d/
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf_orig
RUN ln -s /AppConfig/nginx.conf /etc/nginx/

# Copiando scripts principais e ajustes de permissoes
COPY ./docker_setup/run.sh /run.sh
COPY ./docker_setup/setup.sh /setup.sh
RUN chown ${SSH_USER}:nginx /*.sh
RUN chown -R ${SSH_USER}:nginx /AppCode/ && chmod +x /AppCode/
RUN chown -R ${SSH_USER}:nginx /AppData
RUN chown -R ${SSH_USER}:nginx /AppSocket/run && chmod 775 /AppSocket/run
RUN chmod 775 /*.sh
RUN /setup.sh

## Iniciar Tudo
CMD ["/run.sh"]