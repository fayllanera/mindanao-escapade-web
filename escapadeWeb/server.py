from flask import Flask, render_template, request, session, redirect, make_response, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from flask_cors import CORS
from base64 import b64encode
import os, requests, json

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
        return render_template("empty.html")
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('index.html')

@server.route('/writer/region')
def write_region():
    return render_template('write_region.html')

@server.route('/writer/destination')
def write_destination():
    return render_template('write_destination.html')

@server.route('/writer/attraction')
def write_attraction():
    return render_template('write_attraction.html')

@server.route('/writer')
def writer():
    return render_template('writer.html')

@server.route('/writer/submissions')
def submissions():
    submissions = requests.get('http://127.0.0.1:5000/api/writer/submissions',
                             json={"username": session['user']})
    dict = json.loads(submissions.text)
    return render_template('write_submission.html', submissions=dict['submissions'])

@server.route('/editor/submissions')
def editor_submissions():
    submissions = requests.get('http://127.0.0.1:5000/api/editor/submissions',
                             json={"username": session['user']})
    dict = json.loads(submissions.text)
    return render_template('editor_submissions.html', submissions=dict['submissions'])

@server.route('/editor/edit', methods=['POST'])
def editor_edit():
    write = request.form['write']
    print(write)
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    return render_template('editor_view.html', submission=dict['submission'][0])

@server.route('/edit', methods=['POST'])
def edit_region():
    write = request.form['write']
    print(write)
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit',
                               json={"username": session['user'], "write_id": write})
    print(submission)
    dict = json.loads(submission.text)
    print(dict)
    return render_template('region_edit.html', submission=dict['submission'][0])

@server.route('/upload', methods=['POST', 'GET'])
def upload_photo():
    file = request.files['qqfile']
    response = requests.post('http://127.0.0.1:5000/api/writer/upload',
                             json={"username": session['user'], "filename": b64encode(file.read())})
    print(file)
    return jsonify({'success': 'true'})

@server.route('/delete', methods=['POST', 'GET'])
def delete_photo():
    file = request.files['qqfile']
    response = requests.post('http://127.0.0.1:5000/api/writer/delete',
                             json={"username": session['user'], "filename": b64encode(file.read())})
    print(file)
    return jsonify({'success': 'true'})


CORS(server)
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['USE_SESSION_FOR_NEXT'] = True
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'
dc = SQLAlchemy(server)
server.secret_key = os.urandom(24)

if __name__=='__main__':
    server.run(host='localhost', port=8000, debug=True)
