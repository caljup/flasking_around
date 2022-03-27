This repo concerns itself with Flask application factory and buleprint build practices.
It is designed to load blueprint modules upon build.

Core Blueprints:

- Authentication and Login
        - Allows users to create and login to accounts
        - Requires running database initialization commmands listed below
- This is a Painting of Chili Dawgs
        - Display picture of chili dog painting
- Dumb Fortunes
        - Queries database before displaying returned fortune to user
- Please God, Tell Me the Bengals Won
        - Grabs and displays the 2021 - 2022 Cincinnati Bengals schedule and results from ESPN
        - Requires running database initialization commands listed below


If running in a test environment navigate to the base directory in the CLI and run the following:

```sh
export FLASK_APP=flasking_around
export FLASK_ENV=developement
flask run
```

Once application is running and database initialization CLI command has been registered with it run:


```sh
flask init-db
Initialized the database.
```

You can then test user addition and Dumb Fortunes.
