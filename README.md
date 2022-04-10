# globant_assessment
Globant assessment

STEP 1 CONFIGURATION

This project use poetry to run and install dependencies
INSTALL POETRY
https://python-poetry.org/docs/#installation

After install poetry run the follow commands to activate the poetry environment and install the dependencies

- poetry shell
- poetry install

STEP 2 DJANGO PROJECT CONFIGURATION

Apply makemigrations and migrate to django project with the follow commands

- python manage.py makemigrations
- python manage.py migrate

Create a superuser to login in project and get the access credentials with the follow command

- python manage.py createsuperuser --email admin@example.com --username admin

STEP 3 CONFIGURE ENVIRONMENT VARIABLES

This project use an API key to connect to the Open Weather API, and this key should be in .env file

Create a copy of the .example.env file in the same folder and call it .env

API_WEATHER_API_KEY=WRITE HERE THE KEY

For this purpouse here is the not private key
KEY=1508a9a4840a5574c822d70ca2132032


STEP 4 RUN PROJECT AND USE THE WEATHER API

To run the project run the follow command on the terminal
IMPORTANT: You need to have the poetry environent activated to run the project (poetry shell).

- python manage.py runserver

Access to the API use the follow example url http://127.0.0.1:8000/api/weather/santiago/cl/

 http://127.0.0.1:8000/api/weather/{CITY}/{COUNTRY}/

CITY is the name of the city to get weather eg. BOGOTA
COUNTRY is the country code to get weather eg. CO

TO RUN TEST

In poetry shell run the follow command
- python manage.py test apps
