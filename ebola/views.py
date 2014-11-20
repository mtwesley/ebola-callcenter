import datetime

from flask import Blueprint, render_template, request, session, redirect, url_for, g

from models import User


views = Blueprint("views", __name__)

@views.before_request
def default_timestamp():
    g.timestamp = datetime.datetime.now()


@views.before_request
def default_session():
    session.setdefault('active', False)
    session.setdefault('step', 0)
    session.setdefault('call', {})
    session.setdefault('case', {})


@views.route("/", methods=['GET', 'POST'])
@views.route("/<default_step>", methods=['GET', 'POST'])
def index(default_step=None):

    print session
    print request.form

    agent_action = request.form.get('agent_action', '')
    agent_step = int(request.form.get('agent_step', 0))

    if agent_action == 'cancel':
        session.clear()
        default_session()

    elif agent_step == 0:
        if agent_action == 'submit':
            session['active'] = True
            session['step'] = 1

    elif agent_step == 1:
        if agent_action == 'submit':
            session['call']['caller_phone'] = request.form.get('caller_phone', '')
            session['step'] = 11

    elif agent_step == 11:
        if agent_action == 'submit':
            session['call']['caller_first_name'] = request.form.get('caller_first_name', '')
            session['call']['caller_middle_name'] = request.form.get('caller_middle_name', '')
            session['call']['caller_last_name'] = request.form.get('caller_last_name', '')
            session['call']['caller_suffix'] = request.form.get('caller_suffix', '')
            session['step'] = 12

    elif agent_step == 12:
        if agent_action == 'submit':
            session['call']['caller_sex'] = request.form.get('caller_sex', '')
            session['step'] = 13

    elif agent_step == 13:
        if agent_action == 'submit':
            session['call']['caller_language'] = request.form.get('caller_language', '')
            session['step'] = 14

    elif agent_step == 14:
        if agent_action == 'submit':
            session['call']['caller_county'] = request.form.get('caller_county', '')
            session['step'] = 15

    elif agent_step == 15:
        if agent_action == 'submit':
            session['call']['caller_city'] = request.form.get('caller_city', '')
            session['step'] = 16

    elif agent_step == 16:
        if agent_action == 'submit':
            session['call']['caller_community'] = request.form.get('caller_community', '')
            session['step'] = 17

    elif agent_step == 17:
        if agent_action == 'submit':
            case_report = request.form.get('case_report', '')
            if case_report == 'Y':
                session['step'] = 24
            elif case_report == 'N':
                session['step'] = 18

    elif agent_step == 18:
        if agent_action == 'submit':
            general_inquiry = request.form.get('general_inquiry', '')
            if general_inquiry == 'Y':
                session['step'] = 40
            elif general_inquiry == 'N':
                session['step'] = 19

    elif agent_step == 19:
        if agent_action == 'submit':
            case_inquiry = request.form.get('case_inquiry', '')
            if case_inquiry == 'Y':
                session['step'] = 42
            elif case_inquiry == 'N':
                session['step'] = 20

    elif agent_step == 20:
        if agent_action == 'submit':
            case_update = request.form.get('case_update', '')
            if case_update == 'Y':
                session['step'] = 47
            elif case_update == 'N':
                session['step'] = 22

    elif agent_step == 22:
        if agent_action == 'submit':
            session['step'] = 23

    elif agent_step == 23:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 24:
        if agent_action == 'submit':
            session['case']['patient_first_name'] = request.form.get('patient_first_name', '')
            session['case']['patient_middle_name'] = request.form.get('patient_middle_name', '')
            session['case']['patient_last_name'] = request.form.get('patient_last_name', '')
            session['case']['patient_suffix'] = request.form.get('patient_suffix', '')
            session['step'] = 25
        if agent_action == 'skip':
            session['step'] = 25

    elif agent_step == 25:
        if agent_action == 'submit':
            session['case']['patient_phone'] = request.form.get('patient_phone', '')
            session['step'] = 27
        if agent_action == 'skip':
            session['step'] = 27

    elif agent_step == 27:
        if agent_action == 'submit':
            session['case']['patient_sex'] = request.form.get('patient_sex', '')
            session['step'] = 28
        if agent_action == 'skip':
            session['step'] = 28

    elif agent_step == 28:
        if agent_action == 'submit':
            session['case']['patient_age'] = request.form.get('patient_age', '')
            session['step'] = 29
        if agent_action == 'skip':
            session['step'] = 29

    elif agent_step == 29:
        if agent_action == 'submit':
            session['case']['patient_language'] = request.form.get('patient_language', '')
            session['step'] = 30
        if agent_action == 'skip':
            session['step'] = 30

    elif agent_step == 30:
        if agent_action == 'submit':
            session['case']['patient_county'] = request.form.get('patient_county', '')
            session['step'] = 31
        if agent_action == 'skip':
            session['step'] = 31

    elif agent_step == 31:
        if agent_action == 'submit':
            session['case']['patient_city'] = request.form.get('patient_city', '')
            session['step'] = 32
        if agent_action == 'skip':
            session['step'] = 32

    elif agent_step == 32:
        if agent_action == 'submit':
            session['case']['patient_community'] = request.form.get('patient_community', '')
            session['step'] = 33
        if agent_action == 'skip':
            session['step'] = 33

    elif agent_step == 33:
        if agent_action == 'submit':
            session['case']['patient_conscious'] = request.form.get('patient_conscious', '')
            session['step'] = 34
        if agent_action == 'skip':
            session['step'] = 34

    elif agent_step == 34:
        if agent_action == 'submit':
            session['case']['patient_had_contact'] = request.form.get('patient_had_contact', '')
            session['step'] = 35
        if agent_action == 'skip':
            session['step'] = 35

    elif agent_step == 35:
        if agent_action == 'submit':
            session['case']['patient_days_sick'] = request.form.get('patient_days_sick', '')
            session['step'] = 36
        if agent_action == 'skip':
            session['step'] = 36

    elif agent_step == 36:
        if agent_action == 'submit':
            session['case']['patient_symptoms'] = ', '.join(request.form.getlist('patient_symptoms'))
            session['step'] = 37
        if agent_action == 'skip':
            session['step'] = 37

    elif agent_step == 37:
        if agent_action == 'submit':
            session['case']['caller_comments'] = request.form.get('caller_comments', '')
            session['step'] = 38

    elif agent_step == 38:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 40:
        if agent_action == 'submit':
            session['case']['caller_question'] = request.form.get('caller_question', '')
            session['step'] = 41

    elif agent_step == 41:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 42:
        if agent_action == 'submit':
            session['case']['patient_first_name'] = request.form.get('patient_first_name', '')
            session['case']['patient_middle_name'] = request.form.get('patient_middle_name', '')
            session['case']['patient_last_name'] = request.form.get('patient_last_name', '')
            session['case']['patient_suffix'] = request.form.get('patient_suffix', '')
            session['step'] = 43
        if agent_action == 'skip':
            session['step'] = 43

    elif agent_step == 43:
        if agent_action == 'submit':
            session['case']['patient_phone'] = request.form.get('patient_phone', '')
            session['step'] = 45
        if agent_action == 'skip':
            session['step'] = 45

    elif agent_step == 46:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 47:
        if agent_action == 'submit':
            session['case']['patient_first_name'] = request.form.get('patient_first_name', '')
            session['case']['patient_middle_name'] = request.form.get('patient_middle_name', '')
            session['case']['patient_last_name'] = request.form.get('patient_last_name', '')
            session['case']['patient_suffix'] = request.form.get('patient_suffix', '')
            session['step'] = 48
        if agent_action == 'skip':
            session['step'] = 48

    elif agent_step == 48:
        if agent_action == 'submit':
            session['case']['patient_phone'] = request.form.get('patient_phone', '')
            session['step'] = 56
        if agent_action == 'skip':
            session['step'] = 56

    elif agent_step == 56:
        if agent_action == 'submit':
            case_report = request.form.get('case_report', '')
            if case_report == 'Y':
                session['step'] = 24
            elif case_report == 'N':
                session['step'] = 57

    elif agent_step == 57:
        if agent_action == 'submit':
            session.clear()
            default_session()

    return render_template('layout.html',
                           step=default_step or session['step'],
                           call=session['call'],
                           case=session['case'])


@views.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('views.index'))
