from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), index=True, unique=True)
    content = db.Column(db.String(99999))
    url = db.Column(db.String(9999))
    picture = db.Column(db.String(50), unique=True)
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    more = db.relationship('Extend', backref='EX', lazy='dynamic')
    tech = db.relationship('Tech', backref='TF', lazy='dynamic')
    net = db.relationship('Network', backref='NET', lazy='dynamic')
    anime = db.relationship('Anime', backref='ANI', lazy='dynamic')
    eva = db.relationship('Evaluation', backref='EVA', lazy='dynamic')
    ittime = db.relationship('Ittime', backref='ITT', lazy='dynamic')
    reward = db.relationship('Reward', backref='RW', lazy='dynamic')
    video = db.relationship('Video', backref='VDO', lazy='dynamic')
    special = db.relationship('Special', backref='SP', lazy='dynamic')
    editor = db.relationship('Editor', backref='ED', lazy='dynamic')

    def __repr__(self):
        return '<News {}>'.format(self.title)


class Extend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    nd_con = db.Column(db.String(99999))
    rd_con = db.Column(db.String(99999))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Tech(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))
    nd_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Network(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))
    nd_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))
    nd_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Evaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))
    nd_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Ittime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))
    nd_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Ads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    picture_name = db.Column(db.String(50))
    url = db.Column(db.String(9999))
    big = db.Column(db.Boolean(create_constraint=False, _create_events=False), nullable=False, server_default='False')

    def __repr__(self):
        return '<Ads_name {}>'.format(self.name)


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))
    vdo_link = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Special(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)


class Editor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_name = db.Column(db.String(50), db.ForeignKey('news.picture'))
    st_cat = db.Column(db.String(50))

    def __repr__(self):
        return '<Picture {}>'.format(self.picture_name)
