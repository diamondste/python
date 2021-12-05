from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)
@app.route("/users")
def index(): 
    users = User.get_all()
    print(users)
    return render_template("display.html", all_users = users)

@app.route('/users/new', methods=["POST"])
def new_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "ema": request.form["ema"]
    }

    User.save(data)

    return redirect('/users')

if __name__ == "__main__": 
    app.run(debug=True)