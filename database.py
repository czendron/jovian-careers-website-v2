from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
      "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
      }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    jobs = []    
    for row in result.all():
      jobs.append(dict(zip(column_names, row)))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = {id}")
    )
    column_names = result.keys()
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(zip(column_names, rows[0]))
