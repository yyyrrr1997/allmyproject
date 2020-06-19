#app/__init__.py
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_avatar import Avatar

bootstrap =Bootstrap()
nav =Nav()
db =SQLAlchemy()
pagedown =PageDown()

login_manager =LoginManager()
login_manager.login_view= 'auth.login'
login_manager.login_message ='请先登录'
login_manager.login_message_category ='info'
def create_app():
    app =Flask(__name__)
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:1234@127.0.0.1/flasktest'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    bootstrap.init_app(app)
   # navbar =Navbar('BootstrapTest',
           # View('主页','main.index'),
           # View('服务','main.services'),
           # View('项目','main.projects'),
           # View('关于','main.about'))
    #nav.register_element('top',navbar)
    nav.init_app(app)
    db.init_app(app)
    #init_view(app)
    pagedown.init_app(app)
    Avatar(app)
    CSRFProtect(app)

    login_manager.init_app(app)

    from .auth import auth
    from .main import main

    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(main,url_prefix='/main')

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path
    return app
