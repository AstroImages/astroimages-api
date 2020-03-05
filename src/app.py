#!/usr/bin/env python

from logging.config import dictConfig

import os

from flask import Flask
from flask_restplus import Api

import routes as routes


app = Flask(__name__)
api = Api(app=app)

routes.register_endpoints(app, api)


if __name__ == '__main__':
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s - %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    DOCKER_CONTAINER = os.environ.get('DOCKER_CONTAINER', False)

    if DOCKER_CONTAINER == 'true':
        app.logger.info('Running inside container')
        app.run(debug=True, host='0.0.0.0')
    else:
        app.logger.info('Running standalone container')
        app.run(debug=True)
    
    