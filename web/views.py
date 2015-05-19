from web import app
from flask import render_template, Response

@app.route("/")
def index():
    from db.models import File, Log
    ext_counts = File.get_extension_counts()
    latest_logs = Log.get_latest_logs()

    return render_template('index.html',
                           counts=ext_counts,
                           logs=latest_logs,
                           name=index)


@app.route("/logs/<page>/")
def log_full_view(page):
    if page:
        from db.models import Log
        offset_logs = Log.get_logs_by_offset(offset=int(page)*30, limit=30)
        log_count = Log.query.count()
        more_results = False

        if offset_logs.count() >= 30:
            more_results = True

        return render_template('logs.html',
                               logs=offset_logs,
                               log_count = log_count,
                               next_page=int(page) + 1,
                               more_results=more_results,
                               name=log_full_view)
    else:
        pass

@app.route("/purge/<to_purge>/", methods=['POST'])
def purge(to_purge):
    if to_purge == "logs":
        purge_log()
        return Response(status=200)

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


def purge_log():
    from db.models import File, Log
    Log.pruneLogs()

