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

def get_easy_settings():
    class EasySettings:
        def __init__(self, settings_obj):
            # for key, value in settings_obj['SERVER'].items():
            #     setattr(self, key, settings_obj.getboolean(value))
            self.DEBUG = settings_obj.getboolean('SERVER', 'DEBUG')
            self.PORT = int(settings_obj.get('SERVER', 'PORT'))

    return EasySettings(get_settings())



def write_default_settings():
    config = ConfigParser()
    config.optionxform = str

    config['GENERAL'] = {
        'Folders To Check': "",
    }
    config['FILTERS'] = {
        'Filter By Text': "yes",
        'Filter By File Extensions': "yes",
        'Filter Text': "sample,\n readme",
        'Filter Extensions': "nfo-orig,\n nfo,\nsfv,\nnzb"
    }
    config['LOGS'] = {
        'Location': "Local"
    }

    with open(DEFAULT_SETTINGS_PATH, 'w') as configfile:
        config.write(configfile)

    return config