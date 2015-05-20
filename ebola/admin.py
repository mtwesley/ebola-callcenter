
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
@view.route("/search/<status>", methods=['GET', 'POST'])
def search(status=None):

    search_action = request.form.get('search_action', '')

    subquery = (db.session.query(ComplaintStatus.complaint_id,
                                 func.max(ComplaintStatus.timestamp).label('latest_timestamp'))
                .group_by(ComplaintStatus.complaint_id).subquery())

    if status:

        complaints = db.session.query(Complaint).filter(
            Complaint.id == ComplaintStatus.complaint_id,
            Complaint.id == subquery.columns.complaint_id,
            ComplaintStatus.status == status,
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

        organization = request.form.get('organization', '')
        if organization:
            for x in organization.split():
                complaints = complaints.filter(Complaint.name.ilike('%'+x+'%'))

        organization_type = request.form.get('organization_type', '')
        if organization_type:
            complaints = complaints.filter(Complaint.organization_type == organization_type)

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
                    (Complaint.district.ilike('%'+x+'%')) |
                    (Complaint.city.ilike('%'+x+'%')) |
                    (Complaint.address.ilike('%'+x+'%')))

        is_moh = request.form.get('is_moh', '')
        if is_moh:
            if is_moh == 'Y':
                complaints = complaints.filter(Complaint.is_moh == True)
            elif is_moh == 'N':
                complaints = complaints.filter(Complaint.is_moh == False)

        is_erw = request.form.get('is_erw', '')
        if is_erw:
            if is_erw == 'Y':
                complaints = complaints.filter(Complaint.is_erw == True)
            elif is_erw == 'N':
                complaints = complaints.filter(Complaint.is_erw == False)

        payment_type = request.form.get('payment_type', '')
        if county:
            complaints = complaints.filter(Complaint.payment_type == payment_type)

        payment_issue = request.form.get('payment_issue', '')
        if county:
            complaints = complaints.filter(Complaint.payment_issue == payment_issue)

        complaints = complaints.order_by(subquery.columns.latest_timestamp.desc()).limit(12)
        
    else:
        status = None
        complaints = None
        complaint_id = None
        name = None
        phone = None
        organization = None
        organization_type = None
        position = None
        county = None
        location = None
        is_moh = None
        is_erw = None
        payment_type = None
        payment_issue = None

        complaints = complaints.order_by(subquery.columns.latest_timestamp.desc()).limit(12)

    return render_template('search.html', status=status, complaints=complaints, complaint_id=complaint_id, name=name,
                           phone=phone, organization=organization, organization_type=organization_type,
                           position=position, county=county, location=location, is_moh=is_moh, is_erw=is_erw,
                           payment_type=payment_type, payment_issue=payment_issue)


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


