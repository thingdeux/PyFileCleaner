from common.folder import Folder
from config.settings import get_settings

class Manager():
    settings = None
    folders = []

    def __init__(self, settings):
        self.settings = settings
        self.init_settings()
        self.create_folders()

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



    # Should probably log if no files come back in any of the folders


if __name__ == '__main__':
    settings = get_settings()
    man = Manager(settings)
    pass