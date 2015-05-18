from filesystem.common.folder import Folder
from db.models import File as dbFile
from db.models import Folder as dbFolder
from db.models import db

class FileManager():
    settings = None
    folders = []

    def __init__(self, settings):
        self.settings = settings
        self.init_settings()

    def scan(self):
        self.folders = []
        self.create_folders()
        self.update_folders()

    def create_folders(self):
        for folder in self.folder_list:
            settings = {
                'using_file_extension_filter': self.using_file_extension_filter,
                'using_text_filter': self.using_text_filter,
                'filter_extensions': self.filter_extensions,
                'filter_text': self.filter_text
            }

            self.folders.append(Folder(folder, settings))

    def init_settings(self):
        self.action_to_take = self.settings.get('GENERAL', 'Action')
        self.action_reason = self.settings.get('GENERAL', 'Action Reason')
        self.using_text_filter = self.settings.getboolean('FILTERS', 'Filter By Text')
        self.using_file_extension_filter = self.settings.getboolean('FILTERS', 'Filter By File Extensions')
        self.log_location = self.settings.get('LOGS', 'Location')

        # Remove all carriage returns and extra spaces for lists
        self.folder_list = [self.sanitize_setting(x) for x in
                            self.settings.get('GENERAL', 'Folders To Check').split(',')]

        self.filter_text = [self.sanitize_setting(x) for x in
                            self.settings.get('FILTERS', 'Filter Text').split(',')]

        self.filter_extensions = [self.sanitize_setting(x) for x in
                                  self.settings.get('FILTERS', 'Filter Extensions').split(',')]

    def sanitize_setting(self, setting_text):
        # Strip out any carriage returns or extra spaces
        str_to_return = setting_text.strip('\r')
        str_to_return = str_to_return.strip(' ')
        str_to_return = str_to_return.strip('\n')
        return str_to_return

    def update_folders(self):
        for folder in self.folders:
            existing_folder = dbFolder.query.filter_by(path=folder.root_path).first()
            if existing_folder == None:
                created_folder = dbFolder(folder)

                for file in folder.files:
                    created_file = dbFile(file, created_folder.id)
                    db.session.add(created_file)
                db.session.add(created_folder)

        db.session.commit()
