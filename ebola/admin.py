
from hashlib import sha256
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash
from flask.ext.login import current_user, login_user, logout_user, login_required
from sqlalchemy import func

from models import db, User, Complaint,ComplaintStatus


view = Blueprint('admin', __name__)


@view.route("/admin")
def index(status=None):
    return render_template('admin.html')


@view.route("/search", methods=['GET', 'POST'])
@view.route("/search/<status>", methods=['GET', 'POST'])
def search(status=None):
    if status:
        subquery = (db.session.query(
            ComplaintStatus.complaint_id,
            func.max(ComplaintStatus.timestamp).label('latest_timestamp'))
                    .group_by(ComplaintStatus.complaint_id)
                    .subquery())

        complaints = db.session.query(Complaint).filter(
            Complaint.id == ComplaintStatus.complaint_id,
            ComplaintStatus.status == status,
            ComplaintStatus.timestamp == subquery.columns.latest_timestamp
        ).order_by(subquery.columns.latest_timestamp.desc()).limit(12)

    else:
        complaints = Complaint.query.order_by(Complaint.timestamp.desc()).limit(12)

    return render_template('search.html', complaints=complaints)


@view.route("/complaint/<complaint_id>")
def complaint(complaint_id=None):
    complaint = Complaint.query.get(complaint_id)
    return render_template('complaint.html', complaint=complaint)


