from flask import Flask, render_template, request, redirect, url_for, abort
import database.database as db
from typing import Dict
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

def get_api():
    return api

import api

@app.route('/')
def index():
    return render_template('index.html')


comment_timeouts = Dict[str, int]


@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'GET':
        return render_template('comments.html', comments=db.get_comment_list())
    if request.method == 'POST':
        errors = list()
        if not request.form.get('title'):
            errors.append("Title does not exist")
        if not request.form.get('comment'):
            errors.append("Comment does not exist")
        if errors:
            return render_template('comments.html', comments=db.get_comment_list(), errors=errors)
        db.add_comment_data(request.form['title'], request.form['comment'])
        return redirect(url_for('comments'))


@app.route('/teachers')
def teachers():
    return render_template('teachers.html', teachers=db.get_teacher_list())


@app.route('/teacher/<int:teacher_id>', methods=['GET', 'POST'])
def teacher_by_id(teacher_id: int):
    if request.method == 'GET':
        t = db.get_teacher_by_id(teacher_id)
        if t:
            return render_template('teacher.html', teacher=t, comments=db.get_comment_list(teacher_id))
        else:
            abort(404)
    if request.method == 'POST':
        errors = list()
        if not request.form.get('title'):
            errors.append("Title does not exist")
        if not request.form.get('comment'):
            errors.append("Comment does not exist")
        if errors:
            t = db.get_teacher_by_id(teacher_id)
            if t:
                return render_template('teacher.html', teacher=t,
                                       comments=db.get_comment_list(teacher_id),
                                       errors=errors)
            else:
                abort(404)
        db.add_comment_data(request.form['title'], request.form['comment'], teacher_id)
        return redirect('/teacher/{}'.format(teacher_id))

if __name__ == '__main__':
    app.run()
