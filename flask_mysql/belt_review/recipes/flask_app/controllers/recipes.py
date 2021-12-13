from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('new_recipe.html', user = User.get_one(data))

@app.route('/create/recipe', methods=['POST'])
def create():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "thirty_minute" : request.form['thirty_minute'],
        "date": request.form['thirty_minute'],
        "user_id": session["user_id"]

    }

    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    user_data = { 
        "id": session['user_id']
    }
    return render_template("edit_recipe.html", edit=Recipe.get_one(data), user = User.get_one(user_data))

@app.route('/recipe/<int:id>')
def display_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    user_data = { 
        "id": session['user_id']
    }
    return render_template("edit_recipe.html", edit=Recipe.get_one(data), user = User.get_one(user_data))

@app.route('/update/recipe', methods=['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "thirty_minute" : request.form['thirty_minute'],
        "date": request.form['thirty_minute'],
        "user_id": session["user_id"]

    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/destroy/recipe/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')