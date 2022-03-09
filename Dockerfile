FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD gunicorn --workers=2 --threads=2 --bind=0.0.0.0:19999 main:app --daemon