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


def load_job_from_db(id):
    career_jobs = []
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM career WHERE id = {id}"))
        for row in result:
            career_jobs.append(dict(zip(iter(col), iter(row))))
        print(career_jobs)
        if len(career_jobs) == 0:
            return None
        else:
            return career_jobs[0]


def add_application_to_db():
    pass
