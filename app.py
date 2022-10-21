"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def list_users():
    '''Lists users and shows add form'''

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route('/add_user')
def show_add_form():
    return render_template("add_user.html")


@app.route('/add_user', methods=['POST'])
def add_user():
    '''Add a profile'''
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url']

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/")


@app.route('/<int:user_id>')
def show_user_profile(user_id):
    '''Show user profile'''
    user = User.query.get_or_404(user_id)
    return render_template("profile.html", user=user)


@app.route('/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    '''Delete user'''
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')


@app.route('/edit_profile/<int:user_id>')
def show_edit_form(user_id):
    '''Show edit profile form'''
    user = User.query.get_or_404(user_id)
    return render_template("edit_profile.html", user=user)


@app.route('/edit_profile/<int:user_id>', methods=['POST'])
def edit_profile(user_id):
    '''Edit profile'''
    user = User.query.get_or_404(user_id)

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    img_url = request.form.get('img_url')

    if first_name != "":
        user.first_name = first_name
    if last_name != "":
        user.last_name = last_name
    if img_url != "":
        user.img_url = img_url

    db.session.add(user)
    db.session.commit()
    return redirect('/')