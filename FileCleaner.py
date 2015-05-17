from config import settings
from manage.manager import Manager
from manage.log import log

if __name__ == '__main__':
    settings = settings.get_settings()
    manager = Manager(settings)
