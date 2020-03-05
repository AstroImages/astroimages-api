#!/usr/bin/env python

from flask import Flask, jsonify

import routes as routes

app = Flask(__name__)

routes.register_endpoints(app)

if __name__ == '__main__':
    app.run(debug=True)