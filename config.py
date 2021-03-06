import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = '587'
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = True
    # MAIL_USE_TLS = 'os.environ.get('MAIL_USE_TLS') is not None'
    MAIL_USERNAME = 'masgroupdevry@gmail.com'
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'maspassword1'
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['bwinterhalter@my.devry.edu']
    # ADMINS = ['your-email@example.com']
    LANGUAGES = ['en']#, 'es']
    POSTS_PER_PAGE = 25
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    FLASK_DEBUG=1