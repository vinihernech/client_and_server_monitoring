FROM python:3.8.5

COPY . /app

WORKDIR /app

RUN pip install nslookup==1.4.0 && pip install requests==2.25.1 && pip install icmplib==2.1.1
