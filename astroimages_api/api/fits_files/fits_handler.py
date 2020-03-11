from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth

fits_files = [
    {
        'id': 1,
        'title': u'NGC3051',
        'description': u'NGC3051', 
        'path': '/sdsdf/sdfsdfs/NGC3051.fits'
    },
    {
        'id': 2,
        'title': u'NGC4040',
        'description': u'NGC4040', 
        'path': '/sdsdf/sdfsdfs/NGC4040.fits'
    }
]


def make_public_fits_file(fits_file):
    new_fits_file = {}
    for field in fits_file:
        if field == 'id':
            new_fits_file['uri'] = url_for('get_fits_file', fits_file_id=fits_file['id'], _external=True)
        else:
            new_fits_file[field] = fits_file[field]
    return new_fits_file


def get_fits_files():
    return jsonify({'fits_file': [make_public_fits_file(fits_file) for fits_file in fits_files]})

def get_fits_file(fits_file_id):
    fits_file = [fits_file for fits_file in fits_files if fits_file['id'] == fits_file_id]
    if len(fits_file) == 0:
        abort(404)
    return jsonify({'fits_file': make_public_fits_file(fits_file[0])})


def register_endpoints(api_endpoint, app, api):
    version = 'v1'
    method_url = f'{api_endpoint}/{version}/fits-files'

    app.add_url_rule(f'{method_url}', 'get_fits_files', view_func=get_fits_files, methods=['GET'])
    app.add_url_rule(f'{method_url}/<int:fits_file_id>', 'get_fits_file', view_func=get_fits_file, methods=['GET'])
