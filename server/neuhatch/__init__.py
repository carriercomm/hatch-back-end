from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from neuhatch.config import get_default_config

config = get_default_config()
app = Flask(__name__)
app.secret_key = config.app_secret
app.config["SQLALCHEMY_DATABASE_URI"] = config.database_url
db = SQLAlchemy(app)

import neuhatch.views
import neuhatch.models
