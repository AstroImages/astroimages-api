#!/usr/bin/env python

from flask import Flask
from flask_restplus import Api

import routes as routes

app = Flask(__name__)
api = Api(app=app)

routes.register_endpoints(app, api)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0')
    