from os.path import getsize
from shutil import copy2, move

from filesystem.manage import log


class File:
    path = ""
    filename = ""
    extension = ""

    def __init__(self, path):
        self.path = path
        # Might only work on Unix filesystems
        # Account for windows with \\ potentially
        self.filename = path.split('/')[-1:][0]
        extension = self.filename.split('.')

        # Catch files that have no extension
        if len(extension) > 1:
            self.extension = extension[-1:][0]

    def get_size(self):
        BYTES_TO_MEGABYTES = 1024 * 1024
        return getsize(self.filename) / BYTES_TO_MEGABYTES

    def move(self, destination):
        move(self.filename, destination)

    def copy(self, destination):
        copy2(self.filename, destination)

    def has_extension(self, extension):
        if self.extension is not None:
            if self.extension == extension:
                return True
            return False
        else:
            return False

    def has_extensions(self, extension_list):
        has_extension = False
        for extension in extension_list:
            if self.has_extension(extension):
                has_extension = True
                break
        return has_extension

    def has_filter_in_name(self, filter_name):
        if self.filename is not None:
            if filter_name in self.filename:
                return True
            return False
        else:
            log("Error: File does not have a name: {}".format(self.path))
            raise ValueError

    def has_filters_in_name(self, filter_name_list):
        has_filter = False
        for name_filter in filter_name_list:
            if self.has_filter_in_name(name_filter):
                has_filter = True
                break
        return has_filter