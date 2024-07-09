from flask import Flask
from app.database import db, migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

db.init_app(app)
migrate.init_app(app, db)

from app import models
