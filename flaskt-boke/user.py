#user.py
from flask import Blueprint

user =Blueprint('user',__name__)


@user.route('/index')
def adminindex():
    return '4'
@user.route('/show')
def adminshow():
    return '5'
@user.route('/add')
def adminadd():
    return '6'
 
