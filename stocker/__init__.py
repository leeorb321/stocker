import os

from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
if os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'instance', 'config.py')):
    app.config.from_pyfile('config.py')


from stocker import views
