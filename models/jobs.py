from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db, app



class Job(db.Model):
    __tablename__ = "job"

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(50), nullable=False)
    job_location = db.Column(db.String(25), nullable=False)
    job_description = db.Column(db.Text(), nullable=False)
    job_required_skills = db.Column(db.Text(), nullable=False)
    job_required_experience = db.Column(db.String(100), nullable=False)
    job_salary = db.Column(db.String(25), nullable=False)
    job_created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


    def to_dict(self):
        return {'id' : self.id, 'job_title' : self.job_title, 'job_location' : self.job_location,
                'job_description' : self.job_description, 'job_required_skills' : self.job_required_skills,
                'job_required_experience' : self.job_required_experience, 'job_salary' : self.job_salary,
                'job_created_at' : self.job_created_at
        }
    
