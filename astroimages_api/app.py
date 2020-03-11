#!/usr/bin/env python

import logging.config

import os

from flask import Flask
from flask_restplus import Api

import settings as settings
import routes as routes


app = Flask(__name__)
api = Api(app=app)

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), './logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    routes.register_endpoints(app, api)


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    log.info('FITS_FOLDER: {}'.format(os.environ['FITS_FOLDER']))

    DOCKER_CONTAINER = os.environ.get('DOCKER_CONTAINER', False)

    if DOCKER_CONTAINER == 'true':
        app.logger.info('Running inside container')
        app.run(debug=True, host='0.0.0.0')
    else:
        app.logger.info('Running standalone container')
        app.run(debug=True)


if __name__ == '__main__':
    main()
