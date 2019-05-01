from flask_restful import Resource, Api
from app import get_api
import database.database as db

api = get_api()


class Teacher(Resource):
    def get(self, teacher_id):
        t = db.get_teacher_by_id(teacher_id)
        return { 'id': t.id, 'name': t.name, 'description': t.description, 'score': t.score }


api.add_resource(Teacher, '/api/teacher/<int:teacher_id>')
