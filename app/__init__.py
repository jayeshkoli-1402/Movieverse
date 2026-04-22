from flask import Flask, redirect, render_template, url_for
from app.routes import route

def CREATE_APP():
    app = Flask(__name__)
    app.secret_key = "supersecret"
    app.register_blueprint(route)
    return app