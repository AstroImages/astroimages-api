FROM ubuntu:18.04

MAINTAINER Rodrigo de Souza "rsouza01@gmail.com"
LABEL Author="Rodrigo de Souza"
LABEL E-mail="rsouza01@gmail.com"
LABEL version="0.0.1"


RUN apt-get update && apt-get upgrade -y && apt-get clean

ENV DOCKER_CONTAINER true
ENV FLASK_APP "astroimages_api/server.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True


RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN update-alternatives --set python /usr/bin/python3.7
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./astroimages_api /app/astroimages_api

ENV PYTHONPATH "${PYTHONPATH}:./astroimages_api"


ENTRYPOINT [ "python" ]

CMD [ "./astroimages_api/server.py" ]
