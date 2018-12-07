from flask import Flask, render_template, request, session, redirect, make_response, url_for, flash, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from flask_cors import CORS
from base64 import b64encode
import os, requests, json

server = Flask(__name__)


@server.route('/', methods=['GET','POST'])
def index():
    submissions = requests.get('http://127.0.0.1:5000/get_posted')
    dict = json.loads(submissions.text)
    return render_template("landing_page.html", posts=dict['submissions'])

@server.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@server.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print('pop')
        session.pop('user', None)
        session['user'] = request.form['username']
        print 'pop'
        print session['user']
        g.user = session['user']
        return redirect('#')


@server.route('/logout')
def logout():
    if session['user'] is None:
        session.pop('user', None)
        return redirect('/')
    else:
        session.pop('user', None)
        print ('popped!')
        return redirect('/')


@server.route('/region/<name>', methods=['GET'])
def view_region(name):
    post = requests.get('http://127.0.0.1:5000/get/region',
                               json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('view_post.html', post=post_dict['post'][0])

@server.route('/destination/<name>', methods=['GET'])
def view_destination(name):
    post = requests.get('http://127.0.0.1:5000/get/destination',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('view_post.html', post=post_dict['post'][0])

@server.route('/attraction/<name>', methods=['GET'])
def view_attraction(name):
    post = requests.get('http://127.0.0.1:5000/get/attraction',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('view_post.html', post=post_dict['post'][0])

@server.route('/admin/region/<name>', methods=['GET'])
def admin_view_region(name):
    post = requests.get('http://127.0.0.1:5000/get/region',
                               json={"title": name})
    post_dict = json.loads(post.text)
    print post_dict
    return render_template('admin_view_post.html', post=post_dict['post'][0])

@server.route('/admin/destination/<name>', methods=['GET'])
def admin_view_destination(name):
    post = requests.get('http://127.0.0.1:5000/get/destination',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('admin_view_post.html', post=post_dict['post'][0])

@server.route('/admin/attraction/<name>', methods=['GET'])
def admin_view_attraction(name):
    post = requests.get('http://127.0.0.1:5000/get/attraction',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('admin_view_post.html', post=post_dict['post'][0])

@server.route('/editor/region/<name>', methods=['GET'])
def editor_view_region(name):
    post = requests.get('http://127.0.0.1:5000/get/region',
                               json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('editor_view_post.html', post=post_dict['post'][0])

@server.route('/editor/destination/<name>', methods=['GET'])
def editor_view_destination(name):
    post = requests.get('http://127.0.0.1:5000/get/destination',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('editor_view_post.html', post=post_dict['post'][0])

@server.route('/editor/attraction/<name>', methods=['GET'])
def editor_view_attraction(name):
    post = requests.get('http://127.0.0.1:5000/get/attraction',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('editor_view_post.html', post=post_dict['post'][0])

@server.route('/writer/region/<name>', methods=['GET'])
def writer_view_region(name):
    post = requests.get('http://127.0.0.1:5000/get/region',
                               json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('writer_view_post.html', post=post_dict['post'][0])

@server.route('/writer/destination/<name>', methods=['GET'])
def writer_view_destination(name):
    post = requests.get('http://127.0.0.1:5000/get/destination',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('writer_view_post.html', post=post_dict['post'][0])

@server.route('/writer/attraction/<name>', methods=['GET'])
def writer_view_attraction(name):
    post = requests.get('http://127.0.0.1:5000/get/attraction',
                        json={"title": name})
    post_dict = json.loads(post.text)
    return render_template('writer_view_post.html', post=post_dict['post'][0])

@server.route('/region', methods=['GET'])
def view_all_region():
    post = requests.get('http://127.0.0.1:5000/get/all/region')
    post_dict = json.loads(post.text)
    print(post_dict)
    return render_template('view_regions.html', posts=post_dict['posts'])

@server.route('/destinations', methods=['GET'])
def view_all_destinations():
    post = requests.get('http://127.0.0.1:5000/get/all/destinations')
    post_dict = json.loads(post.text)
    print(post_dict)
    return render_template('view_destinations.html', posts=post_dict['posts'])

@server.route('/attractions', methods=['GET'])
def view_all_attractions():
    post = requests.get('http://127.0.0.1:5000/get/all/attractions')
    post_dict = json.loads(post.text)
    print(post_dict)
    return render_template('view_attractions.html', posts=post_dict['posts'])

@server.route('/admin/region', methods=['GET'])
def view_admin_all_region():
    post = requests.get('http://127.0.0.1:5000/get/all/region')
    post_dict = json.loads(post.text)
    return render_template('admin_region.html', posts=post_dict['posts'])

@server.route('/admin/destinations', methods=['GET'])
def view_admin_all_destination():
    post = requests.get('http://127.0.0.1:5000/get/all/destinations')
    post_dict = json.loads(post.text)
    return render_template('admin_destinations.html', posts=post_dict['posts'])

@server.route('/admin/attractions', methods=['GET'])
def view_admin_all_attractions():
    post = requests.get('http://127.0.0.1:5000/get/all/attractions')
    post_dict = json.loads(post.text)
    return render_template('admin_attractions.html', posts=post_dict['posts'])

@server.route('/editor/region', methods=['GET'])
def view_editor_all_region():
    post = requests.get('http://127.0.0.1:5000/get/all/region')
    post_dict = json.loads(post.text)
    return render_template('editor_region.html', posts=post_dict['posts'])

@server.route('/editor/destinations', methods=['GET'])
def view_editor_all_destination():
    post = requests.get('http://127.0.0.1:5000/get/all/destinations')
    post_dict = json.loads(post.text)
    return render_template('editor_destinations.html', posts=post_dict['posts'])

@server.route('/editor/attractions', methods=['GET'])
def view_editor_all_attractions():
    post = requests.get('http://127.0.0.1:5000/get/all/attractions')
    post_dict = json.loads(post.text)
    return render_template('editor_attractions.html', posts=post_dict['posts'])

@server.route('/writer/view/region', methods=['GET'])
def view_writer_all_region():
    post = requests.get('http://127.0.0.1:5000/get/all/region')
    post_dict = json.loads(post.text)
    return render_template('writer_view_region.html', posts=post_dict['posts'])

@server.route('/writer/view/destination', methods=['GET'])
def view_writer_all_destination():
    post = requests.get('http://127.0.0.1:5000/get/all/destinations')
    post_dict = json.loads(post.text)
    return render_template('writer_view_destination.html', posts=post_dict['posts'])

@server.route('/writer/view/attractions', methods=['GET'])
def view_writer_all_attractions():
    post = requests.get('http://127.0.0.1:5000/get/all/attractions')
    post_dict = json.loads(post.text)
    return render_template('writer_view_attractions.html', posts=post_dict['posts'])


@server.route('/unauthorized')
def unauthorized():
    return render_template("401_error.html")

@server.route('/register', methods=['GET','POST'])
def register():
    return render_template("signup.html")

@server.route('/admin', methods=['GET'])
def landing_admin():
    post = requests.get('http://127.0.0.1:5000/get_posted')
    post_dict = json.loads(post.text)
    return render_template('admin.html', posts=post_dict['submissions'])

@server.route('/admin/user')
def admin_user():
    return render_template('admin_user.html')


@server.route('/writer/region')
def write_region():
    return render_template('write_region.html')

@server.route('/writer/destination')
def write_destination():
    regions = requests.get('http://127.0.0.1:5000/get_regions')
    dict = json.loads(regions.text)
    return render_template('write_destination.html', regions=dict['regions'])

@server.route('/writer/attraction')
def write_attraction():
    regions = requests.get('http://127.0.0.1:5000/get_regions')
    dict = json.loads(regions.text)
    destinations = requests.get('http://127.0.0.1:5000/get_destinations')
    dict2 = json.loads(destinations.text)
    return render_template('write_attraction.html', regions=dict['regions'], destinations=dict2['destinations'])

@server.route('/writer')
def writer():
    if 'user' in session:
        submissions = requests.get('http://127.0.0.1:5000/get_posted')
        dict = json.loads(submissions.text)
        return render_template('writer.html', posts=dict['submissions'])
    else:
        print('error')
        return redirect('unauthorized')

@server.route('/editor')
def editor():
    if 'user' in session:
        submissions = requests.get('http://127.0.0.1:5000/get_posted')
        dict = json.loads(submissions.text)
        return render_template('editor.html', posts=dict['submissions'])
    else:
        print('error')
        return redirect('unauthorized')

@server.route('/writer/submissions')
def submissions():
    submissions = requests.get('http://127.0.0.1:5000/api/writer/submissions',
                             json={"username": session['user']})
    dict = json.loads(submissions.text)
    return render_template('write_submission.html', submissions=dict['submissions'])

@server.route('/writer/returned-submissions')
def returned_submissions():
    submissions = requests.get('http://127.0.0.1:5000/api/writer/submissions/returned',
                             json={"username": session['user']})
    dict = json.loads(submissions.text)
    return render_template('writer_returned_submissions.html', submissions=dict['submissions'])

@server.route('/writer/drafts')
def drafts():
    submissions = requests.get('http://127.0.0.1:5000/api/writer/drafts',
                             json={"username": session['user']})
    dict = json.loads(submissions.text)
    print(dict)
    return render_template('write_drafts.html', submissions=dict['drafts'])

@server.route('/draft/edit', methods=['POST'])
def edit_drafts():
    write = request.form['write']
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    return render_template('edit_drafts.html', submission=dict['submission'][0])

@server.route('/draft/edit-destination', methods=['POST'])
def edit_drafts_destination():
    write = request.form['write']
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit-destination',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    regions = requests.get('http://127.0.0.1:5000/get_regions')
    dict2 = json.loads(regions.text)
    return render_template('edit_drafts_destination.html', submission=dict['submission'][0], regions=dict2['regions'])

@server.route('/draft/edit-attraction', methods=['POST'])
def edit_drafts_attraction():
    write = request.form['write']
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit-attraction',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    regions = requests.get('http://127.0.0.1:5000/get_regions')
    dict2 = json.loads(regions.text)
    destinations = requests.get('http://127.0.0.1:5000/get_destinations')
    dict3 = json.loads(destinations.text)
    return render_template('edit_drafts_attraction.html', submission=dict['submission'][0], regions=dict2['regions'], destinations=dict3['destinations'])

@server.route('/editor/submissions')
def editor_submissions():
    submissions = requests.get('http://127.0.0.1:5000/api/editor/submissions',
                             json={"username": session['user']})
    dict = json.loads(submissions.text)
    print(dict)
    return render_template('editor_submissions.html', submissions=dict['submissions'])

@server.route('/editor/edit', methods=['POST'])
def editor_edit():
    write = request.form['write']
    print(write)
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    return render_template('editor_view.html', submission=dict['submission'][0])

@server.route('/editor/edit-destination', methods=['POST'])
def editor_edit_destination():
    write = request.form['write']
    regions = requests.get('http://127.0.0.1:5000/get_regions')
    dict2 = json.loads(regions.text)
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit-destination',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    return render_template('editor_view_destination.html', submission=dict['submission'][0], regions=dict2['regions'])

@server.route('/editor/edit-attraction', methods=['POST'])
def editor_edit_attraction():
    write = request.form['write']
    print(write)
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit-attraction',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    regions = requests.get('http://127.0.0.1:5000/get_regions')
    dict2 = json.loads(regions.text)
    destinations = requests.get('http://127.0.0.1:5000/get_destinations')
    dict3 = json.loads(destinations.text)
    return render_template('editor_view_attraction.html', submission=dict['submission'][0], regions=dict2['regions'], destinations=dict3['destinations'])

@server.route('/edit', methods=['POST'])
def edit_region():
    write = request.form['write']
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    return render_template('edit_a_region.html', submission=dict['submission'][0])

@server.route('/edit/destination', methods=['POST'])
def edit_destination():
    write = request.form['write']
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit-destination',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    return render_template('edit_a_destination.html', submission=dict['submission'][0])

@server.route('/edit/attraction', methods=['POST'])
def edit_attraction():
    write = request.form['write']
    submission = requests.get('http://127.0.0.1:5000/api/writer/submission/edit-attraction',
                               json={"username": session['user'], "write_id": write})
    dict = json.loads(submission.text)
    regions = requests.get('http://127.0.0.1:5000/get_regions')
    dict2 = json.loads(regions.text)
    destinations = requests.get('http://127.0.0.1:5000/get_destinations')
    dict3 = json.loads(destinations.text)
    return render_template('edit_a_attraction.html', submission=dict['submission'][0], regions=dict2['regions'], destinations=dict3['destinations'])


@server.route('/upload', methods=['POST', 'GET'])
def upload_photo():
    file = request.files['qqfile']
    response = requests.post('http://127.0.0.1:5000/api/writer/upload',
                             json={"username": session['user'], "filename": b64encode(file.read())})
    print(file)
    print(request.files['qqfile']['FileStorage'])
    return jsonify({'success': 'true'})

@server.route('/delete', methods=['POST', 'GET'])
def delete_photo():
    file = request.files['qqfile']
    response = requests.post('http://127.0.0.1:5000/api/writer/delete',
                             json={"username": session['user'], "filename": b64encode(file.read())})
    print(file)
    return jsonify({'success': 'true'})

@server.route('/profile/info')
def profile():
    infos = requests.get('http://127.0.0.1:5000/api/profile',json={"username": session['user']})
    dict = json.loads(infos.text)
    return render_template('profile.html', infos=dict['infos'][0])

@server.route('/profile/mypost')
def profileposts():
    submissions = requests.get('http://127.0.0.1:5000/get_yourpost',json={"username": session['user']})
    dict = json.loads(submissions.text)
    return render_template('profilepost.html', posts=dict['submissions'])

@server.route('/delete/admin', methods=['GET', 'POST'])
def delete_post_admin():
    write_id = request.form['write_id']
    type = request.form.get('type')
    if type == 'Region':
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/region', json={"write_id": write_id})
    elif type == 'Destination':
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/destination', json={"write_id": write_id})
    else:
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/attraction', json={"write_id": write_id})
    return redirect(url_for('landing_admin'))

@server.route('/delete/editor', methods=['POST'])
def delete_post():
    write_id = request.form['write_id']
    type = request.form.get('type')
    print type
    print write_id
    if type == 'Region':
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/region', json={"write_id": write_id})
    elif type == 'Destination':
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/destination', json={"write_id": write_id})
    else:
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/attraction', json={"write_id": write_id})
    return redirect(url_for('editor'))

@server.route('/delete/draft', methods=['POST'])
def delete_writer():
    write_id = request.form['write_id']
    type = request.form.get('type')
    print type
    print write_id
    if type == 'Region':
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/region', json={"write_id": write_id})
    elif type == 'Destination':
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/destination', json={"write_id": write_id})
    else:
        infos = requests.post('http://127.0.0.1:5000/api/editor/delete/attraction', json={"write_id": write_id})
    return redirect(url_for('writer'))

CORS(server)
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['USE_SESSION_FOR_NEXT'] = True
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'
dc = SQLAlchemy(server)
server.secret_key = os.urandom(24)

if __name__=='__main__':
    server.run(host='localhost', port=8000, debug=True)
