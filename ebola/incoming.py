import datetime
import helpers

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash, abort
from flask.ext.login import current_user, login_user, logout_user, login_required

from models import db, User, Complaint, ComplaintStatus


view = Blueprint('incoming', __name__, url_prefix='/incoming')


def clean_session():
    session['active'] = False
    session['deactivate'] = False
    session['step'] = 1
    session['steps'] = []
    session['previous_step'] = 0
    session['complaint_id'] = 0


@view.before_request
def check_agent():
    if not (g.user.is_authenticated() and g.user.is_agent):
        logout_user()
        response = redirect(url_for('home.login'))
        abort(response)


@view.before_request
def default_session():
    session.setdefault('active', False)
    session.setdefault('deactivate', False)
    session.setdefault('step', 1)
    session.setdefault('steps', [])
    session.setdefault('previous_step', 0)
    session.setdefault('complaint_id', 0)

@view.route("/refresh")
def refresh():
    # db.drop_all()
    # db.create_all()
    return "Nothing"


@view.route("/", methods=['GET', 'POST'])
@view.route("/<default_step>", methods=['GET', 'POST'])
@login_required
def index(default_step=None):
    vars = {}

    step = session.get('step', 1)
    previous_step = session.get('previous_step', 0)

    complaint = Complaint.query.get(session.get('complaint_id', 0)) or Complaint()

    agent_action = request.form.get('agent_action', '')
    agent_step = int(request.form.get('agent_step', step))

    if agent_step == 0:
        if agent_action == 'submit':
            complaint = Complaint()
            complaint.timestamp = datetime.datetime.now()
            step = 1
            session['active'] = True
        else:
            step = agent_step

    elif agent_step == 1:
        if agent_action == 'submit':
            complaint = Complaint()
            complaint.timestamp = datetime.datetime.now()
            step = 2
            session['active'] = True
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 2:
        if agent_action == 'submit':
            phone = helpers.e164_phone_number(request.form.get('phone', None))
            if phone:
                complaint.phone = phone
                step = 3
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 3:
        if agent_action == 'submit':
            name = request.form.get('name', None)
            if name:
                complaint.name = name
                step = 4
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 4:
        if agent_action == 'submit':
            county = request.form.get('county', None)
            if county:
                complaint.county = county
                step = 5
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 5:
        if agent_action == 'submit':
            district = request.form.get('district', None)
            if district:
                complaint.district = district
                step = 6
            else:
                step = agent_step
        elif agent_action == 'skip':
            step = 6
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 6:
        if agent_action == 'submit':
            city = request.form.get('city', None)
            if city:
                complaint.city = city
                step = 7
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 7:
        if agent_action == 'submit':
            address = request.form.get('address', None)
            if address:
                complaint.address = address
                step = 8
            else:
                step = agent_step
        elif agent_action == 'skip':
            step = 8
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 8:
        if agent_action == 'submit':
            is_moh = request.form.get('is_moh', None)
            if is_moh == 'Y':
                complaint.is_moh = True
                step = 9
            elif is_moh == 'N':
                complaint.is_moh = False
                step = 9
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 9:
        if agent_action == 'submit':
            is_erw = request.form.get('is_erw', None)
            if is_erw == 'Y':
                complaint.is_erw = True
                step = 10
            elif is_erw == 'N':
                complaint.is_erw = False
                step = 10
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 10:
        if agent_action == 'submit':
            organization = request.form.get('organization', None)
            if organization:
                complaint.organization = organization
                step = 11
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 11:
        if agent_action == 'submit':
            organization_type = request.form.get('organization_type', None)
            if organization_type in helpers.organization_type.keys():
                complaint.organization_type = organization_type
                if organization_type == 'other':
                    step = 12
                else:
                    step = 13
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 12:
        if agent_action == 'submit':
            other_organization_type = request.form.get('other_organization_type', None)
            if other_organization_type:
                complaint.other_organization_type = other_organization_type
                step = 11
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 13:
        if agent_action == 'submit':
            position = request.form.get('position', None)
            if position:
                complaint.position = position
                step = 14
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 14:
        if agent_action == 'submit':
            salary = request.form.get('salary', None)
            if salary == 'Y':
                complaint.payment_type = 'salary'
                step = 19
            elif salary == 'N':
                step = 15
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 15:
        if agent_action == 'submit':
            hazard = request.form.get('hazard', None)
            if hazard == 'Y':
                complaint.payment_type = 'hazard'
                step = 19
            elif hazard == 'N':
                step = 16
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 16:
        if agent_action == 'submit':
            allowance = request.form.get('allowance', None)
            if allowance == 'Y':
                complaint.payment_type = 'allowance'
                step = 19
            elif allowance == 'N':
                step = 17
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

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
        else:
            step = agent_step

    elif agent_step == 18:
        if agent_action == 'submit':
            payment_type = request.form.get('payment_type', None)
            if payment_type:
                complaint.payment_type = payment_type
                step = 19
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 19:
        if agent_action == 'submit':
            not_paid = request.form.get('not_paid', None)
            if not_paid == 'N':
                complaint.payment_issue = 'not_paid'
                step = 22
            elif not_paid == 'Y':
                step = 20
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 20:
        if agent_action == 'submit':
            delayed = request.form.get('delayed', None)
            if delayed == 'Y':
                complaint.payment_issue = 'delayed'
                step = 22
            elif delayed == 'N':
                step = 21
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 21:
        if agent_action == 'submit':
            incorrect = request.form.get('incorrect', None)
            if incorrect == 'Y':
                complaint.payment_issue = 'incorrect'
                step = 22
            elif incorrect == 'N':
                complaint.payment_issue = 'other'
                step = 22
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 22:
        if agent_action == 'submit':
            complaint_description = request.form.get('complaint_description', None)
            if complaint_description:
                complaint.complaint_description = complaint_description
                step = 23
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 23:
        if agent_action == 'submit':
            complaint_resolution = request.form.get('complaint_resolution', None)
            if complaint_resolution:
                complaint.complaint_resolution = complaint_resolution
                step = 24
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 24:
        if agent_action == 'submit':
            status = complaint.status('open')
            db.session.add(status)
            db.session.commit()
            session['deactivate'] = True
        else:
            step = agent_step

    elif agent_step == 98:
        if agent_action == 'submit':
            step = previous_step
        elif agent_action == 'cancel':
            step = 99
        else:
            step = agent_step

    elif agent_step == 99:
        if agent_action == 'submit':
            reason = request.form.get('reason', '')
            status = complaint.status('deleted', reason)
            db.session.add(status)
            db.session.commit()
            session['deactivate'] = True
        else:
            step = agent_step

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
        step = 1
        default_session()
        session['active'] = False
        return cancel()

    # FIXME: remove when development is complete
    print "\n\nSESSION: ", session, "\n\n"
    print "\n\nREQUEST: ", request.form, "\n\n"
    if complaint:
        print "\n\nSTATUS: ", complaint.status(), "\n\n"

    step = default_step or step
    dialog = 'incoming/' + str(step or 1) + '.html'

    if complaint.phone:
        vars['all_complaints'] = Complaint.query.join(ComplaintStatus).filter(
            Complaint.phone == complaint.phone,
            Complaint.response_date == None,
            ComplaintStatus.status == 'open')

        vars['all_resolutions'] = Complaint.query.join(ComplaintStatus).filter(
            Complaint.phone == complaint.phone,
            Complaint.response_date != None,
            ComplaintStatus.status == 'resolved')

        vars['total_calls'] = Complaint.query.filter(Complaint.phone == complaint.phone).count()
        vars['total_calls_today'] = Complaint.query.filter(
            Complaint.phone == complaint.phone,
            Complaint.timestamp.between(datetime.date.today(), datetime.datetime.now())).count()
    else:
        vars['all_complaints'] = None
        vars['all_resolutions'] = None
        vars['total_calls'] = None
        vars['total_calls_today'] = None

    return render_template('dialog.html', dialog=dialog, step=step, complaint=complaint, vars=vars)


@view.route('/new')
@login_required
def new():
    default_session()
    clean_session()

    from_complaint = Complaint.query.get(request.args.get('from_complaint_id', 0))
    if from_complaint:
        clean_session()
        complaint = Complaint()
        complaint.timestamp = datetime.datetime.now()

        complaint.phone = from_complaint.phone
        complaint.name = from_complaint.name

        complaint.organization = from_complaint.organization
        complaint.organization_type = from_complaint.organization_type
        complaint.other_organization_type = from_complaint.other_organization_type
        complaint.position = from_complaint.position

        complaint.county = from_complaint.county
        complaint.district = from_complaint.district
        complaint.city = from_complaint.city
        complaint.address = from_complaint.address

        complaint.is_erw = from_complaint.is_erw
        complaint.is_moh = from_complaint.is_moh
        db.session.add(complaint)
        db.session.commit()

        session['active'] = True
        session['step'] = 14
        session['complaint_id'] = complaint.id

    return redirect(url_for('incoming.index'))

@view.route('/cancel')
@login_required
def cancel():
    default_session()
    clean_session()
    return redirect(url_for('home.index'))


