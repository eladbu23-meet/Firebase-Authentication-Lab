from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config= {

  "apiKey": "AIzaSyB3F7qLE9YWCgiou0k-646kRhq6ZJiasc4",

  "authDomain": "first-fire-base-a6cbb.firebaseapp.com",

  "projectId": "first-fire-base-a6cbb", 

  "storageBucket": "first-fire-base-a6cbb.appspot.com",

  "messagingSenderId": "247748858218",

  "appId": "1:247748858218:web:c9a45efae841ad7b9fd513",
  "measurementId": "G-YHYMEQKXMP",
    "databaseURL": ""
    }

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()    

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")
    if request.methods== "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('/add_tweet'))
        except:
            error = "ajj"
        return render_template("signin.html")
           


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.methods== "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
                    
            return redirect(url_for('/add_tweet'))
        except:
           error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)