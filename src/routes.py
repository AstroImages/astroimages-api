#!/usr/bin/env python

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth

import task_handler as task_handler
import fits_handler as fits_handler


def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def register_endpoints(app, api):

    #task_handler.register_endpoints('/todo/api/', app, api)
    fits_handler.register_endpoints('/api', app, api)

    app._register_error_handler(None, 404, not_found)

