from flask import Flask, render_template,request

app = Flask(__name__)

data = [{'id': 0, 'name': '爱莲', 'count': 0}, {'id': 1, 'name': '朱鸢', 'count': 0},
        {'id': 2, 'name': '青衣', 'count': 0}, {'id': 3, 'name': '简杜', 'count': 0}]

@app.route('/index')
def index():
    return render_template('index.html', data = data)

@app.route('/like')
def like():
    id = request.args.get('id')
    print(f'想要给{data[int(id)]['name']}点赞')

    data[int(id)]['count'] += 1
    return render_template('index.html', data = data)
app.run(debug=True)