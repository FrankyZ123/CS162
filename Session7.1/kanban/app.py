from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/frankyz123/Code/Minerva/JuniorSpring/CS162/personalrepo/Session7.1/kanban/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/')
def home():
    todos = Todo.query.filter_by(complete=False).all()
    todones = Todo.query.filter_by(complete=True).all()
    return render_template('home.html', todos=todos, todones=todones)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['task'], complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/done', methods=['POST'])
def done():
    Todo.query.filter_by(id=request.form['todo']).first().complete = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete', methods=['POST'])
def delete():
    todone = Todo.query.filter_by(id=request.form['todone']).first()
    db.session.delete(todone)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)