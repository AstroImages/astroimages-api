

# List all files in a directory using os.listdir
def list_files_in_folder(basepath):
    return (entry for entry in basepath.iterdir() if entry.is_file())
