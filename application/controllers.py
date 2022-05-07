from flask import  render_template, request
from flask_login import login_user, logout_user, current_user
from flask_login.utils import login_required
from werkzeug.utils import redirect
from application.db_init import db
import requests
from datetime import datetime
import sys
from os import path
from flask import current_app as app 


@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")
