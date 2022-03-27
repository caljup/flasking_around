import sqlite3

import click
from flask import current_app, g 
from flask.cli import with_appcontext

#Establishes initial connection to database when request is sent through
#Database location is taken from configuration object
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db

#Close database conenction prior to sending response
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

#Initializes database from SQL statements in schema.sql
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

#Click (Command line interface creation kit) establishes
#command line call init-db on init_db function and returns success message
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

#Registers database commands with the application instance
#Closes database when cleaning up after response and allows initialization of db
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
