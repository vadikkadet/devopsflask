FROM ubuntu:20.04

COPY app /app
RUN apt-get update -y && apt-get install -y python3 python3-pip
WORKDIR /app 
RUN pip3 install -r requirements.txt
CMD export FLASK_APP=__init__.py && python3 -m flask run --host 0.0.0.0 --port 5001
