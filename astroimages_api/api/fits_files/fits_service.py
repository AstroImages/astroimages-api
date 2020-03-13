from astroimages_api.util.file_system import list_files_in_folder
from astroimages_fits.fits_util_functions import extract_metadata_from_fits_file


class FitsFileService:
    def __init__(self, folder):
        self.folder = folder

    def get_fits_files_from_folder(self):
        fits_file_names = list_files_in_folder(self.folder, '.fits')

        return [extract_metadata_from_fits_file(fits_file_name) for fits_file_name in fits_file_names]

    def get_fits_files(self):
        return self.get_fits_files_from_folder()

    def get_fits_file(self, fits_file_id):
        fits_files = self.get_fits_files_from_folder()
        return [fits_file for fits_file in fits_files if fits_file['id'] == fits_file_id]
