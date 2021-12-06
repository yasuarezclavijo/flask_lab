from core.services.app_logging import AppLogging
from core.services.app_db import AppDb
from flask_marshmallow import Marshmallow
from flask_wtf.csrf import CSRFProtect

app_logging = AppLogging()
app_db = AppDb()
ma = Marshmallow()
csrf = CSRFProtect()