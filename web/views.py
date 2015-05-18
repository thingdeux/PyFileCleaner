from web import app
from flask import render_template

@app.route("/")
def index():
    from db.models import File, Folder
    folders = Folder.query.all()
    return render_template('index.html',
                           folders=folders,
                           name=index)

@app.route("/purge")
def purge():
    return render_template('purge.html', name=purge)

@app.route("/settings")
def config():
    return render_template('settings.html', name=config)