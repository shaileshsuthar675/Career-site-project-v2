from models import db


class Career(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    salary = db.Column(db.Integer)
    currency = db.Column(db.String(2000))
    responsibilites = db.Column(db.String(2000))
    requirements = db.Column(db.String(2000))

    def to_dict(self) -> dict:
        out = {
            "id": self.id,
            "Job Title": self.title,
            "Location": self.location,
            "Salary": self.salary,
            "currency": self.currency,
        }
        return out


def all_career_from_db(app):
    careers = []
    with app.app_context():
        all_career = Career.query.all()
        for career in all_career:
            careers.append(career.to_dict())
    return careers


# all_career_from_db()
# with app.app_context():
#     career_dict = career(title="Data Analyst", location="Bengalore", salary="$90,000")
#     db.session.add(career_dict)
#     db.session.commit()
#     all_career = career.query.all()
#     print(all_career)
