import os

class Config:
    SECRET_KEY = '8c235245f18bdcb3b09d640b145d8199'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sampathkumar.r1212@gmail.com'
    MAIL_PASSWORD = 'sampath@google9201'
    UPLOAD_FOLDER = '/static/data_files'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}



#app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
