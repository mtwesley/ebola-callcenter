
from hashlib import sha256
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash, abort
from flask.ext.login import current_user, login_user, logout_user, login_required
from sqlalchemy import func

from models import db, User, Complaint,ComplaintStatus

import helpers


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
@view.route("/search/<current_status>", methods=['GET', 'POST'])
def search(current_status=None):

    search_action = request.form.get('search_action', '')

    subquery = (db.session.query(ComplaintStatus.complaint_id,
                                 func.max(ComplaintStatus.timestamp).label('latest_timestamp'))
                .group_by(ComplaintStatus.complaint_id).subquery())

    if current_status:

        complaints = db.session.query(Complaint).filter(
            Complaint.id == ComplaintStatus.complaint_id,
            Complaint.id == subquery.columns.complaint_id,
            ComplaintStatus.status == current_status,
            ComplaintStatus.timestamp == subquery.columns.latest_timestamp
        )

    else:
        complaints = db.session.query(Complaint).filter(
            Complaint.id == ComplaintStatus.complaint_id,
            Complaint.id == subquery.columns.complaint_id,
            ComplaintStatus.status != 'pending',
            ComplaintStatus.timestamp == subquery.columns.latest_timestamp
        )

    if search_action == 'submit':
        complaint_id = request.form.get('complaint_id', '')
        if complaint_id:
            complaints = complaints.filter(Complaint.id == int(complaint_id))

        phone = request.form.get('phone', '')
        if phone:
            complaints = complaints.filter(Complaint.phone == helpers.e164_phone_number(phone))

        name = request.form.get('name', '')
        if name:
            for x in name.split():
                complaints = complaints.filter(Complaint.name.ilike('%'+x+'%'))

        workplace = request.form.get('workplace', '')
        if workplace:
            complaints = complaints.filter(Complaint.workplace == workplace)

        organization = request.form.get('organization', '')
        if organization:
            for x in organization.split():
                complaints = complaints.filter(Complaint.name.ilike('%'+x+'%'))

        position = request.form.get('position', '')
        if position:
            for x in position.split():
                complaints = complaints.filter(Complaint.name.ilike('%'+x+'%'))

        county = request.form.get('county', '')
        if county:
            complaints = complaints.filter(Complaint.county == county)

        location = request.form.get('location', '')
        if location:
            for x in location.split():
                complaints = complaints.filter(
                    (Complaint.city.ilike('%'+x+'%')) |
                    (Complaint.address.ilike('%'+x+'%')))

        is_government = request.form.get('is_government', '')
        if is_government:
            if is_government == 'Y':
                complaints = complaints.filter(Complaint.is_government == True)
            elif is_government == 'N':
                complaints = complaints.filter(Complaint.is_government == False)

        is_moh = request.form.get('is_moh', '')
        if is_moh:
            if is_moh == 'Y':
                complaints = complaints.filter(Complaint.is_moh == True)
            elif is_moh == 'N':
                complaints = complaints.filter(Complaint.is_moh == False)

        payment_type = request.form.get('payment_type', '')
        if payment_type:
            complaints = complaints.filter(Complaint.payment_type == payment_type)

    else:
        current_status = None
        complaint_id = None
        name = None
        phone = None
        workplace = None
        organization = None
        position = None
        county = None
        location = None
        is_moh = None
        is_government = None
        payment_type = None

    complaints = complaints.order_by(subquery.columns.latest_timestamp.desc()).limit(12)

    return render_template('search.html', current_status=current_status, complaints=complaints,
                           complaint_id=complaint_id, name=name, phone=phone, workplace=workplace,
                           organization=organization, position=position, county=county, location=location,
                           is_government=is_government, is_moh=is_moh, payment_type=payment_type)


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
            return redirect(url_for('admin.search', current_status=str(complaint.status())))

    return render_template('complaint.html', complaint=complaint)


