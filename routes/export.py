from flask import Blueprint, render_template, request, abort, session, send_file
from db_control.control import data
from docx_generator import CreateDocument

page = Blueprint('export', __name__)

@page.route('/')
def export():
    user_id = session.get('user_id')
    username = session.get('username')
    transactions = data.get_transactions(user_id)
    path = CreateDocument(user_id, username, transactions).save()
    return send_file(path)