from flask import Blueprint, render_template, request, session, redirect, url_for, g

from models import User


views = Blueprint("views", __name__)


@views.before_request
def session_defaults():
    session.setdefault('step', 0)
    session.setdefault('call', {})
    session.setdefault('case', {})

@views.route("/", methods=['GET', 'POST'])
@views.route("/<default_step>", methods=['GET', 'POST'])
def index(default_step=0):

    print session
    print request.form

    agent_action = request.form.get('agent_action', '')
    agent_step = int(request.form.get('agent_step', default_step))

    # if not 'step' in session:
    #     session['step'] = 0
    #
    # if not 'call' in session:
    #     session['call'] = {}
    #
    # if not 'case' in session:
    #     session['case'] = {}

    if agent_action == 'cancel':
        session.clear()
        session_defaults()

    elif agent_step == 0:
        if agent_action == 'submit':
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
                session['step'] = 21




    step = session['step']
    call = session['call']
    case = session['case']

    return render_template('layout.html', step=step, call=call, case=case)


@views.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('views.index'))
