FROM python:3.11
LABEL maintainer="s@mck.la"
ARG MY_APP_PATH=/opt/shortlink-api

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ntp \
    && mkdir -p ${MY_APP_PATH}/data

COPY data ${MY_APP_PATH}/data
ADD main.py requirements.txt app.py shortlink.py ${MY_APP_PATH}
RUN pip3 install -r ${MY_APP_PATH}/requirements.txt 

WORKDIR ${MY_APP_PATH}


VOLUME [${MY_APP_PATH}/data]

ENTRYPOINT python3 -u app.py

EXPOSE 8000/tcp
