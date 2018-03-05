# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, url_for, request
# from flask import request 
from flask.ext.restful import Api, Resource
from flask.ext.restful import reqparse
from passlib.apps import custom_app_context as pwd_context

from flask.ext.sqlalchemy import SQLAlchemy
# from flask.db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))
        # ...

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


@app.route('/api/users', methods = ['POST'])
def new_user():
        
    if not request.form:
        abort(400)
    if 'username' in request.form and type(request.form['username']) != unicode:
        abort(400)
    username = request.values.get('username')
    password = request.values.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}



class TaskListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
            help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListAPI, self).__init__()

    # ...

class TaskAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()


# with app.request_context(environ):
#     assert request.method == 'POST'

# @app.route('/')
# def index():
#     username = request.cookies.get('username')


tasks = [
  {
      'id': 1,
      'title': u'Buy groceries',
      'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
      'done': False
  },
  {
      'id': 2,
      'title': u'Learn Python',
      'description': u'Need to find a good Python tutorial on the web',
      'done': False
  },
]

@app.route('/todo/tasks', methods = ['POST', 'GET'])
def get_tasks():
    if request.method == 'POST':
        return jsonify({'tasks': tasks})

# if __name__ == '__main__':
#   app.run(debug = True)

@app.route('/todo/tasks/<int:task_id>', methods = ['POST', 'GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/')
def index():
    return 'Index Page ha'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/login', methods=['POST', 'GET'])
def login():
    print 'test'
    error = None
    if request.method == 'POST':
        print 'haha'
        if valid_login(request.form['user'],
                       request.form['pwd']):
            return log_the_user_in(request.form['user'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')




if __name__ == '__main__':
    app.run(debug = True)