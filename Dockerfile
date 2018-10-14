FROM python:3.6-alpine
LABEL description "Simple bot to send dankmemes." version "0.2"

WORKDIR /opt/app/

COPY requirements.txt /opt/app/
RUN pip install -r requirements.txt

COPY dankmeme.py /opt/app/

CMD [ "python", "./dankmeme.py" ]

