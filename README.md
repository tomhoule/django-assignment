# Django assignment (3mw interview)

[![Build Status](https://travis-ci.org/tomhoule/django-assignment.svg?branch=master)](https://travis-ci.org/tomhoule/django-assignment)

This app is deployed here: https://django3mw.kafunsho.be/

## Testing

The tests can be run via manage.py once the requirements are met:

        python3 manage.py test

or via docker-compose, with all the dependencies taken care of:

        docker-compose run assignment python3 manage.py test

## Running

        docker-compose run assignment

And visit localhost:8000

Alternatively:

        python3 manage.py runserver

## What should be done next

On a real project, the following additional steps should probably be taken:

  - Switch to a more scalable database, like postgres
  - Set up an assets pipeline, maybe vendor bootstrap, and serve static files
  - Use `coverage` to get detailed data on test overage
  - Make the templates more modular (separate the nav bar...)
  - Maybe package it (write a setup.py, etc.)

Details on some technical choices are available in the commit messages.
