from flask import Blueprint, render_template, request, abort, session
from db_control.control import data

page = Blueprint('dashboard', __name__)



@page.route('/', methods=['GET', 'POST'])
def dashboard():
    q = session.get('user_id')
    if q is None:
        abort(404)

    if request.method == 'POST':
        amount = request.form.get('amount')
        comment = request.form.get('comment')

        if request.form.get('submit-income') is not None:
            data.add_new_trans(int(amount), comment, True, 1)
            print('New transaction Income')

        elif request.form.get('submit-outcome') is not None:
            data.add_new_trans(int(amount), comment, False, 1)
            print('New transaction Outcome')
    tr = data.get_transactions(int(q))
    return render_template('dashboard.html', data = tr)
