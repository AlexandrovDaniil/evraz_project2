FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install gunicorn
RUN pip install psycopg2-binary==2.9.2

COPY ./setup.cfg .
COPY ./setup.py .
RUN pip install --upgrade -e '.[dev]'

#RUN apk add postgresql-dev
#COPY ./entrypoint.sh .
#RUN chmod +x entrypoint.sh

COPY . .
#ENTRYPOINT ["/app/setup.py"]
#ENTRYPOINT ["/app/entrypoint.sh"]
#ENTRYPOINT ["gunicorn","-b","127.0.0.1:8002", "user.composites.user_api:app", "--reload"]
ENTRYPOINT ["gunicorn","-b","0.0.0.0:1234", "user.composites.user_api:app", "--reload"]