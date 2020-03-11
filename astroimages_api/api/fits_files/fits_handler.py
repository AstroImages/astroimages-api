import os

from flask import abort
from flask import url_for
from flask import jsonify

from astroimages_api.util.file_system import list_files_in_folder
from astroimages_api.util.fits.fits_util import extract_metadata_from_fits_file


def get_fits_files_from_folder():
    folder = os.environ['FITS_FOLDER']
    fits_file_names = list_files_in_folder(folder, '.fits')

    return [extract_metadata_from_fits_file(fits_file_name) for fits_file_name in fits_file_names]


def make_public_fits_file(fits_file):
    new_fits_file = {}
    for field in fits_file:
        if field == 'id':
            new_fits_file['id'] = fits_file['id']
            new_fits_file['uri'] = url_for('get_fits_file', fits_file_id=fits_file['id'], _external=True)
        else:
            new_fits_file[field] = fits_file[field]
    return new_fits_file


def get_fits_files():
    fits_files = get_fits_files_from_folder()
    return jsonify(
        {
            'fits_files': [
                make_public_fits_file(fits_file) for fits_file in fits_files]
        }
    )


def get_fits_file(fits_file_id):
    fits_files = get_fits_files_from_folder()
    fits_file = [fits_file for fits_file in fits_files if fits_file['id'] == fits_file_id]
    if len(fits_file) == 0:
        abort(404)
    return jsonify({'fits_file': make_public_fits_file(fits_file[0])})


def register_endpoints(api_endpoint, app, api):
    version = 'v1'
    method_url = f'{api_endpoint}/{version}/fits-files'

    app.add_url_rule(f'{method_url}', 'get_fits_files', view_func=get_fits_files, methods=['GET'])
    app.add_url_rule(f'{method_url}/<int:fits_file_id>', 'get_fits_file', view_func=get_fits_file, methods=['GET'])
