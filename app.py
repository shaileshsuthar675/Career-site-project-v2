import os
from flask import Flask, render_template, jsonify

from database import all_career_from_db
from models import db
from dotenv_vault import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SERVER")
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///career.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app=app)


jobs = all_career_from_db(app=app)
print(type(jobs[0]))


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
