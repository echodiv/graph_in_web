from flask import render_template, flash, redirect, url_for, request, current_app
from app.main import bp

@bp.route("/")
@bp.route("/index")
def index():
    return "hello", 200

