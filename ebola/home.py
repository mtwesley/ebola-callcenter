
from hashlib import sha256
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from flask import Blueprint, render_template, request, session, redirect, url_for, g, flash
from flask.ext.login import current_user, login_user, logout_user, login_required

from models import db, User


view = Blueprint('home', __name__)


@view.route("/", methods=['GET', 'POST'])
def index():
    return render_template('home.html')


@view.route("/refresh")
def refresh():
    # db.drop_all()
    # db.create_all()
    return "Nothing"


@view.route('/login', methods=['GET', 'POST'])
def login():
    user_action = request.form.get('agent_action', '')
    user_email = request.form.get('user_email', '')
    user_password = request.form.get('user_password', '')

    if g.user.is_authenticated():
        return redirect(url_for('home.index'))

    user = None
    if user_action == 'submit':
        try:
            session.clear()
            eml = user_email.lower()
            hsh = sha256(user_password).hexdigest()
            user = User.query.filter_by(email=eml, hash=hsh).one()

            if user is not None and login_user(user):
                return redirect(request.args.get('next') or url_for('home.index'))

        except NoResultFound:
            flash('Email and password do not match', 'error')

        except MultipleResultsFound:
            flash('Email and password do not match', 'error')

    return render_template('dialog.html', dialog='login.html')


@view.route("/logout")
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('home.login'))
