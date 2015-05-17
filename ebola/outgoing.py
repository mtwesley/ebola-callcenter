import datetime
import helpers

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash
from flask.ext.login import current_user, login_user, logout_user, login_required

from models import db, User, Complaint


view = Blueprint('incoming', __name__, url_prefix='/incoming')


@view.before_request
def default_session():
    session.setdefault('active', False)
    session.setdefault('deactivate', False)
    session.setdefault('step', 0)
    session.setdefault('steps', [])
    session.setdefault('previous_step', 0)
    session.setdefault('complaint_id', 0)


@view.context_processor
def inject_helpers():
    return dict(helpers=helpers)


@view.route("/refresh")
def refresh():
    # db.drop_all()
    # db.create_all()
    return "Nothing"


@view.route("/", methods=['GET', 'POST'])
@view.route("/<default_step>", methods=['GET', 'POST'])
@login_required
def index(default_step=None):
    agent_action = request.form.get('agent_action', '')
    agent_step = int(request.form.get('agent_step', 0))

    vars = {}
    step = session.get('step', 0)
    previous_step = session.get('previous_step', 0)
    complaint = Complaint.query.get(session.get('complaint_id', 0)) or Complaint()

    if agent_step == 0:
        if agent_action == 'submit':
            complaint = Complaint()
            complaint.timestamp = datetime.datetime.now()
            step = 1
            session['active'] = True

    elif agent_step == 1:
        if agent_action == 'submit':
            step = 2
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 2:
        if agent_action == 'submit':
            phone = request.form.get('phone', None)
            if phone:
                complaint.phone = helpers.e164_phone_number(phone)
                step = 3
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 3:
        if agent_action == 'submit':
            name = request.form.get('name', None)
            if name:
                complaint.name = name
                step = 4
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 4:
        if agent_action == 'submit':
            county = request.form.get('county', None)
            if county:
                complaint.county = county
                step = 5
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 5:
        if agent_action == 'submit':
            district = request.form.get('district', None)
            if district:
                complaint.district = district
                step = 6
        elif agent_action == 'skip':
            step = 6
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 6:
        if agent_action == 'submit':
            city = request.form.get('city', None)
            if city:
                complaint.city = city
                step = 7
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 7:
        if agent_action == 'submit':
            address = request.form.get('address', None)
            if address:
                complaint.address = address
                step = 8
        elif agent_action == 'skip':
            step = 8
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 8:
        if agent_action == 'submit':
            is_moh = request.form.get('is_moh', None)
            if is_moh == 'Y':
                complaint.is_moh = True
                step = 9
            elif is_moh == 'N':
                complaint.is_moh = False
                step = 9
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 9:
        if agent_action == 'submit':
            is_erw = request.form.get('is_erw', None)
            if is_erw == 'Y':
                complaint.is_erw = True
                step = 10
            elif is_erw == 'N':
                complaint.is_erw = False
                step = 10
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 10:
        if agent_action == 'submit':
            organization = request.form.get('organization', None)
            if organization:
                complaint.organization = organization
                step = 11
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 11:
        if agent_action == 'submit':
            organization_type = request.form.get('organization_type', None)
            if organization_type in helpers.organization_type.keys():
                complaint.organization_type = organization_type
                if organization_type == 'other':
                    step = 12
                else:
                    step = 13
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 12:
        if agent_action == 'submit':
            other_organization_type = request.form.get('other_organization_type', None)
            if other_organization_type:
                complaint.other_organization_type = other_organization_type
                step = 11
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 13:
        if agent_action == 'submit':
            position = request.form.get('position', None)
            if position:
                complaint.position = position
                step = 14
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 14:
        if agent_action == 'submit':
            salary = request.form.get('salary', None)
            if salary == 'Y':
                complaint.payment_type = 'salary'
                step = 19
            elif salary == 'N':
                step = 15
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 15:
        if agent_action == 'submit':
            hazard = request.form.get('hazard', None)
            if hazard == 'Y':
                complaint.payment_type = 'hazard'
                step = 19
            elif hazard == 'N':
                step = 16
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 16:
        if agent_action == 'submit':
            allowance = request.form.get('allowance', None)
            if allowance == 'Y':
                complaint.payment_type = 'allowance'
                step = 19
            elif allowance == 'N':
                step = 17
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 17:
        if agent_action == 'submit':
            response = request.form.get('response', None)
            if response == 'Y':
                complaint.payment_type = 'response'
                step = 19
            elif response == 'N':
                step = 18
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 18:
        if agent_action == 'submit':
            payment_type = request.form.get('payment_type', None)
            if payment_type:
                complaint.payment_type = payment_type
                step = 19
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 19:
        if agent_action == 'submit':
            not_paid = request.form.get('not_paid', None)
            if not_paid == 'Y':
                complaint.payment_issue = 'not_paid'
                step = 22
            elif not_paid == 'N':
                step = 20
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 20:
        if agent_action == 'submit':
            delayed = request.form.get('delayed', None)
            if delayed == 'Y':
                complaint.payment_issue = 'delayed'
                step = 22
            elif delayed == 'N':
                step = 21
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 21:
        if agent_action == 'submit':
            incorrect = request.form.get('incorrect', None)
            if incorrect == 'Y':
                complaint.payment_issue = 'incorrect'
                step = 22
            elif incorrect == 'N':
                complaint.payment_issue = 'other'
                step = 22
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 22:
        if agent_action == 'submit':
            complaint_description = request.form.get('complaint_description', None)
            if complaint_description:
                complaint.organization = complaint_description
                step = 23
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 23:
        if agent_action == 'submit':
            complaint_resolution = request.form.get('complaint_resolution', None)
            if complaint_resolution:
                complaint.organization = complaint_resolution
                step = 24
        elif agent_action == 'cancel':
            step = 98

    elif agent_step == 24:
        if agent_action == 'submit':
            status = complaint.status('open')
            db.session.add(status)
            db.session.commit()
            session['deactivate'] = True

    elif agent_step == 98:
        if agent_action == 'submit':
            step = previous_step
        elif agent_action == 'cancel':
            step = 99

    elif agent_step == 99:
        if agent_action == 'submit':
            reason = request.form.get('reason', '')
            status = complaint.status('deleted', reason)
            db.session.add(status)
            session['deactivate'] = True

    #TODO: implement step stack for easy back and forth movement instead of only "previous_step"
    session['step'] = step
    session['previous_step'] = agent_step

    if session.get('active', False):
        if complaint:
            db.session.add(complaint)
        else:
            complaint = Complaint()

        if not complaint.status():
            status = complaint.status('pending')
            db.session.add(status)
        db.session.commit()
        session['complaint_id'] = complaint.id

    if session.get('deactivate', False):
        step = 0
        default_session()
        session['active'] = False

    # FIXME: remove when development is complete
    print "\n\nSESSION: ", session, "\n\n"
    print "\n\nREQUEST: ", request.form, "\n\n"
    if complaint:
        print "\n\nSTATUS: ", complaint.status(), "\n\n"

    step = default_step or step
    dialog = 'incoming/' + str(step or 0) + '.html'

    return render_template('dialog.html', dialog=dialog, step=step, complaint=complaint, vars=vars)


@view.route('/cancel')
@login_required
def cancel():
    default_session()
    return redirect(url_for('incoming.index'))


