from flask import Flask, render_template, request, redirect, url_for,jsonify
from models.jobs import Job
from config import db, app


# create a route to display and submit a job form
@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    if request.method == 'POST':
        # get the job data from the form
        job_title = request.form['job_title']
        job_location = request.form['job_location']
        job_description = request.form['job_description']
        job_required_skills = request.form['job_required_skills']
        job_required_experience = request.form['job_required_experience']
        job_salary = request.form['job_salary']

        # create a new Job object with the form data
        new_job = Job(
            job_title=job_title,
            job_location=job_location,
            job_description=job_description,
            job_required_skills=job_required_skills,
            job_required_experience=job_required_experience,
            job_salary=job_salary
        )

        # add the new job to the database
        db.session.add(new_job)
        db.session.commit()
        return jsonify({"message": "Job post added succesfully"}), 201


        # redirect to the jobs list page
        #return redirect(url_for('index.html'))

    # if the request method is GET, render the job form
    return render_template('index.html')


'''get a job by id'''
@app.route("/jobs/<int:id>")
def get_job(id):
    job = Job.query.get_or_404(id)
    return render_template('jobPage.html', job=job)


'''apply for a job'''    
@app.route("/jobs/<int:id>/apply", methods=['POST'])
def apply_job(id):
    data = request.form
    return jsonify(data)