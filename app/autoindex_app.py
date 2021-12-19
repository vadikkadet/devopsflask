"""Простейшее автоиндексирование."""

import os.path
from flask import Flask
from flask_autoindex import AutoIndex
app = Flask(__name__)
AutoIndex(app, browse_root=os.path.abspath("files"))
app.run(host="0.0.0.0")