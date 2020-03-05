#!/usr/bin/env python

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth

import task_handler as task_handler


def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def register_endpoints(app):


    app.add_url_rule('/todo/api/v1/tasks', 'get_tasks', view_func=task_handler.get_tasks, methods=['GET'])
    app.add_url_rule('/todo/api/v1/tasks/<int:task_id>', 'get_task', view_func=task_handler.get_task, methods=['GET'])

    app.add_url_rule('/todo/api/v1/tasks', 'create_task', view_func=task_handler.create_task, methods=['POST'])
    app.add_url_rule('/todo/api/v1/tasks/<int:task_id>', 'update_task', view_func=task_handler.update_task, methods=['PUT'])
    app.add_url_rule('/todo/api/v1/tasks/<int:task_id>', 'delete_task', view_func=task_handler.delete_task, methods=['DELETE'])

    app._register_error_handler(None, 404, not_found)

