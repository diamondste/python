from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/')
def checker():
    return render_template('index.html', num1 = 8, num2 = 8)

@app.route('/<int:num>')
def checker2(num):
    return render_template('index.html', num1 = num, num2 = num)

@app.route('/<int:numX>/<int:numY>')
def checker3(numX, numY):
    return render_template('index.html', num1 = numX, num2 = numY)

if __name__=="__main__":
    app.run(debug=True)