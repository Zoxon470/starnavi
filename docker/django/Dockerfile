FROM python:3.7.3-stretch
MAINTAINER  Asadov Ahmed <zoxon470@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./starnavi-backend/Pipfile ./starnavi-backend/Pipfile.lock ./
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --clear

COPY ./docker/django/start.sh ./start.sh
RUN chmod +x start.sh

COPY ./starnavi-backend .

EXPOSE 8000