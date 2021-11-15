FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb


RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install flask_cors
RUN pip3 install Werkzeug
RUN pip3 install email-to

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1


ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

COPY . $APP_HOME/

EXPOSE 5000

CMD tail -f /dev/null

CMD python3 ./Backend/flask_server.py
