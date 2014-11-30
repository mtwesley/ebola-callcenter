import datetime
import helpers
import pickle

from hashlib import sha256
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash
from flask.ext.login import current_user, login_user, logout_user, login_required

from models import db, User, Call, Case, CaseSymptom, Contact, Phone, phone_contacts


views = Blueprint("views", __name__)

@views.before_request
def default_globals():
    g.timestamp = datetime.datetime.now()
    g.user = current_user


@views.before_request
def default_session():
    session.setdefault('active', False)
    session.setdefault('step', 0)
    session.setdefault('call_id', 0)


@views.context_processor
def inject_helpers():
    return dict(helpers=helpers)


@views.route('/test')
def test():
    call = Call()
    contact = Contact()
    phone = Phone('0880358139')

    # return "hello"
    # db.session.add(contact)
    # return str(Case.query.join())

    if call:
        return 'YES'
    else:
        return "NO"

    # print call
    # print call.caller

    # call.caller = contact

    # return str(g.user.calls.exists())


@views.route("/", methods=['GET', 'POST'])
@views.route("/<default_step>", methods=['GET', 'POST'])
@login_required
def index(default_step=None):

    #FIXME: remove when development is complete
    print session
    print request.form

    agent_action = request.form.get('agent_action', '')
    agent_step = int(request.form.get('agent_step', 0))

    variables = {}
    step = session.get('step', 0)
    call = Call.query.get(session.get('call_id', 0))

    if agent_action == 'cancel':
        session.clear()
        default_session()

    elif agent_step == 0:
        if agent_action == 'submit':
            call = Call()
            call.timestamp = datetime.datetime.now()
            step = 1

    elif agent_step == 1:
        if agent_action == 'submit':
            caller_phone = request.form.get('caller_phone', None)
            call.phone = Phone.lookup_or_create(caller_phone)
            if call.phone.number:
                step = 2 if call.phone.contacts.exists() else 11

    elif agent_step == 2:
        if agent_action == 'submit':
            caller_id = request.form.get('caller_id', None)
            if caller_id:
                call.caller = Contact.query.get(caller_id)
                variables['cases'] = call.caller.cases.all()
                step = 3
            else:
                call.caller = Contact()
                step = 4

    elif agent_step == 3:
        if agent_action == 'submit':
            case_id = request.form.get('case_id', None)
            case = Case.query.get(case_id)
            if case:
                call.case = case
                step = 19
            else:
                step = 17

    elif agent_step == 4:
        if agent_action == 'submit':
            caller_phone = request.form.get('caller_phone', None)
            phone = Phone.lookup_or_create(caller_phone)
            if phone.number:
                call.caller.phones.append(phone)
                step = 5

    elif agent_step == 5:
        if agent_action == 'submit':
            first_name = request.form.get('caller_first_name', None)
            middle_name = request.form.get('caller_middle_name', None)
            last_name = request.form.get('caller_last_name', None)
            suffix = request.form.get('caller_suffix', None)
            if first_name and last_name:
                call.caller.first_name = first_name
                call.caller.middle_name = middle_name
                call.caller.last_name = last_name
                call.caller.suffix = suffix
                step = 6

    elif agent_step == 6:
        if agent_action == 'submit':
            sex = request.form.get('caller_sex', None)
            if sex:
                call.caller.sex = sex
                step = 7

    elif agent_step == 7:
        if agent_action == 'submit':
            language = request.form.get('caller_language', None)
            if language:
                call.caller.language = language
                step = 8

    elif agent_step == 8:
        if agent_action == 'submit':
            county = request.form.get('caller_county', None)
            if county:
                call.caller.county = county
                step = 9

    elif agent_step == 9:
        if agent_action == 'submit':
            city = request.form.get('caller_city', None)
            if city:
                call.caller.city
                step = 10

    elif agent_step == 10:
        if agent_action == 'submit':
            community = request.form.get('caller_community', None)
            if community:
                call.caller.community = community
                step = 3

    elif agent_step == 11:
        if agent_action == 'submit':
            first_name = request.form.get('caller_first_name', None)
            middle_name = request.form.get('caller_middle_name', None)
            last_name = request.form.get('caller_last_name', None)
            suffix = request.form.get('caller_suffix', None)
            if first_name and last_name:
                call.caller.first_name = first_name
                call.caller.middle_name = middle_name
                call.caller.last_name = last_name
                call.caller.suffix = suffix
                step = 12

    elif agent_step == 12:
        if agent_action == 'submit':
            sex = request.form.get('caller_sex', None)
            if sex:
                call.caller.sex = sex
                step = 13

    elif agent_step == 13:
        if agent_action == 'submit':
            language = request.form.get('caller_language', None)
            if language:
                call.caller.language = language
                step = 14

    elif agent_step == 14:
        if agent_action == 'submit':
            county = request.form.get('caller_county', None)
            if county:
                call.caller.county = county
                step = 15

    elif agent_step == 15:
        if agent_action == 'submit':
            city = request.form.get('caller_city', None)
            if city:
                call.caller.city
                step = 16

    elif agent_step == 16:
        if agent_action == 'submit':
            community = request.form.get('caller_community', None)
            if community:
                call.caller.community = community
                step = 17

    elif agent_step == 17:
        if agent_action == 'submit':
            case_report = request.form.get('case_report', None)
            if case_report == 'Y':
                step = 24
            elif case_report == 'N':
                step = 18

    elif agent_step == 18:
        if agent_action == 'submit':
            general_inquiry = request.form.get('general_inquiry', None)
            if general_inquiry == 'Y':
                step = 40
            elif general_inquiry == 'N':
                step = 19

    elif agent_step == 19:
        if agent_action == 'submit':
            case_inquiry = request.form.get('case_inquiry', None)
            if case_inquiry == 'Y':
                step = 42
            elif case_inquiry == 'N':
                step = 20

    elif agent_step == 20:
        if agent_action == 'submit':
            case_update = request.form.get('case_update', None)
            if case_update == 'Y':
                step = 47
            elif case_update == 'N':
                step = 22

    elif agent_step == 21:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 22:
        if agent_action == 'submit':
            step = 23

    elif agent_step == 23:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 24:
        if agent_action == 'submit':
            call.case = Case()
            call.case.timestamp = datetime.datetime.now()
            first_name = request.form.get('patient_first_name', None)
            middle_name = request.form.get('patient_middle_name', None)
            last_name = request.form.get('patient_last_name', None)
            suffix = request.form.get('patient_suffix', None)
            if first_name and last_name:
                call.case.patient = Contact()
                call.case.patient.first_name = first_name
                call.case.patient.middle_name = middle_name
                call.case.patient.last_name = last_name
                call.case.patient.suffix = suffix
                step = 25
        elif agent_action == 'skip':
            step = 25

    elif agent_step == 25:
        if agent_action == 'submit':
            patient_phone = request.form.get('patient_phone', None)
            phone = Phone.lookup_or_create(patient_phone)
            if phone.number:
                call.case.patient.phones.append(phone)
                if phone.cases().exists():
                    variables['cases'] = phone.cases().all()
                    step = 26
                else:
                    step = 27
        elif agent_action == 'skip':
            step = 27

    elif agent_step == 26:
        if agent_action == 'submit':
            case_id = request.form.get('case_id', None)
            case = Case.query.get(case_id)
            if case:
                call.case = case
                step = 39
            else:
                step = 27

    elif agent_step == 27:
        if agent_action == 'submit':
            sex = request.form.get('patient_sex', None)
            if sex:
                call.case.patient.sex = sex
                step = 28
        elif agent_action == 'skip':
            step = 28

    elif agent_step == 28:
        if agent_action == 'submit':
            age = request.form.get('patient_age', None)
            if age:
                call.case.patient.age = age
                step = 30
        elif agent_action == 'skip':
            step = 30

    elif agent_step == 29:
        if agent_action == 'submit':
            language = request.form.get('patient_language', None)
            if language:
                call.case.patient.language = language
                step = 30
        elif agent_action == 'skip':
            step = 30

    elif agent_step == 30:
        if agent_action == 'submit':
            county = request.form.get('patient_county', None)
            if county:
                call.case.patient.county = county
                step = 31
        elif agent_action == 'skip':
            step = 31

    elif agent_step == 31:
        if agent_action == 'submit':
            city = request.form.get('patient_city', None)
            if city:
                call.case.patient.city
                step = 32
        elif agent_action == 'skip':
            step = 32

    elif agent_step == 32:
        if agent_action == 'submit':
            community = request.form.get('patient_community', None)
            if community:
                call.case.patient.community = community
                step = 33
        elif agent_action == 'skip':
            step = 33

    elif agent_step == 33:
        if agent_action == 'submit':
            condition = request.form.get('patient_condition', None)
            if condition:
                call.case.patient.condition = condition
                step = 34
        elif agent_action == 'skip':
            step = 34

    elif agent_step == 34:
        if agent_action == 'submit':
            had_contact = request.form.get('patient_had_contact', None)
            if had_contact == 'Y':
                call.case.patient.had_contact = True
            elif had_contact == 'N':
                call.case.patient.had_contact = False
            step = 35
        elif agent_action == 'skip':
            step = 35

    elif agent_step == 35:
        if agent_action == 'submit':
            days_sick = request.form.get('patient_days_sick', None)
            if days_sick is not None:
                call.case.patient.days_sick = days_sick
                step = 36
        elif agent_action == 'skip':
            step = 36

    elif agent_step == 36:
        if agent_action == 'submit':
            symptoms = request.form.getlist('patient_symptoms')
            if symptoms:
                case_symptoms = []
                for s in symptoms:
                    case_symptoms.append(CaseSymptom(call.case, s))
                call.case.symptoms = case_symptoms
                step = 37
        elif agent_action == 'skip':
            step = 37

    elif agent_step == 37:
        if agent_action == 'submit':
            call.case.comments = request.form.get('caller_comments', '')
            step = 38
        if agent_action == 'skip':
            step = 38

    elif agent_step == 38:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 39:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 40:
        if agent_action == 'submit':
            call.case['caller_question'] = request.form.get('caller_question', '')
            step = 41

    elif agent_step == 41:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 42:
        if agent_action == 'submit':
            call.case = Case()
            call.case.timestamp = datetime.datetime.now()
            first_name = request.form.get('patient_first_name', None)
            middle_name = request.form.get('patient_middle_name', None)
            last_name = request.form.get('patient_last_name', None)
            suffix = request.form.get('patient_suffix', None)
            if first_name and last_name:
                call.case.patient = Contact()
                call.case.patient.first_name = first_name
                call.case.patient.middle_name = middle_name
                call.case.patient.last_name = last_name
                call.case.patient.suffix = suffix
                step = 43
        elif agent_action == 'skip':
            step = 43

    #TODO: handle situations with patient/caller name similarity check lookup

    elif agent_step == 43:
        if agent_action == 'submit':
            patient_phone = request.form.get('patient_phone', None)
            phone = Phone.lookup_or_create(patient_phone)
            if phone.number:
                call.case.patient.phones.append(phone)
                if phone.cases().exists():
                    variables['cases'] = phone.cases().all()
                    step = 44
                else:
                    step = 45
        elif agent_action == 'skip':
            step = 45

    #TODO: handle situations to lookup phone cases from the following step

    elif agent_step == 44:
        if agent_action == 'submit':
            case_id = request.form.get('case_id', None)
            case = Case.query.get(case_id)
            if case:
                call.case = case
                step = 46
            else:
                step = 45

    elif agent_step == 46:
        if agent_action == 'submit':
            session.clear()
            default_session()

    elif agent_step == 47:
        if agent_action == 'submit':
            call.case.patient.first_name = request.form.get('patient_first_name', call.case.patient.first_name or None)
            call.case.patient.middle_name = request.form.get('patient_middle_name', call.case.patient.middle_name or None)
            call.case.patient.last_name = request.form.get('patient_last_name', call.case.patient.last_name or None)
            call.case.patient.suffix = request.form.get('patient_suffix', call.case.patient.suffix or None)
            step = 48
        elif agent_action == 'skip':
            step = 48

    elif agent_step == 48:
        if agent_action == 'submit':
            call.case.patient.phone = request.form.get('patient_phone', call.case.patient.phone or None)
            step = 56
        elif agent_action == 'skip':
            step = 56

    elif agent_step == 56:
        if agent_action == 'submit':
            case_report = request.form.get('case_report', None)
            if case_report == 'Y':
                step = 24
            elif case_report == 'N':
                step = 57

    elif agent_step == 57:
        if agent_action == 'submit':
            session.clear()
            default_session()

    step = default_step or step
    dialog = 'steps/' + str(step or 0) + '.html'

    return render_template('dialog.html', dialog=dialog, step=step, call=call)


@views.route('/cancel')
@login_required
def cancel():
    session.clear()
    default_session()
    redirect(url_for('views.index'))


@views.route('/login', methods=['GET', 'POST'])
def login():
    user_action = request.form.get('agent_action', '')
    user_email = request.form.get('user_email', '')
    user_password = request.form.get('user_password', '')

    if g.user.is_authenticated():
        return redirect(url_for('views.index'))

    user = None
    if user_action == 'submit':
        try:
            session.clear()
            eml = user_email.lower()
            hsh = sha256(user_password).hexdigest()
            user = User.query.filter_by(email=eml, hash=hsh).one()

            if user is not None and login_user(user):
                return redirect(request.args.get('next') or url_for('home.index'))

        except NoResultFound:
            flash('Email and password do not match', 'error')

        except MultipleResultsFound:
            flash('Email and password do not match', 'error')

    return render_template('dialog.html', dialog='login.html')


@views.route("/logout")
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('views.index'))
