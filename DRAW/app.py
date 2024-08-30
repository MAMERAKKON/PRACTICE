''' 让我们的电脑可以支持服务访问
需要一个web框架
pip install Flask '''
from random import randint, uniform

from flask import Flask, render_template

app = Flask(__name__)

hero = []
with open('zzzhero.text', 'r', encoding='utf-8') as f:
    for line in f:
        hero.append(line.strip())

heroA = hero
heroS = []
while True:
    heroS.append(heroA[0])
    heroA.remove(heroA[0])
    if heroA[0] == '苍角':
        break

weapon = []
with open('zzzweapon', 'r', encoding='utf-8') as f:
    for line in f:
        weapon.append(line.strip())

weaponB = weapon
weaponA = []
weaponS = []
while True:
    weaponS.append(weaponB[0])
    weaponB.remove(weaponB[0])
    if weaponB[0] == '啜泣摇篮':
        break
while True:
    weaponA.append(weaponB[0])
    weaponB.remove(weaponB[0])
    if weaponB[0] == '「湍流」-铳型':
        break

alllist = weaponS + heroS + heroA + weaponA + weaponB
Alist = heroA + weaponA
Slist = heroS + weaponS
prob = [0.6, 7.8]

heroStrS = ''
for heros in heroS:
    heroStrS += heros + ' '
heroStrS += '\n'

heroStrA = ''
for heros in heroA:
    heroStrA += heros + ' '
heroStrA += '\n'

weaponStrS = ''
for weapons in weaponS:
    weaponStrS += weapons + ' '
weaponStrS += '\n'

weaponStrA = ''
for weapons in weaponA:
    weaponStrA += weapons + ' '
weaponStrA += '\n'

weaponStrB = ''
for weapons in weaponB:
    weaponStrB += weapons + ' '
weaponStrB += '\n'

allString = heroStrS + heroStrA + weaponStrS + weaponStrA + weaponStrB

@app.route('/index')
def index():
    return render_template('index.html', herolistS = heroStrS, herolistA = heroStrA, weaponlistS = weaponStrS,
                           weaponlistA = weaponStrA, weaponlistB = weaponStrB)

@app.route('/choujiang')
def choujiang():
    p = uniform(0,100)
    if prob[0]<= p < prob[1]:
        id = randint(0, len(Alist)-1)
        return render_template('index.html', herolistS = heroStrS, herolistA = heroStrA, weaponlistS = weaponStrS,
                           weaponlistA = weaponStrA, weaponlistB = weaponStrB, get = Alist[id])
    elif p < prob[0]:
        id = randint(0, len(Slist)-1)
        return render_template('index.html', herolistS = heroStrS, herolistA = heroStrA, weaponlistS = weaponStrS,
                           weaponlistA = weaponStrA, weaponlistB = weaponStrB, get = Slist[id])
    else:
        id = randint(0, len(weaponB)-1)
        return render_template('index.html', herolistS = heroStrS, herolistA = heroStrA, weaponlistS = weaponStrS,
                           weaponlistA = weaponStrA, weaponlistB = weaponStrB, get = weaponB[id])

@app.route('/shilian')
def shilian():
    idlist = []
    bcount = 0
    notbcount = 0
    for i in range(10):
        p = uniform(0, 100)
        if prob[0] <= p < prob[1]:
            id = randint(0, len(Alist) - 1)
            idlist.append(str(i+1) + ':' +Alist[id])
            notbcount += 1
        elif p < prob[0]:
            id = randint(0, len(Slist) - 1)
            idlist.append(str(i+1) + ':' +Slist[id])
            notbcount += 1
        else:
            id = randint(0, len(weaponB) - 1)
            idlist.append(str(i+1) + ':' +weaponB[id])
            bcount += 1
        if bcount == 9 and notbcount == 0:
            p = uniform(0, 7.8)
            if prob[0] <= p < prob[1]:
                id = randint(0, len(Alist) - 1)
                idlist.append(str(i+2) + ':' +Alist[id])
            else:
                id = randint(0, len(Slist) - 1)
                idlist.append(str(i+2) + ':' + Slist[id])
            break
    return render_template('index.html', herolistS = heroStrS, herolistA = heroStrA, weaponlistS = weaponStrS,
                           weaponlistA = weaponStrA, weaponlistB = weaponStrB, get=idlist)



app.run(debug = True)