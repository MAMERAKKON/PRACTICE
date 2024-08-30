import string
import sys
from random import randint


code_list = list(string.ascii_letters)
code = ''
for i in range(10):
    code_list.append(str(i))
with open('CODE','w') as c:
    for i in range(6):
        code += code_list[randint(0,len(code_list))]
    c.write(code)

info = '''这是一个学生系统，请输入对应数字启用功能：
1. 查询学生列表
2. 查询学生成绩
3. 录入学生成绩
4. 查询学生信息
5. 学生签到
6. 查询学生出勤状态
7. 转学操作
0. 退出登录
-. 退出系统
--------------------------------------------------------'''
student = {'1':'张三','2':'李四','3':'王五','4':'悟空','5':'悟能','6':'悟净','7':'玄奘'}
score = {'1':[100,90,90],'2':[80,90,70],'3':[0,50,20],'4':[80,70,90],'5':[100,100,90],'6':[90,90,90],'7':[80,80,80]}

def action1():
    print(student)

def action2():
    id = input('请输入学生学号，返回请按0：')
    if id == '0':
        choose_action()
    Chi = score[id][0]
    Mat = score[id][1]
    Eng = score[id][2]
    print('学生的成绩是：语文：' + str(Chi) + '分，数学：' + str(Mat) +'分，英语：' + str(Eng) + '分。')

def if_score(mark):
    while not 0 <= int(mark) <= 100:
        mark = input('您输入的分数有误，请重新输入：')
    return mark


def action3():
    id = input('请输入学生学号，返回请按0：')
    if id == '0':
        choose_action()
    input_score(id)

def input_score(id):
    act = 1
    while not act == '0':
        act = input('请输入要录入的科目，返回请按0：')
        if act == 'Chi':
            Chi = if_score(input('请输入分数：'))
            score[id][0] = int(Chi)
            print('录入成功，' + student[id] + '的语文成绩为：' + str(Chi))
        elif act == 'Mat':
            Mat = if_score(input('请输入分数：'))
            score[id][1] = int(Mat)
            print('录入成功，' + student[id] + '的数学成绩为：' + str(Mat))
        elif act == 'Eng':
            Eng = if_score(input('请输入分数：'))
            score[id][2] = int(Eng)
            print('录入成功，' + student[id] + '的英语成绩为：' + str(Eng))
        elif act == '0':
            action3()
        else:
            print('您输入的科目有误，请核对')



def choose_action():
    print(info)
    action = input('请选择您需要的操作:')
    while True:
        if action == '1':
            action1()
        elif action == '2':
            action2()
        elif action == '3':
            action3()
        elif action == '0':
            login()
        elif action == '-':
            sys.exit()




def register():
    user = input('请输入用户名：')
    password = input('请输入密码：')
    with open('TUTOR','a') as a:
        a.write(user + ',' + password + '\n')
    print('注册成功，请登录。')
    login()

def login():
    log = False
    user_list = []
    password_list = []
    with open('TUTOR', 'r') as a:
        for i in a:
            user = i[:i.find(',')].strip()
            password = i[i.find(',') + 1:].strip()
            user_list.append(user)
            password_list.append(password)
    while not log:
        user = input('''
欢迎使用教师系统v1.0,
请先登录，
如需注册请按0，
如需退出系统请按-，
--------------------------------------------------------
请输入您的教师账号：''')
        if user == '0':
            register()
        if user in user_list:
            i = user_list.index(user)
            password = input('请输入您的密码：')
            if password == password_list[i]:
                log = True
                choose_action()
            else:
                print('您的密码有误。')
        else:
                print('用户名不存在。')





login()