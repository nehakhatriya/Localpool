# Localpool
> Community driven delivery platform for the ones who need it the most

## Instructions to install

1. **Install PostgreSQL and PostGIS**
perform an installation directly on the host operating system:
    - [Download](https://www.postgresql.org/download/) the official PostgreSQL installer for your system.
    - [Install](https://postgis.net/install/) the PostGIS extension

2. **Install `python3.7` and `pip3`**
3. **Install Django and other dependencies**
    `pip install -r requirements.text`

## Instructions to run
1. **Start Django web server (Make sure the virtual environment is activated)**
    `python manage.py runserver`

## To write psql queries
1. Run `psql` on the terminal
2. enable the PostGIS extension by typing `enable extension postgis`

