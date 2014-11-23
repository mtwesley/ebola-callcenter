import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)


phone_contacts = db.Table('phone_contacts',
    db.Column('phone_id', db.Integer, db.ForeignKey('phones.id', onupdate='CASCADE', ondelete='CASCADE')),
    db.Column('contact_id', db.Integer, db.ForeignKey('contacts.id', onupdate='CASCADE', ondelete='CASCADE'))
)


class Phone(db.Model):
    __tablename__ = 'phones'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(23), nullable=False, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)

    calls = db.relationship(Call, backref='phone', lazy='dynamic')
    contacts = db.relationship(Contact, secondary=phone_contacts, backref='phones', lazy='dynamic')


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    middle_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    suffix = db.Column(db.Enum('jr', 'sr', 'ii', 'iii', native_enum=False))
    sex = db.Column(db.Enum('male', 'female', native_enum=False))
    language = db.Column(db.String(32))
    county = db.Column(db.String(32))
    city = db.Column(db.String(32))
    community = db.Column(db.String(64))
    condition = db.Column(db.Enum('conscious', 'unconscious', 'alive', 'dead', native_enum=False))

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)

    calls = db.relationship(Call, backref='caller', lazy='dynamic')
    cases = db.relationship(Case, backref='patient', lazy='dynamic')

    status = db.relationship('ContactStatus', backref='contact_status')


class Call(db.Model):
    __tablename__ = 'calls'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('case_report', 'case_update', 'case_inquiry', 'general_inquiry', native_enum=False))
    phone_id = db.Column(db.Integer, db.ForeignKey(Phone.id), nullable=False)
    caller_id = db.Column(db.Integer, db.ForeignKey(Contact.id), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey(Case.id))

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)

    cases = db.relationship(Case, backref='call', lazy='dynamic')

    statuses = db.relationship(CallStatus, backref='call', lazy='dynamic')


class CallStatus(db.Model):
    __tablename__ = 'call_statuses'

    id = db.Column(db.Integer, primary_key=True)
    call_id = db.Column(db.Integer, db.ForeignKey(Call.id), nullable=False)
    status = db.Column(db.Enum('pending', 'active', 'cancelled', 'deleted', native_enum=False), nullable=False)
    reason = db.Column(db.String(32))
    comments = db.Column(db.String(256))
    json = db.Column(db.Text, nullable=False)


class Case(db.Model):
    __tablename__ = 'cases'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey(Contact.id), nullable=False)
    dhis2_number = db.Column(db.String(32))
    comments = db.Column(db.String(256))

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)

    symptoms = db.relationship(CaseSymptom, backref='case', lazy='dynamic')
    statuses = db.relationship(CaseStatus, backref='case', lazy='dynamic')


class CaseSymptom(db.Model):
    __tablename__ = 'case_symptoms'

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey(Case.id), nullable=False)
    symptom = db.Column(db.Enum(
        'abdominal_pain', 'black_stool', 'diarrhea', 'difficulty_breathing',
        'difficulty_swallowing', 'fever', 'headache', 'hiccups', 'loss_of_appetite',
        'muscle_pain', 'nausea', 'red_eyes', 'skin_rash', 'sore_throat', 'unexplained_bleeding',
        'vomiting', 'weakness', native_enum=False), nullable=False)
    start_ts = db.Column(db.DateTime(), nullable=False)
    end_ts = db.Column(db.DateTime(), nullable=False)

    call = db.relationship(Call, backref='symptoms', lazy='dynamic')


class CaseStatus(db.Model):
    __tablename__ = 'case_statuses'

    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey(Case.id), nullable=False)
    status = db.Column(db.Enum('pending', 'active', 'duplicate', 'deleted', native_enum=False), nullable=False)
    reason = db.Column(db.String(32))
    comments = db.Column(db.String(256))
    json = db.Column(db.Text, nullable=True)


