from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe: 

    db = "recipes"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.thirty_minute = data['thirty_minute']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date, thirty_minute, user_id) VALUES(%(name)s , %(description)s , %(instructions)s , %(date)s , %(thirty_minute)s , %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            print(row['date'])
            recipes.append(cls(row))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s , description = %(description)s , instructions = %(instructions)s, date = %(date)s, thirty_minute = %(thirty_minute)s , updated_at= NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False 
            flash("Name must be at least 3 characters." , "recipe")
        if len(recipe['description']) < 3:
            is_valid = False 
            flash("Description must be at least 2 characters.", "recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False 
            flash("Instructions must be at least 3 characters.", "recipe")
        if recipe['date'] == "": 
            flash("Please enter a date", "recipe")
        return is_valid