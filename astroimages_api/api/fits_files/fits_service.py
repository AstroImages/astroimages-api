from astroimages_api.util.file_system import list_files_in_folder
from astroimages_fits.fits_util_functions import extract_metadata_from_fits_file


class FitsFileService:
    def __init__(self, folder):
        self.folder = folder
        self.files = []
        self.FITS_EXTENSION = '.fits'

    def get_fits_files(self):
        """
        Method that retrieves a list of every file in self.folder.

        Returns:
        string[]: List all files in a directory using os.listdir.

        """
        fits_file_names = list_files_in_folder(self.folder, self.FITS_EXTENSION)

        self.files = [
            extract_metadata_from_fits_file(fits_file_name) for fits_file_name in fits_file_names
        ]

        return self.files

    def get_fits_file(self, fits_file_id, refresh_listing=False):
        if refresh_listing:
            self.get_fits_files()

        result = [fits_file for fits_file in self.files if fits_file['id'] == fits_file_id]

        return result[0] if result else None

