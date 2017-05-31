from flask import Flask, jsonify, abort, make_response
from flask import request


app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug = True)
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
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
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





        