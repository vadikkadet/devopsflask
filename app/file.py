from flask import Blueprint, render_template
import os.path
from flask_autoindex import AutoIndex
from flask_login import login_required
file = Blueprint('file', __name__)
files_index = AutoIndex(file, os.path.curdir + '/Flask/files', add_url_rules=False)
# Custom indexing
@file.route('/files')
@file.route('/files/<path:path>')
@login_required
def autoindex(path='.'):
    return files_index.render_autoindex(path)