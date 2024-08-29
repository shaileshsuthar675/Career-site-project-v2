import os
from flask import Flask, render_template, jsonify, request

# from database import all_career_from_db, load_job_from_db
from database2 import jobs, load_job_from_db
from models import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_ENVIRON"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app=app)


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    else:
        return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["post"])
def apply_to_the_job(id):
    form_info = request.form
    job = load_job_from_db(id)
    return render_template("application_submitted.html", application=form_info, job=job)


@app.route("/job/<id>/apply/submitted")
def application_submittion(id):
    job = load_job_from_db(id)
    return render_template(
        "application_submitted_success.html",
        job=job,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
