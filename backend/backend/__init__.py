from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

backend = Flask(__name__)
backend.config.from_object(Config)
db = SQLAlchemy(backend)
migrate = Migrate(backend, db)

from backend import routes
