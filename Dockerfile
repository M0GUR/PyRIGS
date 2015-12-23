FROM       python:2.7

WORKDIR    /var/app

RUN     pip install virtualenv
RUN        virtualenv /var/app

ADD     . /var/app
RUN     if [ -f /var/app/packages.txt ]; then apt-get update && cat /var/app/packages.txt | xargs apt-get install -y; fi
RUN     if [ -f /var/app/requirements.txt ]; then /var/app/bin/pip install -r /var/app/requirements.txt; fi

EXPOSE  8000

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
