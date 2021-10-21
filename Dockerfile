FROM ubuntu:bionic

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


RUN pip install flask
RUN pip install requests
RUN pip install flask_cors

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1


ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

COPY . $APP_HOME/

EXPOSE 5000

CMD tail -f /dev/null

CMD python ./Backend/flask_server.py
