from configparser import ConfigParser
import os

# Default path is the root of the ProjectDirectory
DEFAULT_PATH = os.path.dirname(os.path.dirname(__file__))
DEFAULT_SETTINGS_PATH = os.path.join(DEFAULT_PATH, "Settings.conf")
MAX_LOG_SIZE = 10 * (1024*1024)

def get_settings():
    config = ConfigParser()
    config.optionxform = str
    # Make sure the settings file exists, if not create it with the default keys/settings
    config.read(DEFAULT_SETTINGS_PATH)

    if (config.sections() == []):
        to_return = write_default_settings()
        return to_return

    return config

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

    return config