from app import create_app
from flask import url_for

app = create_app()

app.add_url_rule('/favicon.ico',
                redirect_to=url_for('static', filename='favicon.ico'))