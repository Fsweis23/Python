from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Sports:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.teams = data['teams']
        self.players = data['players']
        self.stats = data['stats']
        self.scores = data['scores']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO sports (teams, players, stats, scores, text, user_id) VALUES (%(teams)s, %(players)s, %(stats)s, %(scores)s, %(text)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sports JOIN users on sports.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_sports = []
            for row in results:
                this_sport = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                this_user = user_model.User(user_data)
                this_sport.planner = this_user
                all_sports.append(this_sport)
            return all_sports
        return[]

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sports WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM sports JOIN users on users.id = sports.user_id WHERE sports.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_sport = cls(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['created_at'],
            'updated_at': row['updated_at']
        }
        planner = user_model.User(user_data)
        this_sport.planner = planner
        return this_sport
    
    @classmethod
    def update(cls, data):
        query = "UPDATE sports SET teams = %(teams)s, players = %(players)s, stats = %(stats)s, scores = %(scores)s, text = %(text)s WHERE id = %(id)s AND user_id = %(user_id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['teams']) < 1:
            flash("teams required")
            is_valid = False
        if len(form_data['players']) < 1:
            flash("players required")
            is_valid = False
        if len(form_data['stats']) < 1:
            flash("stats required")
            is_valid = False
        if len(form_data['scores']) < 1:
            flash("scores required")
            is_valid = False
        if len(form_data['text']) < 1:
            flash("text required")
            is_valid = False
        return is_valid