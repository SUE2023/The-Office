#!/usr/bin/env python3
""" Flask application instance"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

from app import models
