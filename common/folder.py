from common.file import File
from os import walk, stat
from os.path import join
from manage.log import log

class Folder:
    files = []
    root_path = ""

    def __init__(self, filepath, settings):
        self.root_path = filepath
        self.discover_files(filepath, settings)

    def discover_files(self, folder_root, settings):
        try:
            root, dirs, files = walk(folder_root, followlinks=False)

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
        except ValueError:
            log("Folder is empty or no access: {}".format(folder_root))

