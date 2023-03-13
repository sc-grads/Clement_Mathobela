from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://localhost/e-commerce?driver=ODBC+Driver+17+for+SQL+Server?trusted_connection=yes'
    db.init_app(app)
    return app
