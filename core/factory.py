# factory.py

from flask import Flask, request, g, url_for,  current_app,  render_template
from flask import Blueprint
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap

from services import app_logging, app_db, ma
from settings import INSTALLED_APPS

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.ConfigDevelopment')
    # services
    app.logger = app_logging.init_app(app)
    app_db.init_app(app)
    ma.init_app(app)
    Bootstrap(app)
    csrf = CSRFProtect()
    csrf.init_app(app)

    @app.teardown_appcontext
    def teardown_db(response_or_exception):
        if hasattr(app_db, 'session'):
            app_db.session.remove()
    from app import app_bp
    app.register_blueprint(app_bp)

    for mod_name in INSTALLED_APPS:
        mod = __import__(mod_name, fromlist=['app'])
        for var in vars(mod).values():
            if isinstance(var, Blueprint):
                app.register_blueprint(var)

    return app
