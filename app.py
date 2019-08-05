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

@app.route('/events')
def events():
    return render_template('events.html')



if __name__ == '__main__':
   app.run(debug = True)
