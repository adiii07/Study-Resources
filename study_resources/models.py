from study_resources import db
from datetime import datetime

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.String, nullable=False)
    doc_name = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.doc_name}', '{self.grade}', '{self.subject}', '{self.date_posted}')"
