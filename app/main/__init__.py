#!/usr/bin/env python3
"""Blueprint Initialization"""

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
