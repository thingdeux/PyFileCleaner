from flask.ext.sqlalchemy import SQLAlchemy
from web import app
from config.settings import DEFAULT_PATH

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


    def __repr__(self):
        return '<File {}>'.format(self.path)


def check_db_exists():
    try:
        Folder.query.all().first()
        File.query.all().first()
    except:
        db.create_all()