from config import settings
from filesystem.manage.filemanager import FileManager
from db.models import check_db_exists

if __name__ == '__main__':
    check_db_exists()
    settings = settings.get_settings()
    manager = FileManager(settings)
    manager.scan()
    from web import runserver
