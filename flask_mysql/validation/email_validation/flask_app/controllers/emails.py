from flask_app import app
from flask import render_template, redirect, request 
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create/email', methods=['POST'])
def create():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template("success.html", email = Email.get_all())


# @app.route('/destroy/<int:id>')
# def destroy_email(id):
#     data = {
#         "id": id
#     }
#     Email.destroy(data)
#     return redirect('/results')