from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from sqlalchemy.sql import functions as func

app_db = SQLAlchemy()


class User(app_db.Model):
    __tablename__ = "users"

    id = sa.Column(sa.BIGINT, primary_key=True)
    name = sa.Column(sa.String(128))

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(id, deferrable=True), nullable=True)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())

    modified_by = sa.Column(sa.BIGINT, sa.ForeignKey(id, deferrable=True), nullable=True)
    modified_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class Phone(app_db.Model):
    __tablename__ = "phones"

    id = sa.Column(sa.BIGINT, primary_key=True)
    msisdn = sa.Column(sa.String(23), nullable=False, unique=True)

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=True)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())

    modified_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=True)
    modified_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class Contact(app_db.Model):
    __tablename__ = "contacts"

    id = sa.Column(sa.BIGINT, primary_key=True)
    name = sa.Column(sa.String(128), nullable=False)
    sex = sa.Column(sa.Enum("M", "F", "N", "U", name="sex"), nullable=False)
    lang = sa.Column(sa.String(50), nullable=False)
    county = sa.Column(sa.String(50))
    city = sa.Column(sa.String(50))
    location = sa.Column(sa.String(255))
    community = sa.Column(sa.String(255))

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())

    modified_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    modified_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class ContactStatus(app_db.Model):
    __tablename__ = "contact_statuses"

    id = sa.Column(sa.BIGINT, primary_key=True)
    contact_id = sa.Column(sa.BIGINT, sa.ForeignKey(Contact.id), nullable=False)
    status = sa.Column(sa.String(255))

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class Call(app_db.Model):
    __tablename__ = "calls"

    id = sa.Column(sa.BIGINT, primary_key=True)
    type = sa.Column(sa.String(128), nullable=False)
    phone_id = sa.Column(sa.BIGINT, sa.ForeignKey(Phone.id), nullable=False)
    contact_id = sa.Column(sa.BIGINT, sa.ForeignKey(Contact.id), nullable=False)

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())

    modified_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    modified_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class CallStatus(app_db.Model):
    __tablename__ = "call_statuses"

    id = sa.Column(sa.BIGINT, primary_key=True)
    status = sa.Column(sa.String(128), nullable=False)
    comments = sa.Column(sa.String, nullable=True)
    old_content = sa.Column(sa.String, nullable=True)
    new_content = sa.Column(sa.String, nullable=True)

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())

    modified_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    modified_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class Case(app_db.Model):
    __tablename__ = "cases"

    id = sa.Column(sa.BIGINT, primary_key=True)
    contact_id = sa.Column(sa.BIGINT, sa.ForeignKey(Contact.id), nullable=False)
    context = sa.Column(sa.String, nullable=False)
    case_number = sa.Column(sa.String(128), nullable=False)
    condition = sa.Column(sa.String)
    phone_id = sa.Column(sa.BIGINT, sa.ForeignKey(Contact.id), nullable=False)

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())

    modified_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    modified_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class CaseSymptom(app_db.Model):
    __tablename__ = "case_symptoms"

    id = sa.Column(sa.BIGINT, primary_key=True)
    case_id = sa.Column(sa.BIGINT, sa.ForeignKey(Case.id), nullable=False)
    symptom = sa.Column(sa.String, nullable=False)
    start_ts = sa.Column(sa.DateTime(timezone=True), nullable=False)
    end_ts = sa.Column(sa.DateTime(timezone=True), nullable=False)

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())


class CaseStatus(app_db.Model):
    __tablename__ = "case_statuses"

    id = sa.Column(sa.BIGINT, primary_key=True)

    case_id = sa.Column(sa.BIGINT, sa.ForeignKey(Case.id), nullable=False)
    status = sa.Column(sa.String(128), nullable=False)
    comments = sa.Column(sa.String, nullable=True)
    old_content = sa.Column(sa.String, nullable=True)
    new_content = sa.Column(sa.String, nullable=True)

    created_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    created_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())

    modified_by = sa.Column(sa.BIGINT, sa.ForeignKey(User.id), nullable=False)
    modified_ts = sa.Column(sa.DateTime(timezone=True), server_default=func.now(), default=func.now())
