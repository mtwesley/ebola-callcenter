
from flask import Blueprint, render_template, redirect
from .db import *

ui = Blueprint("_ui", __package__,  template_folder="tmpl")


@ui.route("/")
def index():
    return render_template("new_call.tpl")


@ui.route("/calls/")
def all_calls():
    return redirect("/")


@ui.route("/calls/new", endpoint="new_call")
def new_call():
    return render_template("01.html")


@ui.route("/calls/<int:call_id>")
def view_call(call_id):
    rs = Call.query.filter( Call.id == call_id )

    return render_template("03.html")