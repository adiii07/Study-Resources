from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file_name = StringField('File name', validators=[DataRequired()])
    grade = SelectField('Grade', validators=[DataRequired()], choices=['9', '10', '11', '12'])
    subject = SelectField('Subject', validators=[DataRequired()], choices=['Mathematics', 'Science', 'Social Science', 'English', 'Hindi', 
                                                                                                                        'Physics', 'Chemistry', 'Biology', 'Computer Science'])
    submit = SubmitField("Upload")

class DownloadForm(FlaskForm):
    grade = SelectField('Grade', validators=[DataRequired()], choices=['9', '10', '11', '12'])
    subject = SelectField('Subject', validators=[DataRequired()], choices=['Mathematics', 'Science', 'Social Science', 'English', 'Hindi',
                                                                                                                        'Physics', 'Chemistry', 'Biology', 'Computer Science'])
    submit = SubmitField("Get Files")