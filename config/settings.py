from configparser import ConfigParser
import os

# Default path is the root of the ProjectDirectory
DEFAULT_PATH = os.path.dirname(os.path.dirname(__file__))
DEFAULT_SETTINGS_PATH = os.path.join(DEFAULT_PATH, "settings.conf")

def get_settings():
    config = ConfigParser()
    config.optionxform = str
    # Make sure the settings file exists, if not create it with the default keys/settings
    config.read(DEFAULT_SETTINGS_PATH)

    if (config.sections() == []):
        write_default_settings()


def write_default_settings():
    config = ConfigParser()
    config.optionxform = str

    config['GENERAL'] = {
        'Folders To Check': "",
        'Action': "Touch"
    }
    config['FILTERS'] = {
        'Filter By Text': "False",
        'Filter By File Extensions': "True",
        'Filter Text': "sample",
        'Filter Extensions': ".mkv, .nfo"
    }
    config['LOGS'] = {
        'Location': "Local"
    }

    with open(DEFAULT_SETTINGS_PATH, 'w') as configfile:
        config.write(configfile)
