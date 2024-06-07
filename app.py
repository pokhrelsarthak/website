from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Science',
        'location': 'Delhi, India',
        'salary': '1,10,000'
    },
    {
        'id': 2,
        'title': 'Data Management',
        'location': 'Punjab, India',
        'salary': '1,22,000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': '1,00,000'
    },
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
