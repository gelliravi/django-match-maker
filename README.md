Django Match Maker
==================

You can visit a hosted version of this site at https://playerpointer.com

There are literally hundreds of public basketball courts in Singapore. I have
three in close walking distance, yet I often end up playing all alone. This app
aims to solve that problem:

* People can login via Email, Facebook or Twitter and create a
  **player profile**
* People can **create** new places (i.e. basketball courts) and give them names
* People can **check-in** at the place where they currently are.
* People can **subscribe to places** to get notifications when friends check in
  at that place (this would solve my problem *g).
* Since the app knows, who is checked in currently, it can **suggest randomized
  teams**.
* People can **rate other player's skills**, the matchmaker should take that
  skill into consideration.
* After a game, people can enter the end result and **vote for player of the
  match** (in their own team and in the other team). This will go into the
  player's skill calculation as well.
* Now we can **collect all kinds of data** which would allow us to generate a
  **high-score list** for the neighborhood, the city or even globally:
  * Ratio of won/lost games per player
  * Average playing time per player
  * Usual time of day when this player plays

This should be a mobile app but since I don't really have the time to mess
around with PhoneGap I will start with a simple website first. With HTML5
geolocation API it should actually be possible to get the whole check-in thing
up and running with just a mobile browser.

Contribute
==========

If you want to contribute, here is how you can setup the project locally:

    mkdir -p ~/Projects/matchmaker
    cd ~/Projects/matchmaker
    mkvirtualenv -p python2.7 matchmaker
    git clone git://github.com/mbrochh/django-match-maker.git src
    cd src/matchmaker
    pip install -r requirements.txt
    ./manage.py runserver

You need to install PostgreSQL 9.2 and PostGIS 2.0. On OSX The easiest way to
do that is

1. Install [Postgres.app](http://postgresapp.com/). Make sure to place the
   app in your `/Applications/` folder **before** you run it the first time.
2. Create the geospatial database::

    psql -h localhost
    create database matchmaker;
    create user matchmaker with password 'matchmaker';
    grant all privileges on database matchmaker to matchmaker;
    \connect matchmaker;
    create extension postgis;
    ./manage.py syncdb
