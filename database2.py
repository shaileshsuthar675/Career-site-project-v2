import os
from models import db
from sqlalchemy import create_engine, text

engine = create_engine(os.environ["DB_ENVIRON"])
application_data_engine = create_engine(os.environ["APPLICATION_DB"])
jobs = []
col = [
    "id",
    "Job Title",
    "Location",
    "Salary",
    "currency",
    "responsibilites",
    "requirements",
]

with engine.connect() as connection:
    result = connection.execute(text("select * from career"))
    for row in result:
        # print(row)
        jobs.append(dict(zip(iter(col), iter(row))))


career_jobs = []


def load_job_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM career WHERE id = {id}"))
        for row in result:
            career_jobs.append(dict(zip(iter(col), iter(row))))
        # print(career_jobs)
        if len(career_jobs) == 0:
            return None
        else:
            return career_jobs[0]


applications = []
application_col = ["id", "job_id", "full_name", "email", "linkedin_url", "address"]


def add_application_to_db(id, application):
    with application_data_engine.connect() as application_db_connection:
        query = text(
            "INSERT INTO application_db (job_id, full_name, email, linkedin_url, address) VALUES (:job_id, :full_name, :email, :linkedin_url, :address)"
        )
        params = {
            "job_id": int(id),
            "full_name": application["inputFName"] + application["inputLName"],
            "email": application["inputEmail4"],
            "linkedin_url": application["linkedinurl"],
            "address": application["inputAddress"]
            + ", "
            + application["inputCity"]
            + ", "
            + application["inputState"]
            + " - "
            + application["inputZip"],
        }

        application_db_connection.execute(query, params)

        result = application_db_connection.execute(
            text(f"SELECT * FROM application_db")
        )
        for row in result:
            applications.append(dict(zip(iter(application_col), iter(row))))
        print(applications)
        if len(applications) == 0:
            return None
        else:
            return applications
