#app/models.py
from . import db,login_manager
from flask_login import UserMixin
from datetime import datetime
class Comment(db.Model):
    __tablename__='comments'
    id =db.Column(db.Integer,primary_key=True)
    body =db.Column(db.String(200),nullable=True)
    created =db.Column(db.DateTime,index=True,default=datetime.now)
    post_id =db.Column(db.Integer,db.ForeignKey('posts.id'))
    author_id =db.Column(db.Integer,db.ForeignKey('users.id'))
class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(20),nullable=True)
    body =db.Column(db.String(200),nullable=True)
    body_html =db.Column(db.String(200),nullable=True)
    created =db.Column(db.DateTime,index=True,default=datetime.now)
    author_id =db.Column(db.Integer,db.ForeignKey('users.id'))
    comments =db.relationship('Comment',backref ='post')
class Role(db.Model):
    __tablename__='role'
    __table_args__={'extend_existing':True}
    id=db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(20),nullable=True)
    users =db.relationship('User',backref='role')
class User(db.Model,UserMixin):
    __tablename__='users'
    __table_args__={'extend_existing':True}
    id=db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(20),nullable=True)
    password=db.Column(db.String(40),nullable=True)
    email =db.Column(db.String(20),nullable=True)
    age=db.Column(db.Integer,nullable=True)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))    
    posts =db.relationship('Post',backref='author')
    comments =db.relationship('Comment',backref ='author')
    @staticmethod
    def on_created(target,value,oldvalue,initiator):
        target.role =Role.query.filter_by(name='user').first()
        db.session.add(target)
        db.session.commit()
        print('haha')

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

db.event.listen(User.name,'set',User.on_created)
