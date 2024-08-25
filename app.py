from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        "Job Title": "Data Analyst",
        "Location": "Pune",
        "Salary": "$100,000",
    },
    {
        "Job Title": "Data Scientist",
        "Location": "Gurgaon",
        "Salary": "$120,000",
    },
    {
        "Job Title": "Data Analyst",
        "Location": "Bengalore",
        "Salary": "$90,000",
    },
    {
        "Job Title": "Software Development Engineer",
        "Location": "Mumbai",
        "Salary": "$950,000",
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
