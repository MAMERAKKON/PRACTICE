from flask import Flask, render_template, request
import requests
from lxml import etree

app = Flask(__name__)

user_list = {}
user_list['SamShbai'] = 'ShanmuShbai0605'

@app.route('/index')
def index():
    return render_template('index.html' )

@app.route('/login')
def login():
    action = request.args.get('action')
    user = request.args.get('user')
    password = request.args.get('password')
    if action == '登录':
        if user in user_list:
            if user_list[user] == password:
                return '登录成功'
            else:
                return '密码错误'
        else:
            return '用户不存在或为空'
    else:
        if user not in user_list and user.strip() != '' and 6 <= len(password) <= 12 and password.strip() != '':
            user_list[user] = password
            return '注册成功'
        else:
            return '用户名已存在或密码不可用'



app.run(debug = True)