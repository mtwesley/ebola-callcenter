import datetime
import helpers

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash
from flask.ext.login import current_user, login_user, logout_user, login_required

from models import db, User, Complaint, ComplaintStatus


view = Blueprint('outgoing', __name__, url_prefix='/outgoing')


def clean_session():
    session['active'] = False
    session['deactivate'] = False
    session['step'] = 1
    session['steps'] = []
    session['previous_step'] = 0
    session['complaint_id'] = 0


@view.before_request
def default_session():
    session.setdefault('active', False)
    session.setdefault('deactivate', False)
    session.setdefault('step', 1)
    session.setdefault('steps', [])
    session.setdefault('previous_step', 0)
    session.setdefault('complaint_id', 0)


@view.route("/", methods=['GET', 'POST'])
@view.route("/<default_step>", methods=['GET', 'POST'])
@login_required
def index(default_step=None):
    vars = {}

    step = session.get('step', 1)
    previous_step = session.get('previous_step', 0)

    agent_action = request.form.get('agent_action', '')
    agent_step = int(request.form.get('agent_step', step))

    complaint_id = session.get('complaint_id', 0)
    if not complaint_id:
        complaint_id = request.args.get('complaint_id', 0)

    complaint = Complaint.query.get(complaint_id)

    if not complaint:
        return redirect(url_for('home.index'))

    if agent_step == 0:
        if agent_action == 'submit':
            step = 1
            session['active'] = True
        else:
            step = agent_step

    elif agent_step == 1:
        if agent_action == 'submit':
            step = 2
            session['active'] = True
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 2:
        if agent_action == 'submit':
            is_complainant = request.form.get('is_complainant', None)
            if is_complainant == 'Y':
                step = 5
            elif is_complainant == 'N':
                step = 3
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 3:
        if agent_action == 'submit':
            is_complainant_available = request.form.get('is_complainant_available', None)
            if is_complainant_available == 'Y':
                step = 5
            elif is_complainant_available == 'N':
                step = 4
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 4:
        if agent_action == 'submit':
            status = complaint.status('closed')
            db.session.add(status)
            session['deactivate'] = True
        else:
            step = agent_step

    elif agent_step == 5:
        if agent_action == 'submit':
            step = 6
        else:
            step = agent_step

    elif agent_step == 6:
        if agent_action == 'submit':
            step = 7
        else:
            step = agent_step

    elif agent_step == 7:
        if agent_action == 'submit':
            is_satisfied = request.form.get('is_satisfied', None)
            if is_satisfied == 'Y':
                complaint.is_satisfied = True
                step = 9
            elif is_satisfied == 'N':
                complaint.is_satisfied = False
                step = 8
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 8:
        if agent_action == 'submit':
            new_complaint = request.form.get('new_complaint', None)
            if new_complaint == 'Y':
                return redirect(url_for('incoming.new', from_complaint_id=complaint.id))
            elif new_complaint == 'N':
                step = 9
            else:
                step = agent_step
        elif agent_action == 'cancel':
            step = 98
        else:
            step = agent_step

    elif agent_step == 9:
        if agent_action == 'submit':
            status = complaint.status('closed')
            db.session.add(status)
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
            # reason = request.form.get('reason', '')
            # status = complaint.status('deleted', reason)
            # db.session.add(status)
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
    dialog = 'outgoing/' + str(step or 1) + '.html'

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
    return redirect(url_for('outgoing.index', complaint_id=request.args.get('complaint_id', 0)))


@view.route('/cancel')
@login_required
def cancel():
    default_session()
    clean_session()
    return redirect(url_for('home.index'))


