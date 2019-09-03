from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
# https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-mysql-with-flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONNECTION_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # result_value = "SELECT * FROM user"

    #result = db.session.execute('INSERT INTO user VALUES(:name);', {'name': 'Mike'})
    #result = db.session.execute('SELECT * FROM user;')
    # no commit needed?

    #for r in result:
    #    print(r)
    #return "success"

    if request.method == 'POST':
        return request.form['password']
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cat')
def cat():
    return render_template('cat.html')

@app.route('/fruits')
def fruits():
    fruits = ['Apple', 'Mango', 'Orange']
    return render_template('fruits.html', fruits=fruits)

@app.route('/css')
def css():
    return render_template('css.html')

@app.errorhandler(404)
def page_not_found():
    return "This page was not found."

if __name__ == '__main__':
    app.run(debug=True, port=5000)
