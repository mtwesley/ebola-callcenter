
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
            return redirect(url_for(".stage_1"))

    else:
        session.clear()

    return render_template("phone_no.tpl")

@ui.route("/new/1", methods=["GET", "POST"])
def stage_1():
    return ""


@ui.route("/new/2")
def stage_2():

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
            return redirect(url_for(".stage_24"))
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



@ui.route("/new/24", methods=["GET", "POST"])
def stage_24():
    if request.method == "POST":
        f = request.form

        session["p_first_name"] = f["p_name_first"]
        session["p_middle_name"] = f["p_name_middle"]
        session["p_last_name"] = f["p_name_last"]
        session["p_suffix_name"] = f["p_suffix"].lower().replace("none", "")
        session["p_name"] = "%(p_name_first)s %(p_name_middle)s %(p_name_last)s" % f

        return redirect(url_for(".stage_25"))

    return render_template("stage_24.tpl")

@ui.route("/new/25", methods=["GET", "POST"])
def stage_25():
    if request.method == "POST":
        session["p_msisdn"] = request.form["p_msisdn"]
        P = Phone.query.filter(Phone.msisdn == session["p_msisdn"]).first()
        if P is None:
            return redirect(url_for(".stage_27"))

        session["tmp_p_name"] = "LOOKUP_PATIENT_NAME_FROM_DB"
        session["tmp_p_location"] = "LOOKUP_PATIENT_LOC_FROM_DB"
        return redirect(url_for(".stage_26"))

    return render_template("stage_25.tpl")

@ui.route("/new/26", methods=["GET", "POST"])
def stage_26():
    pass

@ui.route("/new/27", methods=["GET", "POST"])
def stage_27():
    if request.method == "POST":
        cond = request.form.get("p_sex")
        if cond == "M" or cond == "F":
            session["p_sex"] = cond
            return redirect(url_for(".stage_28"))

    return render_template("stage_27.tpl")

@ui.route("/new/28", methods=["GET", "POST"])
def stage_28():
    if request.method == "POST":
        session["p_age"] = request.form["p_age"]
        return redirect(url_for(".stage_29"))

    return render_template("stage_28.tpl")


@ui.route("/new/29", methods=["GET", "POST"])
def stage_29():
    if request.method == "POST":
        session["p_lang"] = request.form.get("p_lang", "English")
        return redirect(url_for(".stage_30"))

    return render_template("stage_29.tpl")

@ui.route("/new/30", methods=["GET", "POST"])
def stage_30():
    if request.method == "POST":
        session["p_county"] = request.form["county"]
        return redirect(url_for(".stage_31"))

    return render_template("stage_30.tpl")


@ui.route("/new/31", methods=["GET", "POST"])
def stage_31():
    if request.method == "POST":
        session["p_city"] = request.form["city"]
        return redirect(url_for(".stage_32"))

    return render_template("stage_31.tpl")


@ui.route("/new/32", methods=["GET", "POST"])
def stage_32():
    if request.method == "POST":
        session["p_location"] = request.form["location"]
        return redirect(url_for(".stage_33"))

    return render_template("stage_32.tpl")


@ui.route("/new/33", methods=["GET", "POST"])
def stage_33():
    if request.method == "POST":
        session["p_status"] = request.form["p_status"]
        return redirect(url_for(".stage_34"))

    return render_template("stage_33.tpl")


@ui.route("/new/34", methods=["GET", "POST"])
def stage_34():
    if request.method == "POST":
        session["p_ebola_contact"] = request.form["ebola_contact"]
        return redirect(url_for(".stage_35"))

    return render_template("stage_34.tpl")


@ui.route("/new/35", methods=["GET", "POST"])
def stage_35():
    if request.method == "POST":
        session["p_sick_days"] = request.form["p_sick_days"]
        return redirect(url_for(".stage_36"))

    return render_template("stage_35.tpl")

@ui.route("/new/36", methods=["GET", "POST"])
def stage_36():
    if request.method == "POST":
        session["p_symptoms"] = request.form["symptoms"]
        print request.form
        return redirect(url_for(".stage_37"))

    return render_template("stage_36.tpl")


@ui.route("/new/37", methods=["GET", "POST"])
def stage_37():
    if request.method == "POST":
        session["p_comment"] = request.form["comment"]
        return redirect(url_for(".stage_38"))

    return render_template("stage_37.tpl")


@ui.route("/new/38", methods=["GET", "POST"])
def stage_38():
    if request.method == "POST":
        save_session()
        return redirect(url_for(".index"))

    return render_template("stage_38.tpl")


@ui.route("/new/39", methods=["GET", "POST"])
def stage_39():
    if request.method == "POST":
        session.clear()
        return redirect(url_for(".index"))

    return render_template("stage_39.tpl")


@ui.route("/new/40", methods=["GET", "POST"])
def stage_40():
    if request.method == "POST":
        print request.form
        return redirect(url_for(".stage_41"))

    return render_template("stage_40.tpl")


@ui.route("/new/41", methods=["GET", "POST"])
def stage_41():
    if request.method == "POST":
        session.clear()
        return redirect(url_for(".index"))

    return render_template("stage_41.tpl")
