import datetime
import helpers
from phonenumbers import parse as parse_number, format_number, PhoneNumberFormat

from flask import g
from flask.ext.sqlalchemy import SQLAlchemy, orm
from flask.ext.login import UserMixin, current_user


db = SQLAlchemy()

phone_contacts = db.Table('phone_contacts',
    db.Column('phone_id', db.Integer, db.ForeignKey('phones.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False),
    db.Column('contact_id', db.Integer, db.ForeignKey('contacts.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    hash = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), server_default=db.func.now(), nullable=False)

    calls = db.relationship('Call', backref='user', lazy='dynamic')
    cases = db.relationship('Case', backref='user', lazy='dynamic')

    def hash_password(self, password):
        pass


class Phone(db.Model):
    __tablename__ = 'phones'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(23), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), server_default=db.func.now(), nullable=False)

    calls = db.relationship('Call', backref='phone', lazy='dynamic')
    contacts = db.relationship('Contact', secondary=phone_contacts, lazy='dynamic')
    user = db.relationship('User')

    COUNTRY_CODE = 'LR'

    @classmethod
    def lookup(cls, number):
        return Phone.query.filter_by(number=Phone.e164(number)).first()

    @classmethod
    def lookup_or_create(cls, number):
        lookup = Phone.lookup(number)
        return lookup if lookup is not None else Phone(number)
        # if lookup is not None:
        #     return lookup
        # else:
        #     create = Phone(number)
        #     db.session.add(create)
        #     return create

    @classmethod
    def e164(cls, number):
        return str(format_number(
            parse_number(number, Phone.COUNTRY_CODE),
            PhoneNumberFormat.E164))

    @classmethod
    def local(cls, number):
        return str(format_number(
            parse_number(number, Phone.COUNTRY_CODE),
            PhoneNumberFormat.NATIONAL))

    @classmethod
    def international(cls, number):
        return str(format_number(
            parse_number(number, Phone.COUNTRY_CODE),
            PhoneNumberFormat.INTERNATIONAL))

    @orm.reconstructor
    def set_user(self):
        self.user_id = g.user.id

    def __init__(self, number):
        self.number = str(Phone.e164(number))
        self.user_id = g.user.id

    def __nonzero__(self):
        return bool(self.number)

    def cases(self):
        return Case.query.join(Contact).join(phone_contacts).join(Phone).filter(Phone.number == self.number)

    def pretty(self):
        return Phone.local(self.number)


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    middle_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    suffix = db.Column(db.Enum('jr', 'sr', 'ii', 'iii', native_enum=False))
    sex = db.Column(db.Enum('male', 'female', native_enum=False))
    age = db.Column(db.Integer)
    language = db.Column(db.String(32))
    county = db.Column(db.String(32))
    city = db.Column(db.String(32))
    community = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), server_default=db.func.now(), nullable=False)

    calls = db.relationship('Call', backref='caller', lazy='dynamic')
    cases = db.relationship('Case', backref='patient', lazy='dynamic')
    phones = db.relationship('Phone', secondary=phone_contacts, lazy='dynamic')

    @orm.reconstructor
    def set_user(self):
        self.user_id = g.user.id

    def __init__(self):
        self.user_id = g.user.id

    def name(self):
        return ' '.join([self.first_name or '', self.middle_name or '', self.last_name or '', self.suffix or '']).strip()

    def call_cases(self):
        return Case.query.join(Call).join(Call.caller).filter(Contact.id == self.id)

    def today_calls(self):
        return self.calls.filter(Call.timestamp.between(
            datetime.datetime.today(),
            datetime.datetime.today().replace(hour=11, min=59, second=59)))


class Call(db.Model):
    __tablename__ = 'calls'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('case_report', 'case_update', 'case_inquiry', 'general_inquiry', native_enum=False))
    phone_id = db.Column(db.Integer, db.ForeignKey('phones.id'))
    caller_id = db.Column(db.Integer, db.ForeignKey('contacts.id'))
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), server_default=db.func.now(), nullable=False)

    statuses = db.relationship('CallStatus', backref='call', lazy='dynamic', cascade="all, delete-orphan")

    @orm.reconstructor
    def set_user(self):
        self.user_id = g.user.id

    def __init__(self, phone=None):
        if phone is None:
            pass
        elif isinstance(phone, Phone):
            self.phone = phone
        else:
            self.phone = Phone(phone)
        self.user_id = g.user.id

    def __nonzero__(self):
        return bool(self.timestamp)


class CallStatus(db.Model):
    __tablename__ = 'call_statuses'

    id = db.Column(db.Integer, primary_key=True)
    call_id = db.Column(db.Integer, db.ForeignKey('calls.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.Enum('pending', 'active', 'cancelled', 'deleted', native_enum=False), nullable=False)
    reason = db.Column(db.String(32))
    comments = db.Column(db.String(256))
    json = db.Column(db.Text, nullable=False)


class Case(db.Model):
    __tablename__ = 'cases'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('contacts.id'))
    dhis2_number = db.Column(db.String(32))
    condition = db.Column(db.Enum('conscious', 'unconscious', 'alive', 'dead', native_enum=False))
    had_contact = db.Column(db.Boolean)
    days_sick = db.Column(db.Integer)
    comments = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), server_default=db.func.now(), nullable=False)

    calls = db.relationship('Call', backref='case', lazy='dynamic')
    symptoms = db.relationship('CaseSymptom', backref='case', lazy='dynamic', cascade="all, delete-orphan")
    statuses = db.relationship('CaseStatus', backref='case', lazy='dynamic', cascade="all, delete-orphan")

    @orm.reconstructor
    def set_user(self):
        self.user_id = g.user.id

    def __init__(self):
        self.user_id = g.user.id

    def __nonzero__(self):
        return bool(self.timestamp)

    def pretty_symptoms(self):
        pretty = []
        for s in self.symptoms.all():
            pretty.append(helpers.symptom[s.symptom])
        return ', '.join(pretty)


class CaseSymptom(db.Model):
    __tablename__ = 'case_symptoms'

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    symptom = db.Column(db.Enum(
        'abdominal_pain', 'black_stool', 'diarrhea', 'difficulty_breathing',
        'difficulty_swallowing', 'fever', 'headache', 'hiccups', 'loss_of_appetite',
        'muscle_pain', 'nausea', 'red_eyes', 'skin_rash', 'sore_throat', 'unexplained_bleeding',
        'vomiting', 'weakness', native_enum=False), nullable=False)
    start_ts = db.Column(db.DateTime())
    end_ts = db.Column(db.DateTime())

    def __init__(self, case, symptom):
        self.case = case
        self.symptom = symptom


class CaseStatus(db.Model):
    __tablename__ = 'case_statuses'

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'active', 'duplicate', 'deleted', native_enum=False), nullable=False)
    reason = db.Column(db.String(32))
    comments = db.Column(db.String(256))
    json = db.Column(db.Text, nullable=True)


