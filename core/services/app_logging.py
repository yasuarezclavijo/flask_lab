# service_app_logging.py

import logging

class AppLogging:

    def __init__(self, app=None):
        if app is not  None:
            self.init_app(app)

    def init_app(self, app):
        FORMAT = '%(asctime)s [%(levelname)-5.5s] [%(funcName)30s()] %(message)s'
        log_formatter = logging.Formatter(FORMAT)
        app.logger = logging.getLogger()
        app.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('app.log')
        file_handler.setFormatter(log_formatter)
        app.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        app.logger.addHandler(console_handler)

        return app.logger