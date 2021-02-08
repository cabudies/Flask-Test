
from flask import Flask, render_template, request

app = Flask(__name__)

dict_name = {
    1:'Mr Ved',
    2:'Miss Sunita',
    3:'Mr Suraj',
    4:'Miss Anjali',
    5:'Miss Madhu',
    6:'Miss Rosy',
    7:'Mr Dev',
    8:'Mr S.K.Jha',
    9:'Miss Ranjana',
    10:'Mr Akhilesh',
    11:'Mr Rakesh',
    12:'Miss Nisha'
}

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/home_page", methods=['POST'])
def profile():
    if request.method == 'POST':
        data = request.form
        name = data['username']
        password = data['password']

        details = {
            'name':name,
            'password':password
        }

        if ((name == 'rajat')&(password == '123456')):
            return render_template('home_page.html')

@app.route("/data_display", methods=['POST'])
def data_display():
    if request.method == 'POST':
        data = request.form
        id = data['id']
        name = data['name']
        cls = data['class']
        teacher = dict_name[int(cls)]

        details = {
            'name':name,
            'class':cls,
            'id':id,
            'teacher':teacher
        }

        return render_template('data_display.html', data=details)

if __name__ == "__main__":
    app.run(debug=True)
