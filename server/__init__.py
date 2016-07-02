from flask import Flask

app = Flask(__name__)

from .views import site
from .views import api

app.register_blueprint(site.mod)
app.register_blueprint(api.mod)
