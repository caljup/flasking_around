import os
# from config import Config

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskrdumb.sqlite')
    )
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from .auth.auth import authorization_bp
    app.register_blueprint(authorization_bp)

    from .chili_dogs.chili_dogs import chili_dogs_bp
    app.register_blueprint(chili_dogs_bp)

    from .dumb_fortunes.dumb_fortunes import dumb_fortunes_bp
    app.register_blueprint(dumb_fortunes_bp)

    from .football_stats.football_stats import football_stats_bp
    app.register_blueprint(football_stats_bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

