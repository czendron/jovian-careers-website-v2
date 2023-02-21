from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'USD 80,000' 
  },
  {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Sao Paulo, Brazil',
  'salary': 'USD 120,000' 
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Product Manager',
    'location': 'Remote',
    'salary': 'USD 131,000' 
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
