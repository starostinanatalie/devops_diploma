from flask import Flask
from flask_bootstrap import Bootstrap

app_frontend = Flask(__name__)

bootstrap = Bootstrap(app_frontend)

from app_frontend import routes