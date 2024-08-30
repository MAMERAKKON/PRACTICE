# 发送请求的地址
from flask import Flask, render_template, request
from lxml import etree
import requests



def get_number(number):

    url = f'https://www.haojixiong.com/shouji/{number}.html'
    # 发送请求

    from flask import Flask,render_template

    # 伪装
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    # 发送请求
    resp = requests.get(url, headers = headers)
    # 解析响应
    e = etree.HTML(resp.text)

    datas = e.xpath('//tr/td/span/a/text()')
    table = e.xpath('//tr/td/span/text()')
    data = {}
    data['手机号'] = str(number)
    data['手机号码归属地'] = str(datas[0]) + str(table[-3])
    data['手机区号'] = str(datas[1])
    data['归属地邮编'] = str(datas[2])
    data[table[0][:-1]] = str(table[1])
    data[table[2][:-1]] = str(table[3])
    data[table[4][:-1]] = str(table[5])
    data[table[6][:-1]] = str(table[7])
    data[table[8][:-1]] = str(table[9])
    data[table[10][:-1]] = str(table[11])
    data[table[12][:-1]] = str(table[13])
    data[table[14][:-1]] = str(table[15])
    zhouyi_yunshi = ''
    i = 0
    while True:
        zhouyi_yunshi += str(table[17 + i])
        i += 1
        if table[17 + i] == '周易详情：':
            break
    data[table[16][:-1]] = zhouyi_yunshi
    next_key = 17 + i
    zhouyi_xiangqing = ''
    n = 1
    while True:
        zhouyi_xiangqing += str(table[next_key + n])
        n += 1
        if table[next_key + n] == '手机号码归属地：':
            break
    data[table[next_key][:-1]] = zhouyi_xiangqing
    print(data)
    return data
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    number = request.args.get('number')
    if len(number) != 11:
        return '号码有误'
    data = get_number(number)
    return render_template('/index.html', data = data)

app.run(debug = True)