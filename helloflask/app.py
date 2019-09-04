from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

'''
app.config.update(
    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:topsecret@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)
'''

db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask!'

@app.route('/new')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1>the greeting is: {0} </h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def no_query_string(name='Justine'):
    return '<h1>hello there ! {} </h1>'.format(name)

# Strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> there is a string: {} </h1>'.format(name)

# Numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: {} </h1>'.format(num)

# Numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is: {}</h1>'.format(num1 + num2)

# Floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is: {}</h1>'.format(num1 * num2)

# Using templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')

# Jinja templates
@app.route('/watch')
def top_movies():
    movie_list = [
        'Autopsy of jane doe',
        'Ghost in the shell',
        'Kong: Skull Island',
        'John Wick 2',
        'Spiderman - Homecoming'
    ]

    return render_template('movies.html',
                           movies=movie_list,
                           name="Christoph")

@app.route('/tables')
def movies_plus():
    movie_dict = {
        'Autopsy of jane doe': 2.14,
        'Ghost in the shell': 3.20,
        'Kong: Skull Island': 1.50,
        'John Wick 2': 02.52,
        'Spiderman - Homecoming': 1.48,
    }

    return render_template('table_data.html',
                           movies=movie_dict,
                           name="Christoph")


@app.route('/filters')
def filter_data():
    movie_dict = {
        'Autopsy of jane doe': 2.14,
        'Ghost in the shell': 3.20,
        'Kong: Skull Island': 1.50,
        'John Wick 2': 02.52,
        'Spiderman - Homecoming': 1.48,
    }

    return render_template('filter_data.html',
                           movies=movie_dict,
                           name=None,
                           movie='a christmas carol')

@app.route('/macros')
def jinja_macros():
    movie_dict = {
        'Autopsy of jane doe': 2.14,
        'Ghost in the shell': 3.20,
        'Kong: Skull Island': 1.50,
        'John Wick 2': 02.52,
        'Spiderman - Homecoming': 1.48,
    }

    return render_template('using_macros.html', movies=movie_dict)

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, name is {}'.format(self.id, self.name)

if __name__ == "__main__":
    # create all tables only if they do not exist
    db.create_all()
    app.run(debug=True)
