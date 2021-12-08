from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create/dojo', methods=['POST'])
def create():
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/results')
    return redirect('/')


@app.route('/results')
def result():
    return render_template("result.html", dojo=Dojo.get_last())