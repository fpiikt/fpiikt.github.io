from config import Config

from flask import Flask

from flask import g

from flask import flash, render_template, redirect

from forms import LoginForm



from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager, UserMixin




app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

import models

from routes import *







if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4321', debug = True)

