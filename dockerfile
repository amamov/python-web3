FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN mkdir /srv/app

WORKDIR /srv/app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install --no-dev
RUN poetry shell

# EXPOSE 4000
# CMD ["python3", ]