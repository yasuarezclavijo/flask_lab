from core.services.app_logging import AppLogging
from core.services.app_db import AppDb
from flask_marshmallow import Marshmallow

app_logging = AppLogging()
app_db = AppDb()
ma = Marshmallow()