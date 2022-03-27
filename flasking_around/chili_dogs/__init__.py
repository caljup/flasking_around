import os
# from config import Config

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskrdumb.sqlite')
    )

    # if test_config is None:
    #     app.config.from_pyfile('config.py')
    # else:
    #     app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from .auth.auth import authorization_bp
    app.register_blueprint(authorization_bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/this-is-a-painting-of-chili-dogs')
    def chili_dogs_painting():
        return render_template('chili_dog_painting.html')
    
    @app.route('/dumb_fortunes')
    def dumb_fortunes():
        return render_template('dumb_fortunes.html')

    @app.route('/football')
    def football_statistics():
        return render_template('football_statistics.html')
    
    return app
        

 

# @app.route('/the_beauty_of_data')
# def data_analytics():
#     render_template('the_beauty_of_data.html')
