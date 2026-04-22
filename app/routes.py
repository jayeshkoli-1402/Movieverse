from flask import Blueprint, Flask, redirect, render_template, url_for, session, request
from app.model import recommend
route = Blueprint("route_bp", __name__)




@route.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        movie_name = request.form.get("movie")
        print(movie_name)
        
        recommendations = recommend(movie_name)

    return render_template("home.html", recommendations=recommendations)