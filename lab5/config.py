import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'asfdsfsaaf'
WTF_CRSF_ENAVLED = True
# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'form.db')
# SQLALCHEMY_DATABASE_URI =  'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False