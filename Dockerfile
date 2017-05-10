FROM python:alpine
LABEL description ="Simple bot to send dankmemes." version="0.1"

COPY requirements.txt /opt/app/
COPY dankmeme.py /opt/app/
WORKDIR /opt/app/

RUN pip install -r requirements.txt

CMD [ "python", "./dankmeme.py" ]

