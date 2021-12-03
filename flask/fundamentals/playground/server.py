from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:num>')
def play2(num):
    return render_template('index2.html', times = num)

@app.route('/play/<int:num>/<string:color>')
def play3(num, color):
    return render_template('index3.html', times = num, changeColor = color)
    
if __name__=="__main__":
    app.run(debug=True)
