FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install gunicorn
RUN pip install kombu
RUN pip install amqp

RUN pip install psycopg2-binary==2.9.2

COPY ./setup.cfg .
COPY ./setup.py .
RUN pip install --upgrade -e '.[dev]'

COPY . .

ENTRYPOINT ["gunicorn","-b","0.0.0.0:1236", "issue.composites.issue_api:app", "--reload"]