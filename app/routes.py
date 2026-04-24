from flask import Flask, redirect, render_template, url_for, session, Blueprint, request
from app.model import reccomend, movies

route = Blueprint("route", __name__)

@route.route("/", methods = ["POST", "GET"])
def home():
    title = movies["title"].to_frame()
    table = title.to_html(classes="table", index=False)
    if request.method == "POST":
        title = request.form.get("movie")
        reccomendation = reccomend(title)
        
        return render_template("home.html", reccomendation = reccomendation, table = table)
    return render_template("home.html", table = table)
