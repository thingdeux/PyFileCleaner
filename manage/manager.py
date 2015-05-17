from common.file import File
from common.folder import Folder
import shutil
from config.settings import get_settings

class Manager():
    settings = None
    folders = []

    def __init__(self, settings):
        self.settings = settings
        self.create_folders()

    def create_folders(self):
        folder_list = self.settings.get('GENERAL', 'Folders To Check')

        for folder in folder_list.split(','):
            self.folders.append(Folder(folder.strip('\n')))

        # Should probably log if no files come back in any of the folders


if __name__ == '__main__':
    settings = get_settings()
    man = Manager(settings)
    pass