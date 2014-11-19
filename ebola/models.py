from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, BIGINT, ForeignKey, DateTime, Enum
from sqlalchemy.sql import functions

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True)
    name = Column(String(128))

    created_by = Column(BIGINT, ForeignKey(id, deferrable=True), nullable=True)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    modified_by = Column(BIGINT, ForeignKey(id, deferrable=True), nullable=True)
    modified_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())


class Phone(db.Model):
    __tablename__ = "phones"

    id = Column(BIGINT, primary_key=True)
    msisdn = Column(String(23), nullable=False, unique=True)

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=True)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    modified_by = Column(BIGINT, ForeignKey(User.id), nullable=True)
    modified_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    calls = db.relationship("Call", backref="call")
    cases = db.relationship("Case", backref="case")


class Contact(db.Model):
    __tablename__ = "contacts"

    id = Column(BIGINT, primary_key=True)
    name = Column(String(128), nullable=False)
    sex = Column(Enum("M", "F", "N", "U", name="sex"), nullable=False)
    lang = Column(String(50), nullable=False)
    county = Column(String(50))
    city = Column(String(50))
    location = Column(String(255))
    community = Column(String(255))

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    modified_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    modified_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    status = db.relationship("ContactStatus", backref="contact_status")
    ##case = db.relationship("Case", uselist=False, backref="case", foreign_keys="contact_id")


class ContactStatus(db.Model):
    __tablename__ = "contact_statuses"

    id = Column(BIGINT, primary_key=True)
    contact_id = Column(BIGINT, ForeignKey(Contact.id), nullable=False)
    status = Column(String(255))

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())


class Call(db.Model):
    __tablename__ = "calls"

    id = Column(BIGINT, primary_key=True)
    type = Column(String(128), nullable=False)
    phone_id = Column(BIGINT, ForeignKey(Phone.id), nullable=False)
    contact_id = Column(BIGINT, ForeignKey(Contact.id), nullable=False)

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    modified_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    modified_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    status = db.relationship("CallStatus", backref="case_status")


class CallStatus(db.Model):
    __tablename__ = "call_statuses"

    id = Column(BIGINT, primary_key=True)
    call_id = Column(BIGINT, ForeignKey(Call.id), nullable=False)
    status = Column(String(128), nullable=False)
    comments = Column(String, nullable=True)
    old_content = Column(String, nullable=True)
    new_content = Column(String, nullable=True)

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    modified_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    modified_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())


class Case(db.Model):
    __tablename__ = "cases"

    id = Column(BIGINT, primary_key=True)
    contact_id = Column(BIGINT, ForeignKey(Contact.id), nullable=False)
    context = Column(String, nullable=False)
    case_number = Column(String(128), nullable=False)
    condition = Column(String)
    phone_id = Column(BIGINT, ForeignKey(Phone.id), nullable=False)

    symptoms = db.relationship("CaseSymptom", backref="case_symptom")
    status = db.relationship("CaseStatus", backref="case_status")

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    modified_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    modified_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())


class CaseSymptom(db.Model):
    __tablename__ = "case_symptoms"

    id = Column(BIGINT, primary_key=True)
    case_id = Column(BIGINT, ForeignKey(Case.id), nullable=False)
    symptom = Column(String, nullable=False)
    start_ts = Column(DateTime(timezone=True), nullable=False)
    end_ts = Column(DateTime(timezone=True), nullable=False)

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())


class CaseStatus(db.Model):
    __tablename__ = "case_statuses"

    id = Column(BIGINT, primary_key=True)

    case_id = Column(BIGINT, ForeignKey(Case.id), nullable=False)
    status = Column(String(128), nullable=False)
    comments = Column(String, nullable=True)
    old_content = Column(String, nullable=True)
    new_content = Column(String, nullable=True)

    created_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())

    modified_by = Column(BIGINT, ForeignKey(User.id), nullable=False)
    modified_ts = Column(DateTime(timezone=True), server_default=functions.now(), default=functions.now())
