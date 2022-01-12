from re import T
from flask import Flask, request, render_template, send_from_directory, redirect
from flask_basicauth import BasicAuth
from werkzeug.utils import secure_filename
import os, json, urllib
import ast
app = Flask(__name__, template_folder='html')
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, './temp')
ALLOWED_EXTENSIONS = {'json'}
app.config.update(TEMPLATES_AUTO_RELOAD = True)

app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def root():
    return "I AM ALIVE"