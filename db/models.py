from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from web import app
from config.settings import DEFAULT_PATH
from collections import Counter
from datetime import datetime


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/{}'.format(DEFAULT_PATH, 'app.db')
db = SQLAlchemy(app)


class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    path = db.Column(db.String(512))
    files = db.relationship('File')

    def __init__(self, Folder):
        self.path = Folder.root_path

    def __repr__(self):
        return '<Folder {}>'.format(self.path)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    path = db.Column(db.String(512))
    size = db.Column(db.Float)
    extension = db.Column(db.String(256))
    folder_id = db.Column(db.Integer, db.ForeignKey(Folder.id))


    def __init__(self, File, parent_folder):
        self.path = File.path
        self.name = File.filename
        self.extension = File.extension
        self.size = File.size
        self.folder_id = parent_folder

    @staticmethod
    def get_extension_counts():
        all_files = File.query.all()
        extensions = [x.extension for x in all_files]
        return Counter(extensions)


    def __repr__(self):
        return '<File {}>'.format(self.path)

class Log(db.Model):
    """
    I really only want to keep a handful of logs in this DB. There will be a rotating local log,
    this is mostly for an easy peak into the file log on the Dashboard.
    """
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(512))
    log_type = db.Column(db.String(256))
    time = db.Column(db.DateTime)

    def __init__(self, message, type):
        self.message = message
        self.log_type = type
        self.time = datetime.now()

    @staticmethod
    def get_latest_logs():
        return Log.query.order_by(desc(Log.id)).limit(30)

    @staticmethod
    def get_logs_by_offset(offset=0, limit=50):
        return Log.query.order_by(desc(Log.id)).offset(offset).limit(limit)

    @staticmethod
    def pruneLogs():
        f = Log.query.order_by(desc(Log.id))[30:]
        for log in f:
            db.session.delete(log)
        db.session.commit()

    def __repr__(self):
        return '<Log-{}: {}>'.format(self.time, self.message)

def check_db_exists():
    try:
        Folder.query.count()
        File.query.count()
        Log.query.count()
    except:
        db.create_all()


