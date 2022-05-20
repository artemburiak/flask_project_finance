from flask import Blueprint, request, flash, session, render_template, redirect
from db_control.control import data


page = Blueprint('login', __name__)


@page.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        q = request.form.get('lgn')
        w = request.form.get('pwd')
        if q == '' or ' ' in q:
            flash('Error! Incorrect login.')
        if request.form.get('register_btn') is not None:

            is_registered = data.reg_new_user(q, w)
            if not is_registered:
                flash('Error! Username already used.')
            else:
                print(f'New user:{q},{w}')
        if request.form.get('login_btn') is not None:
            user_info = data.get_user_by_login(q)
            if user_info is not None:
                if user_info[2] == w:
                    print(f'user login:{q},{w}')
                    session['user_id'] = user_info[0]
                    session['username'] = user_info[1]
                    return redirect('/dashboard/')
                else:
                    flash('Error! Incorrect password.')
            else:
                flash('Error! User not found.')
        #
        # elif request.form.get('register_btn') is not None:
        #     print(f'New user:{q},{w}')
    return render_template('homepage.html')