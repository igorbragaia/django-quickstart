# Django quick-start project

It is just the code produced after following this [Youtube tutorial](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=11042s).

The purpose of this quick-start is to learn how to setup the django environment for a full stack web application using docker+nginx+vue+django deployed to EC2 with github actions.

## Virtual environment commands

Creates the virual environment

```shell script
python3 -m venv venv
```

Gets into the virtual environment

```shell script
source venv/bin/activate
```

Gets out of the virtual environment
```shell script
deactivate
```

## Django commands

Creates a new django app boilerplate
```shell script
python manage.py startapp myapp
```

Creates the new migrations
```shell script
python manage.py makemigrations
```

Runs the new migrations on the database
```shell script
python manage.py migrate
```

Starts the server
```shell script
python manage.py runserver
```