import os
from flask import Flask, render_template, jsonify

from database import all_career_from_db
from models import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ("DB_ENVIRON")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app=app)


jobs = all_career_from_db(app=app)


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
