from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc



def init_app():
    app = Flask(__name__)
    app.config['SECRECT_KEY'] = 'updown'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://DESKTOP-LSF0DGJ/e-cormmerce' # 
    
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    return app