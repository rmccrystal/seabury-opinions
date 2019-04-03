from flask import Flask, render_template, request, redirect, url_for
import comments as comment_manager
import teachers as teachers_manager
from typing import Dict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


comment_timeouts = Dict[str, int]


@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'GET':
        return render_template('comments.html', comments=comment_manager.get_comments())
    if request.method == 'POST':
        errors = list()
        if not request.form.get('title'):
            errors.append("Title does not exist")
        if not request.form.get('comment'):
            errors.append("Comment does not exist")
        if errors:
            return render_template('comments.html', comments=comment_manager.get_comments(), errors=errors)
        comment_manager.add_comment(request.form['title'], request.form['comment'])
        return redirect(url_for('comments'))


teachers_manager._init_teacher_list()


@app.route('/teachers')
def teachers():
    return render_template('teachers.html', teachers=teachers_manager.get_teachers())


if __name__ == '__main__':
    app.run()
