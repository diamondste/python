from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z0-9.+_-]+$')
class Email: 
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT into email (email) VALUES (%(email)s);"
        return connectToMySQL('emails').query_db(query, data)
    
    @classmethod
    def get_all(cls): 
        query = "SELECT * FROM email;"
        results = connectToMySQL('emails').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is not valid")
            is_valid = False
        return is_valid