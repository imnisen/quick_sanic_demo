FROM python:3.6-jessie
MAINTAINER zhimian


COPY ./ /opt
RUN mv /opt/config/config.bak /opt/config/config.ini

RUN pip3 install -r /opt/requirements.txt -i https://mirrors.aliyun.com/pypi/simple

EXPOSE 6623

CMD ["/bin/bash", "-c", "/opt/docker_run.sh"]