# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -qq -y gcc netcat python3-dev libpq-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt

# copy entrypoint.sh          Script para saber se o banco de dados esta rodando ou não
#COPY ./DjangoApp/entrypoint.sh .

# copy project
# copia tudo que tem aqui e joga para o container com o comando ./ .
COPY ./ .

#/DjangoApp/ 
# run entrypoint.sh                 Script para saber se o banco de dados esta rodando ou não
#ENTRYPOINT ["/usr/src/app/dev_entrypoint.sh"]

CMD python manage.py runserver 0.0.0.0:8000