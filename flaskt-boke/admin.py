#admin.py
from flask import Blueprint

admin =Blueprint('admin',__name__)


@admin.route('/index')
def adminindex():
    return '4'
@admin.route('/show')
def adminshow():
    return '5'
@admin.route('/add')
def adminadd():
    return '6'
