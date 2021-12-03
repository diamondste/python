from flask import Flask
app = Flask(__name__) 
@app.route('/') 
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    print(name)
    return 'Hi ' + name + '!'

# @app.route('/say/<name>')
# def say_name(name):
#     return f"Hi {name.capitalize()}!"
@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    x = int(num)
    y = str(word)
    print(y)
    return y * x

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     output = ''

#     for i in range(0,num):
#         output += f"<p>{word}</p>"

#     return output

if __name__=="__main__":
    app.run(debug=True)
