from os import walk
from os.path import join
from filesystem.common.file import File
from filesystem.manage.log import log


class Folder:
    def __init__(self, filepath, settings):
        self.files = []
        self.root_path = filepath
        self.discover_files(settings)

    def discover_files(self, settings):
        def walk_error(error):
            if error is PermissionError:
                log("Error accessing folder: {}".format(error))

        for root, dirs, files in walk(self.root_path, followlinks=False, onerror=walk_error):
            for filename in files:
                file = File(join(root, filename))

                if settings['using_file_extension_filter']:
                    if file.has_extensions(settings['filter_extensions']):
                        self.files.append(file)
                        continue

                if settings['using_text_filter']:
                    if file.has_filters_in_name(settings['filter_text']):
                        self.files.append(file)
                        continue

