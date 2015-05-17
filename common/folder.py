from common.file import File
from utils import discover_files

class Folder:
    files = []
    root_path = ""

    def __init__(self, filepath):
        self.root_path = filepath
        filenames = discover_files(filepath)
        self.add_files(filenames)

    def add_files(self, filenames):
        for filename in filenames:
            self.files.append(File(filename))


