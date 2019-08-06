from flask import Flask, render_template
from databases import *
app = Flask(__name__)


   

@app.route('/')
def home_page():
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


@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/log_in')
def log_in():
    return render_template ("log_in.html" )

if __name__ == '__main__':
   app.run(debug = True)
