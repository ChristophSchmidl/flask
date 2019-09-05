from flask import Flask, request, render_template, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import click

'''
Request decorators

@app.before_request
@app.before_first_request
@app.after_request
@app.teardown_request
'''

app = Flask(__name__)

app.config.update(
    SECRET_KEY='mysecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:mysecret@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

db = SQLAlchemy(app)

@app.before_request
def some_function():
    g.string = '<br> This code ran before any request'

@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask!' + g.string

@app.route('/new')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1>the greeting is: {0} </h1> {1}'.format(query_val, g.string)

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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'The name is {}'.format(self.name)

class Book(db.Model):
    __tablename_ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship: one-to-many
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)

@app.cli.command("seed-db")
def seed_db():
    """Creating some samples."""
    print("seed-db")
    p1 = Publication("Oxford Publications")
    p2 = Publication("Paramount Press")
    p3 = Publication("Oracle Books Inc")
    p4 = Publication("Vintage Books and Comics")
    p5 = Publication("Trolls Press")
    p6 = Publication("Broadway Press")
    p7 = Publication("Downhill Publishers")
    p8 = Publication("Kingfisher Inc")
    db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8])

    b1 = Book("Miky's Delivery Service", "William Dobelli", 3.9, "ePub", "broom-145379.svg", 123, 1)
    b2 = Book("The Secret Life of Walter Kitty", "Kitty Stiller", 4.1, "Hardcover", "cat-150306.svg", 133, 1)
    b3 = Book("The Empty Book of Life", "Roy Williamson", 4.2, "eBook", "book-life-34063.svg", 153, 1)
    b4 = Book("Life After Dealth", "Nikita Kimmel", 3.8, "Paperback", "mummy-146868.svg", 175, 2)
    b5 = Book("The Legend of Dracula", "Charles Rowling", 4.6, "Hardcover", "man-37603.svg", 253, 2)
    b6 = Book("Taming Dragons", "James Vonnegut", 4.5, "MassMarket Paperback", "dragon-23164.svg", 229, 2)
    b7 = Book("The Singing Magpie", "Oscar Steinbeck", 5, "Hardcover", "magpie-147852.svg", 188, 3)
    b8 = Book("Mr. Incognito", "Amelia Funke", 4.2, "Hardcover", "incognito-160143.svg", 205, 3)
    b9 = Book("A Dog without purpose", "Edgar Dahl", 4.8, "MassMarket Paperback", "dog-159271.svg", 300, 4)
    b10 = Book("A Frog's Life", "Herman Capote", 3.9, "MassMarket Paperback", "amphibian-150342.svg", 190, 4)
    b11 = Book("Logan Returns", "Margaret Elliot", 4.6, "Hardcover", "wolf-153648.svg", 279, 5)
    b12 = Book("Thieves of Kaalapani", "Mohit Gustav", 4.1, "Paperback", "boat-1296201.svg", 270, 5)
    b13 = Book("As Men Thinketh", "Edward McPhee", 4.5, "Paperback", "cranium-2028555.svg", 124, 6)
    b14 = Book("Mathematics of Music", "Mary Turing", 4.5, "Hardcover", "music-306008.svg", 120, 6)
    b15 = Book("The Mystery of Mandalas", "Jack Morrison", 4.2, "Paperback", "mandala-1817599.svg", 221, 6)
    b16 = Book("The Sacred Book of Kairo", "Heidi Zimmerman", 3.8, "ePub", "book-1294676.svg", 134, 7)
    b17 = Book("Love is forever, As Long as it lasts", "Kovi O'Hara", 4.5, "Hardcover", "love-2026554.svg", 279, 8)
    b18 = Book("Order in Chaos", "Wendy Sherman", 3.5, "MassMarket Paperback", "chaos-1769656.svg", 140, 8)
    db.session.add_all([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18])
    db.session.commit()

if __name__ == "__main__":
    '''
    try:
        db.session.execute("SELECT 1")
        print('<h1>It works.</h1>')
    except:
        print('<h1>Something went wrong</h1>')
    '''

    # create all tables only if they do not exist
    db.create_all()

    #pub1 = Publication(2, 'Christoph Master Thesis')
    #db.session.add(pub1)
    #db.session.add_ll([pub1, pub2, pub3])
    #db.session.commit()

    app.run(debug=True)
