FROM python:3.10

COPY main.py .
COPY requirements.txt .

RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

RUN git clone https://github.com/archit120/DNSWhy.git

CMD gunicorn main:app