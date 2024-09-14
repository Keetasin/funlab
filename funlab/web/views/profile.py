import datetime
import mongoengine as me

from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    session,
    current_app,
    send_file,
    abort,
)
from flask_login import login_user, logout_user, login_required, current_user

from funlab.models import users
from .. import oauth2
from .. import acl
from .. import forms

module = Blueprint("profile", __name__, url_prefix="/profile")


@module.route("/")
def index():
    return render_template("profile/index.html",
                           username=current_user.username,
                           email=current_user.email,
                           created_date = current_user.created_date)
