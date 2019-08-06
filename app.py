from flask import Flask, render_template, request
from databases import *
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


   

@app.route('/')
def home_page():
    print(query_all_books())
    return render_template ("home.html" )

@app.route('/about')
def about():
	return render_template("about-us.html")

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/staff')
def events():
    return render_template('staff.html')

@app.route('/event-details')
def event_details():
    return render_template('event-details.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/single-blog')
def singlr_blog():
    return render_template('single-blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/log_in',methods=['POST','GET'])
def log_in():
    if request.method == "GET":
        return render_template ("log_in.html" )
    else:
        name = request.form['uname']
        password = request.form['psw']
        if name == 'admin' and password== 'rebooks123':
            return render_template('add_book.html')
        else:
            return render_template ("log_in.html",wrong=True )

    return render_template ("log_in.html" )

    
@app.route('/add_book',methods=['POST','GET'])
def add_books():
    if request.method == "GET":
        return render_template ("add_book.html" )
    else:
        bookname=request.form['bookname']
        authorname=request.form['authorname']
        price=request.form['price']
        print(request.files)
        f = request.files['bookpic']
        f.save("static/img/"+f.filename)
        add_book(bookname,authorname, price, f.filename)
        return render_template("store.html")



if __name__ == '__main__':
   app.run(debug = True)



