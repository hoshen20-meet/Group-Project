from flask import Flask, render_template
from databases import *
app = Flask(__name__)


   

@app.route('/')
def home_page():
    return render_template ("home.html" )

@app.route('/about')
def about():
	return render_template("about-us.html")

@app.route('/causes')
def causes():
    return render_template('causes.html')



if __name__ == '__main__':
   app.run(debug = True)
