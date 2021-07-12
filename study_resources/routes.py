from flask import render_template, url_for, redirect, flash, request, send_file
from study_resources import app, db
from study_resources.forms import DownloadForm, UploadForm
from study_resources.models import File
from io import BytesIO


@app.route("/", methods=['GET', 'POST'])
def home():
	download_form = DownloadForm()
	upload_form = UploadForm()
	if upload_form.validate_on_submit():
		uploaded_file = request.files['file']
		if uploaded_file.filename == '':
			flash('No file select. Try again', 'danger')
			return redirect(url_for('home'))
		file = File(document=uploaded_file.read(), doc_name=upload_form.file_name.data, 
                                                 grade=upload_form.grade.data, subject=upload_form.subject.data)
		db.session.add(file)
		db.session.commit()
		flash('Post created', 'success')
		return redirect(url_for('home'))
	if request.method == 'POST' and download_form.validate():
		return redirect(url_for('downloads_page', grade=download_form.grade.data, subject=download_form.subject.data))
	return render_template('home.html', form=upload_form, download_form=download_form)

@app.route("/downloadpage/<int:grade>/<subject>/", methods=['GET', 'POST'])
def downloads_page(grade, subject):
	global files
	files = File.query.filter_by(grade=grade, subject=subject).all()
	files_len = len(files)
	return render_template('down_files.html', files = files, files_len=files_len, grade=grade, subject=subject)

@app.route("/download/<int:i>/")
def download_file(i):
    return send_file(BytesIO(files[i].document),
            attachment_filename=files[i].doc_name, as_attachment=True)

@app.route("/about/")
def about():
    return render_template('about.html')
