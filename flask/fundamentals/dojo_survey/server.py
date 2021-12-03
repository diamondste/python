from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'shhhh...secret'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    print("Got Post Info")
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomments'] = request.form['comments']
    return redirect('/result')

@app.route("/result")
def show_user():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)