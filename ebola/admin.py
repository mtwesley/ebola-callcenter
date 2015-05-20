
from hashlib import sha256
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash, abort
from flask.ext.login import current_user, login_user, logout_user, login_required
from sqlalchemy import func

from models import db, User, Complaint,ComplaintStatus


view = Blueprint('admin', __name__)


@view.route("/admin")
@login_required
def index():
    return render_template('admin.html')


@view.before_request
def check_admin():
    if not (g.user.is_authenticated() and g.user.is_admin):
        logout_user()
        response = redirect(url_for('home.login'))
        abort(response)


@view.route("/search/", methods=['GET', 'POST'])
@view.route("/search/<status>", methods=['GET', 'POST'])
def search(status=None):
    subquery = (db.session.query(ComplaintStatus.complaint_id,
                                 func.max(ComplaintStatus.timestamp).label('latest_timestamp'))
                .group_by(ComplaintStatus.complaint_id)
                .subquery())
    if status:

        complaints = db.session.query(Complaint).filter(
            Complaint.id == ComplaintStatus.complaint_id,
            Complaint.id == subquery.columns.complaint_id,
            ComplaintStatus.status == status,
            ComplaintStatus.timestamp == subquery.columns.latest_timestamp
        ).order_by(subquery.columns.latest_timestamp.desc()).limit(12)

    else:
        complaints = db.session.query(Complaint).filter(
            Complaint.id == ComplaintStatus.complaint_id,
            Complaint.id == subquery.columns.complaint_id,
            ComplaintStatus.status != 'pending',
            ComplaintStatus.timestamp == subquery.columns.latest_timestamp
        ).order_by(subquery.columns.latest_timestamp.desc()).limit(12)

    return render_template('search.html', status=status, complaints=complaints)


@view.route("/complaint/<complaint_id>", methods=['GET', 'POST'])
@login_required
def complaint(complaint_id=None):
    complaint = Complaint.query.get(complaint_id)

    admin_action = request.form.get('admin_action', '')

    if admin_action == 'submit':
        response_description = request.form.get('response_description', None)
        if response_description:
            complaint.response_description = response_description
            status = complaint.status('resolved')
            db.session.add(complaint)
            db.session.add(status)
            db.session.commit()
            return redirect(url_for('admin.search', status=str(complaint.status())))

    return render_template('complaint.html', complaint=complaint)


