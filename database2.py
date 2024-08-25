from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:shai@saarthee@06@some_mariadb/dbname?charset=utf8mb4"
)
db_connection_string = "mysql+pymysql://root:shai@saarthee@06@localhost/world"

engine = create_engine(db_connection_string, pool_size=10, max_overflow=20)

with engine.connect() as conn:
    result = conn.execute(text("select * from players"))
    jobs = []
    for row in result.all():
        jobs.append(dict(row))
    print(jobs)
