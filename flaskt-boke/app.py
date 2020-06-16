#app.py
from flask import Flask
from flask_script import Manager
from livereload import Server
from flask_migrate import Migrate,MigrateCommand
from app import *
#from app.models import User,Role

from admin import admin #from 文件名 import 标识符
from user import user

app =create_app()
#app=Flask(__name__)
manager =Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user,url_prefix='/user')
@manager.command
def dev():
    live_server=Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)

if __name__ =='__main__':
    #app.run(host='0.0.0.0',port=5000)
    manager.run()
