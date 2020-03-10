import os


class Config:
    SECRET_KEY = 'f7446e435991868183813c59f0307b58' # u produkciji export to enviroment variables kako bi se zastitila privatnost
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # u produkciji export to enviroment variables kako bi se zastitila privatnost
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    #app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = 'kupusislanina@gmail.com' # u produkciji export to enviroment variables kako bi se zastitila privatnost
    MAIL_PASSWORD = 'epiphone' # u produkciji export to enviroment variables kako bi se zastitila privatnost