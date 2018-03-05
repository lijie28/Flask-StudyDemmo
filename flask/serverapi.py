# -*- coding: utf-8 -*-
from flask import Flask ,jsonify,request
app = Flask(__name__)

log_info = {
    'un':'jie',
    'pwd':'asdf'
}

error_mes = {
    '0':'错误请求',
    '1':'没有该用户',
    '2':'密码错误',
    '3':'请输入用户名',
    '4':'请输入密码',
}
# def error_message(;code):
#     if code == 1:
#         return '没有该用户'
#     elif code == 2:
#         return
        

@app.route('/api/verify', methods = ['POST'])
def respondapi():
    if not request.form:
        return jsonify(error_mes['0'])
    if 'un' in request.form and type(request.form['un']) != unicode:
        return jsonify(error_mes['0'])
    username = request.values.get('un')
    password = request.values.get('pwd')

    if username is None or password is None:
        return jsonify(error_mes['3'])
    # if User.query.filter_by(username = username).first() is not None:
    #     abort(400) # existing user

    return jsonify({'status':'200'})

@app.route('/api/upload', methods = ['POST'])
def upload():
    
    return jsonify({'ret':200,'data':'testsuccess'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run(debug = True)