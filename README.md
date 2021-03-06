# Graveyard: Place for Dead (and Undead)

Graveyard is an attempt at open-source reimplementation of [DraciDoupe.cz](https://www.dracidoupe.cz/) (referred to as DDCZ in this text).

Developer's documentation is [at Read the Docs](https://ddcz.readthedocs.io/en/latest/). 

## Contributions

Contributions are welcome provided you agree your work will be shared under the same license as Graveyard (MIT).

If you don't know where to start, take a look at issues or ask Almad on [development Slack](https://dracidoupe.slack.com/messages/C7F0YCTFU) or in Pošta on [DraciDoupe.cz](https://www.dracidoupe.cz/). 

## Installation

You can run Graveyard either directly on your machine or inside [Docker](https://www.docker.com/).

Installing and running Graveyard directly is faster (on some systems) and removes one lever of indirection, but it makes the setup more complicated. 

Running in Docker requires familiarity with it, but it makes setup easier and guarantees consistency with the testing environment (and hopefully in the future, production environment as well). 

In both cases, first clone this repository and run all commands in its directory.

### Installing in Docker

Requirements:

* You have [Docker CE installed](https://www.docker.com/community-edition)
* You have [installed docker-compose](https://docs.docker.com/compose/install/)

Verify you have everything ready by running the test suite:

* `docker-compose run web python3 manage.py test`

If you see output like this:

```
(graveyard-venv) almad@zeruel:~/projects/graveyard$ docker-compose run web python3 manage.py test
Starting graveyard_db_1 ... done
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
Destroying test database for alias 'default'...
(graveyard-venv) almad@zeruel:~/projects/graveyard$ 

```

You are all set. Afterwards, install database schema by running

*  `docker-compose run web python3 manage.py migrate`

and load data about pages

*  `docker-compose run web python3 manage.py loaddata pages`

You are done! Now you can just run the project and develop using

*  `docker-compose start`


### Installing on your machine

Graveyard is currently written in [Django](https://www.djangoproject.com/). Requirements to develop it:

* You have working Python 3 installation on your machine
* You have working MySQL installation on your machine

To use the project, clone this repository and:

* Create a virtual environment: `python3 -m venv gvenv`
* Enter it (on Mac OS X or Linux): `source gvenv/bin/activte`
* Copy settings template: `cp graveyard/settings/local.example.py graveyard/settings/local.py`
* Edit the settings above, especially enter credentials to your local MySQL
* Verify you have correct installation and run tests with `python manage.py test`. You should see output like this:

```
(graveyard-venv) almad@zeruel:~/projects/graveyard$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...........
----------------------------------------------------------------------
Ran 11 tests in 0.031s

OK
Destroying test database for alias 'default'...
(graveyard-venv) almad@zeruel:~/projects/graveyard$ 
```

* Create the database schema: `python manage.py migrate`
* Load data about pages to see what's on production: `python manage.py loaddata pages`
* Run the thing! `python manage.py runserver`
* Observe if you have contact at `http://localhost:8000`
* Maybe create a superuser in order to enter admin: `python manage.py createsuperuser`
* Look around the administration interface at `http://localhost:8000/admin/`


