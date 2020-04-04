import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog import create_app, db, mail
import unittest

testdb = SQLAlchemy('test.db')
# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'
mail = Mail()

class BasicTests(unittest.TestCase):
    def create__test_app(self):

        app.config.from_object(TestConfig)

        testdb.init_app(app)
        # bcrypt.init_app(app)
        # login_manager.init_app(app)
        mail.init_app(app)

        from flaskblog.users.routes import users
        from flaskblog.posts.routes import posts
        from flaskblog.main.routes import main
        from flaskblog.errors.handlers import errors
        app.register_blueprint(users)
        app.register_blueprint(posts)
        app.register_blueprint(main)
        app.register_blueprint(errors)

        client = app.test_client()

        SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
        SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
        MAIL_SERVER = 'smtp.gmail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = 'masgroupdevry@gmail.com'
        MAIL_PASSWORD = 'maspassword1'

        return app