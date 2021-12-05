from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users(): 
    return render_template("display.html", users = User.get_all())


@app.route('/users/new')
def new_user():
    return render_template("new.html")

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__ == "__main__": 
    app.run(debug=True)