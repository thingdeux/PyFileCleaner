from web import app
from flask import render_template

@app.route("/")
def index():
    from db.models import File, Log
    ext_counts = File.get_extension_counts()
    latest_logs = Log.get_latest_logs()

    return render_template('index.html',
                           counts=ext_counts,
                           logs=latest_logs,
                           name=index)

@app.route("/purge")
def purge():
    return render_template('purge.html',name=purge)



@app.route("/delete")
def delete():
    from db.models import File, Folder
    folders = Folder.query.all()

    return render_template('delete.html',
                           folders=folders,
                           name=delete)

@app.route("/settings")
def config():
    return render_template('settings.html', name=config)