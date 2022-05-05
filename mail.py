from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] =  'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'collinsabaya07@gmail.com'
app.config['MAIL_PASSWORD'] = None
app.config['MAIL_DEFAULT_SENDER'] = 'collinsabaya07@gmail.com'
#app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPRESS_SENDER'] = False


mail = Mail(app)