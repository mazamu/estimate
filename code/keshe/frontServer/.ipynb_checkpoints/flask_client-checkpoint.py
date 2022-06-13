######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
 #     > Mail: 250919354@qq.com 
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, send_file
import sys


app = Flask(__name__)



@app.route('/test_api')
def test_api():
    #测试
    return send_file('templates/test_api.html')

@app.route('/test_json')
def test_api2():
    #测试
    return send_file('templates/json_data.html')


@app.route('/LimitDance')
def test_api3():
    #测试
    return send_file('templates/TeacherLin2.html')
@app.route('/WordBrowsing')
def test_api33():
    #测试
    return send_file('templates/TeacherLin.html')

@app.route('/test3')
def test_api4():
    #测试
    return send_file('templates/test3.html')

@app.route('/ceshi')
def test_api5():
    #测试
    return send_file('templates/ceshi.html')

@app.route('/login')
def login():
    #测试
    return send_file('templates/login.html')

@app.route('/login2')
def login2():
    #测试
    return send_file('templates/login2.html')

@app.route('/testWord')
def testWord():
    #测试
    return send_file('templates/testWord.html')

@app.route('/result')
def result():
    #测试
    return send_file('templates/result.html')

@app.route('/first')
def first():
    #测试
    return send_file('templates/first.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)

