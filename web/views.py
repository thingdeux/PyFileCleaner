from web import app
from flask import render_template, Response
from filesystem.manage.log import log

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
    from db.models import Folder
    folders = Folder.query.all()

    return render_template('delete.html',
                           folders=folders,
                           name=delete)

@app.route("/delete/<file_or_folder>/<object_id>/", methods=['POST'])
def delete_file_or_folder(file_or_folder, object_id):
    # TODO: Should do this all in a background task

    from db.models import Folder, File, Log, db
    from filesystem.common.file import File as FSFile

    if file_or_folder == "folder":
        try:
            # Query all files in the folder, delete them
            files_to_delete = File.query.filter_by(folder_id=object_id)
            for file in files_to_delete:
                file_to_delete = FSFile(file.path)
                file_to_delete.delete()
                log("Deleted File: {}".format(file.path), log_type="INFO")
                db.session.add(Log("Deleted File: {}".format(file.path), "INFO"))
                db.session.delete(file)
            db.session.commit()
            return Response(status=200)
        except OSError as e:
            log("Problem Deleting File: {}".format(e))

    elif file_or_folder == "file":
        try:
            db_file = File.query.filter_by(id=object_id).first()
            to_delete = FSFile(db_file.path)
            to_delete.delete()

            log("Deleted File: {}".format(db_file.path), log_type="INFO")
            db.session.add(Log("Deleted File: {}".format(db_file.path), "INFO"))
            db.session.delete(db_file)
            db.session.commit()
            return Response(status=200)
        except ValueError as e:
            log("No File.ID found to delete: {}".format(e))




@app.route("/move/<file_id>/", methods=['POST'])
def move_file(file_id):
    from db.models import File
    # Move File
    print(file_id)
    return (Response(status=200))


@app.route("/settings")
def config():
    return render_template('settings.html', name=config)


def purge_log():
    from db.models import File, Log
    Log.pruneLogs()

