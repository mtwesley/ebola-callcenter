
from flask import Blueprint, render_template, request, session, redirect, url_for, g
from .db import *

ui = Blueprint("_ui", __package__,  template_folder="tmpl")


def save_session():
    phone = Phone()
    if "phone_id" not in session:
        phone = Phone.query.filter(Phone.id == session["phone_id"]).first()

    phone.msisdn = session["msisdn"]
    phone.save()


    contact = Contact()
    contact.name = session["name"]
    contact.sex = session["sex"]
    contact.lang = session["lang"]
    contact.county = session["county"]
    contact.city = session["city"]
    contact.location = contact.community = session["location"]
    contact.save()

    call = Call()

    call.phone_id = phone.id
    call.contact_id = contact.id
    call.type = session["call_type"]

    call.save()

@ui.route("/")
def index():
    return render_template("new_call.tpl")


@ui.route("/new/", methods=["GET", "POST"])
def new_call():
    if request.method == "POST":
        msisdn = request.form.get("msisdn", None)
        old_msisdn = session.get("msisdn", None)
        # if msisdn is not None and not old_msisdn == msisdn:
        #     res = Phone.query.filter(Phone.msisdn == msisdn).first()
        #     if res:
        #         session["phone_id"] = res.id
        #         session["patients"] = Call.query.filter(Call.phone_id == res.id).all()

        session["msisdn"] = msisdn

        if "phone_id" not in session:
            return redirect(url_for(".stage_11"))

        else:
            return redirect(url_for(".stage_one"))

    else:
        session.clear()

    return render_template("phone_no.tpl")

@ui.route("/new/1", methods=["GET", "POST"])
def stage_one():
    return ""


@ui.route("/new/2")
def stage_two():

    fon = session.get('fon')
    if fon is None:
        return redirect(url_for(".index"))

    msisdn = request.form.get("msisdn", None)
    if msisdn is not None and not fon.msisdn == msisdn:
        res = Phone.query.filter(Phone.msisdn == msisdn)
        if res:
            session['fon'] = res

    return render_template("call_1.tpl")

@ui.route("/new/11", methods=["GET", "POST"])
def stage_11():
    if request.method == "POST":
        f = request.form

        session["first_name"] = f.get("name_first", "")
        session["middle_name"] = f.get("name_middle", "")
        session["last_name"] = f.get("name_last", "")
        session["suffix_name"] = f.get("suffix","").lower().replace("none", "")
        session["name"] = "%(name_first)s %(name_middle)s %(name_last)s" % f

        return redirect(url_for(".stage_12"))

    return render_template("stage_11.tpl")


@ui.route("/new/12", methods=["GET", "POST"])
def stage_12():
    if request.method == "POST":
        session["sex"] = request.form.get("sex", "")
        return redirect(url_for(".stage_13"))

    return render_template("stage_12.tpl")

@ui.route("/new/13", methods=["GET", "POST"])
def stage_13():
    if request.method == "POST":
        session["lang"] = request.form.get("lang", "English")
        return redirect(url_for(".stage_14"))

    return render_template("stage_13.tpl")


@ui.route("/new/14", methods=["GET", "POST"])
def stage_14():
    if request.method == "POST":
        session["county"] = request.form.get("county")
        return redirect(url_for(".stage_15"))

    return render_template("stage_14.tpl")


@ui.route("/new/15", methods=["GET", "POST"])
def stage_15():
    if request.method == "POST":
        session["city"] = request.form.get("city")
        return redirect(url_for(".stage_16"))

    return render_template("stage_15.tpl")


@ui.route("/new/16", methods=["GET", "POST"])
def stage_16():
    if request.method == "POST":
        session["location"] = request.form.get("community")
        return redirect(url_for(".stage_17"))

    return render_template("stage_16.tpl")


@ui.route("/new/17", methods=["GET", "POST"])
def stage_17():
    if request.method == "POST":
        is_ebola = request.form.get("is_ebola")
        if is_ebola == "Y":
            session["call_type"] = "New Case Report"
            return redirect(url_for(".new_case"))
        elif is_ebola == "N":
            return redirect(url_for(".stage_18"))

    return render_template("stage_17.tpl")


@ui.route("/new/18", methods=["GET", "POST"])
def stage_18():
    if request.method == "POST":
        cond = request.form.get("is_general")
        if cond == "Y":
            session["call_type"] = "General Inquiry"
            return redirect(url_for(".general_inquiry"))
        elif cond == "N":
            return redirect(url_for(".stage_19"))

    return render_template("stage_18.tpl")


@ui.route("/new/19", methods=["GET", "POST"])
def stage_19():
    if request.method == "POST":
        cond = request.form.get("about_patient")
        if cond == "Y":
            session["call_type"] = "About Patient"
            return redirect(url_for(".patient_info"))
        elif cond == "N":
            return redirect(url_for(".stage_20"))


    return render_template("stage_19.tpl")


@ui.route("/new/20", methods=["GET", "POST"])
def stage_20():
    if request.method == "POST":
        cond = request.form.get("new_info")
        if cond == "Y":
            session["call_type"] = "New Patient Info"
            return redirect(url_for(".new_patient_info"))
        elif cond == "N":
            return redirect(url_for(".stage_21"))


    return render_template("stage_20.tpl")

@ui.route("/new/21", methods=["GET", "POST"])
def stage_21():
    if request.method == "POST":
        save_session()
        return redirect(url_for(".index"))

    return render_template("stage_21.tpl")

@ui.route("/new/22", methods=["GET", "POST"])
def stage_22():
    if request.method == "POST":
        if "last" in session:
            return redirect(url_for(".stage_23"))

        else:
            session["last"] = True
            return redirect(url_for(".stage_11"))

    return render_template("stage_22.tpl")

@ui.route("/new/23", methods=["GET", "POST"])
def stage_23():
    if request.method == "POST":
        save_session()
        return redirect(url_for(".index"))

    return render_template("stage_23.tpl")

