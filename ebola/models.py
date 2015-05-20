import datetime

from flask import g
from flask.ext.sqlalchemy import SQLAlchemy, orm
from flask.ext.login import UserMixin, current_user


db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    hash = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(128))
    is_agent = db.Column(db.Boolean, default=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), server_default=db.func.now(), nullable=False)

    complaints = db.relationship('Complaint', backref='user', lazy='dynamic')

    def hash_password(self, password):
        pass

    def today_complaints(self, status=None):
        query = self.calls.filter(Complaint.timestamp.between(
            datetime.datetime.today().replace(hour=0, minute=0, second=0),
            datetime.datetime.today().replace(hour=23, minute=59, second=59)))
        if status:
            query = query.join(ComplaintStatus).filter(ComplaintStatus.status == status)
        return query


class Complaint(db.Model):
    __tablename__ = 'complaints'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    phone = db.Column(db.String(23))

    organization = db.Column(db.String(128))
    organization_type = db.Column(db.Enum('moh', 'ingo', 'lngo', 'clinic', 'other', native_enum=False))
    other_organization_type = db.Column(db.String(64))
    position = db.Column(db.String(128))

    county = db.Column(db.String(32))
    district = db.Column(db.String(64))
    city = db.Column(db.String(32))
    address = db.Column(db.String(64))

    is_erw = db.Column(db.Boolean)
    is_moh = db.Column(db.Boolean)
    is_satisfied = db.Column(db.Boolean)

    payment_type = db.Column(db.Enum('salary', 'hazard', 'allowance', 'response', 'unknown', native_enum=False))
    payment_issue = db.Column(db.Enum('not_paid', 'delayed', 'incorrect', 'other', native_enum=False))

    complaint_date = db.Column(db.Date(), default=datetime.datetime.today(), server_default=db.func.now(), nullable=False)
    complaint_description = db.Column(db.Text)
    complaint_resolution = db.Column(db.Text)

    response_date = db.Column(db.Date())
    response_description = db.Column(db.Text)

    comments = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), server_default=db.func.now(), nullable=False)

    statuses = db.relationship('ComplaintStatus', backref='inquiry', lazy='dynamic', cascade="all, delete-orphan")

    @orm.reconstructor
    def set_user(self):
        self.user_id = g.user.id

    def __init__(self):
        self.user_id = g.user.id

    def __nonzero__(self):
        return bool(self.timestamp)

    def first_name(self):
        return self.name.split()[0]

    def status(self, status=None, reason='system', comments=None):
        if status is None:
            return self.statuses.order_by(ComplaintStatus.timestamp.desc()).first()
        else:
            return ComplaintStatus(self, status, reason, comments)


class ComplaintStatus(db.Model):
    __tablename__ = 'complaint_statuses'

    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(db.Integer, db.ForeignKey('complaints.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'open', 'resolved', 'closed', 'duplicate', 'deleted', native_enum=False), nullable=False)
    reason = db.Column(db.String(16), nullable=False)
    comments = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime(), server_default=db.func.now(), nullable=False)

    def __init__(self, complaint, status, reason='system', comments=None):
        self.complaint_id = complaint.id
        self.status = status
        self.reason = reason
        self.comments = comments
        self.user_id = g.user.id

    def __str__(self):
        return self.status
