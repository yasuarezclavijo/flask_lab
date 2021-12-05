#  run.py

import core.factory as factory

app = factory.create_app()

if __name__ == '__main__':
    app.run(host= '0.0.0.0')