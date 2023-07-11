from flask import Flask, render_template, url_for
from config import app, db
from models.jobs import Job
from routes import job_r, auth



''' create the database'''
with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/home")
def home():
    jobs = Job.query.all()
    return render_template('/index.html', jobs=jobs)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)