FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./requirements /app/requirements

RUN  pip install -r requirements/base.txt

COPY ./entrypoint.sh /app

RUN chmod +x entrypoint.sh

COPY ./ /app

CMD ["uwsgi", "--ini", "./uwsgi/uwsgi.ini"]
