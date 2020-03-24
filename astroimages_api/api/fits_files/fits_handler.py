import os

from flask import abort
from flask import jsonify

# from astroimages_api.util.file_system import list_files_in_folder
# from astroimages_fits.fits_util_functions import extract_metadata_from_fits_file
from astroimages_api.api.fits_files.fits_service import FitsFileService

from astroimages_file_drivers.factory import get_file_driver
from astroimages_file_drivers.handler_enums import FILE_HANDLER_TYPE


def get_fits_files():

    # TODO: FILE HANDLER TYPE should be injected (rsouza01)
    file_handler = get_file_driver(FILE_HANDLER_TYPE.LOCAL)

    fitsFileService = FitsFileService(os.environ['FITS_FOLDER'], file_handler)
    fits_files = fitsFileService.get_fits_files()

    return jsonify(
        {
            'fits_files': fits_files
        }
    )


def get_fits_file(fits_file_id):
    # TODO: FILE HANDLER TYPE should be injected (rsouza01)
    file_handler = get_file_driver(FILE_HANDLER_TYPE.LOCAL)

    fitsFileService = FitsFileService(os.environ['FITS_FOLDER'], file_handler)
    fits_files = fitsFileService.get_fits_files()

    fits_file = [fits_file for fits_file in fits_files if fits_file['id'] == fits_file_id]

    if len(fits_file) == 0:
        abort(404)

    return jsonify(
        {
            'fits_file': fits_file
        }
    )


def register_endpoints(api_endpoint, app, api):
    version = 'v1'
    method_url = f'{api_endpoint}/{version}/fits-files'

    app.add_url_rule(f'{method_url}', 'get_fits_files', view_func=get_fits_files, methods=['GET'])
    app.add_url_rule(f'{method_url}/<string:fits_file_id>', 'get_fits_file', view_func=get_fits_file, methods=['GET'])
