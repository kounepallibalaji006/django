from flask import Flask ,render_template , request , jsonify
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model) :
        id =  db.Column(db.Integer, primary_key=True)
        book = db.Column(db.String(100), nullable=False)
        author = db.Column(db.String(100), nullable=False)
        price = db.Column(db.Float, nullable=False)
        
        def to_dict(self) :
                return {
                        "id" : self.id,
                        "book" : self.book,
                        "author" : self.author,
                        "price" : self.price
                }

with app.app_context() :
        db.create_all()

        


@app.route('/home/')


def home():
    name ="wanda witch"
    context ={"name":name}
    return  render_template("homepage.html",**context)

@app.route('/contactus/')

def contactus():
    name ="contactpage"
    age=35
    context = {
        "name":name,
        "age": age
    }
    return render_template("contactuspage.html",**context)

@app.route('/aboutus/')

def aboutus():
    name ="virat"
    age =17
    
    context ={
        "name":name,
        "age":age,
        
    }
    return render_template("aboutuspage.html",**context)


@app.route("/")
def master():
    return render_template("master.html")
#api end points

@app.route('/api/books')
def get_books():
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books])
        



@app.route('/api/books' , methods=['POST',])
def add_book():
        data = request.get_json()
        new_book = Book(id = data['id'], book=data['book'], author=data['author'], price= data['price'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201
        


if __name__=="__main__":
    app.run(debug=True)