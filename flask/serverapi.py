# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for ,jsonify
from werkzeug.utils import secure_filename
import os

import sys   
reload(sys) 
sys.setdefaultencoding('utf8')  

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

# @app.route('/api/upload', methods = ['POST'])
# def upload():
    
#     return jsonify({'ret':200,'data':'testsuccess'})


@app.route('/api/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        try:
            f = request.files['file']
            basepath = os.path.dirname(__file__)  # 当前文件所在路径
            # print '当前路径',basepath
            upload_path = os.path.join(basepath, 'static/uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
            f.save(upload_path)
            return jsonify({
                'ret':200,
                'data':'获取文件成功'
            })
        except Exception as e:
            print 'fail:',e
            return jsonify({
                'ret':2001,
                'data':'获取文件失败'
            })
        
        # return redirect(url_for('/api/upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run(debug = True)