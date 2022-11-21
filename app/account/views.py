from app import db
from app.models import User
from flask import redirect, render_template, url_for
from flask_login import login_required
from . import account


@ account.route('/user/detail/<int:id>')
@ login_required
def detail_user(id):
    user = User.query.get(id)
    return render_template('user-detail.html', user=user)


@ account.route('/user/delete/<int:id>')
@ login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    print(user.name)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('index'))
