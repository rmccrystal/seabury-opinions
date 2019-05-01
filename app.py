from flask import Flask, render_template, request, redirect, url_for
import database.database as db
from typing import Dict

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
