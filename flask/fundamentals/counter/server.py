from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "counting"
@app.route('/')
def counter():
    if 'counts' in session:
        session['counts'] += 1
    else:
        session['counts'] = 0

    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)