from flask import Flask, render_template, request, session, redirect, make_response, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from flask_cors import CORS
import os

server = Flask(__name__)


@server.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print ('b')
        session.pop('user', None)
        session['user'] = request.form['username']
        print session['user']
        print request.form['stat']
        print request.form['roleid']
        
        if request.form['roleid'] == '2':
            print ('succ')
            return redirect('adminpage')
           
    return render_template("index.html")

@server.route('/logout')
def logout():
    if session['user'] is None:
        session.pop('user', None)
        return redirect('index')
    else:
        session.pop('user', None)
        print ('popped!')
        return redirect('index')



@server.route('/register', methods=['GET','POST'])
def register():
    return render_template("signup.html")

@server.route('/admin/landing', methods=['GET'])
def landing_admin():
    if 'user' in session:
        return render_template("timeline.html")
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('index.html')





CORS(server)
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dc = SQLAlchemy(server)
server.config['USE_SESSION_FOR_NEXT'] = True
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'

server.secret_key = os.urandom(24)

if __name__=='__main__':
    server.run(host='localhost', port=8000, debug=True)
