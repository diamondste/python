from flask_app.config.mysqlconnection import connectToMySQL
from .recipe import Recipe
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z0-9.+_-]+$')
from flask import flash 
class User: 
    db = "recipes"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES(%(first_name)s , %(last_name)s , %(email)s , %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)

        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate(user):
        is_valid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invaild Email", "register")
            is_valid = False 
        if len(user['first_name']) < 2:
            is_valid = False 
            flash("Last  Name must be at least 2 characters." , "register")
        if len(user['last_name']) < 2:
            is_valid = False 
            flash("Last Name must be at least 2 characters.", "register")
        if len(user['password']) < 2:
            is_valid = False 
            flash("Password must be at least 8 characters.", "register")
        if user['password'] != user['confirm']: 
            flash("Password doesn't match", "register")
        return is_valid