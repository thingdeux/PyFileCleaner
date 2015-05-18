from os import walk
from os.path import join
from filesystem.common.file import File
from filesystem.manage.log import log


class Folder:
    files = []
    root_path = ""

    def __init__(self, filepath, settings):
        self.root_path = filepath
        self.discover_files(filepath, settings)

    def discover_files(self, folder_root, settings):
        def walk_error(error):
            log("Error accessing folder: {}".format(error))
            raise error

        for root, dirs, files in walk(folder_root, followlinks=False, onerror=walk_error):
            for filename in files:
                file = File(filename)

                if settings['using_file_extension_filter']:
                    if file.has_extensions(settings['filter_extensions']):
                        self.files.append(file)
                        continue

                if settings['using_text_filter']:
                    if file.has_filters_in_name(settings['filter_text']):
                        self.files.append(file)
                        continue

