#[to-do] colocar variável de ambiente aqui

import os

SECRET_KEY = '5DgDZ{_B?&F&HC2Yys'
SQLALCHEMY_DATABASE_URI = 'mysql://shiori_admin:shiori2019@localhost/shiori_db'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = 1
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']


#SEND_MAIL_FROM = 'project.shiori2019@gmail.com'
#MAIL_SERVER=smtp.googlemail.com
#MAIL_PORT=587
#MAIL_USE_TLS=1
#MAIL_USERNAME='project.shiori2019@gmail.com'
#MAIL_PASSWORD='shiori#2019'

