import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import flickr
from random import random


DATABASE = 'colleck.db'
DEBUG = True
SECRET_KEY = 'development key'
# USERNAME = 'admin'
# PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def initial():
	flash('test')
	return render_template('initial.html')

@app.route('/result',methods=['GET','POST'])
def show_results():
	if request.method == 'POST' and request.form['search']:
		print request.form['search']
		photos = flickr.photos_search(text=request.form['search'])
		url_list = [url.getMedium() for url in photos]
		
		if not len(url_list):
			flash("Sorry, no photos were found")
			return redirect(url_for('initial'))
		
		random_index = int(random()*len(url_list))
		photo = url_list[random_index]
		return render_template('result.html', photo=photo)
	return redirect(url_for('initial'))

# def check_login(name, password):
# 	cur = g.db.execute("select name, password from users where name = (?)", [request.form['name']])
# 	return (name, password) in cur.fetchall()


# @app.route('/login', methods=['GET','POST'])
# def login():
# 	if request.method == 'POST':
# 		if check_login(request.form['name'], request.form['password']):
# 			flash('Welcome!')
# 			return redirect(url_for('initial'))
# 		else:
# 			session['logged_in'] = True
# 			flash('Your username or password was mistyped')
# 	return render_template('login.html')

# @app.route('/add', methods=['POST'])
# def add_photo():
# 	if not session.get('logged_in'):
# 		abort(401)
# 	g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'],request.form['text']])
# 	g.db.commit()
# 	flash('New entry was succesfully posted')
# 	return redirect(url_for('show_entries'))


# @app.route('/register', methods=['GET','POST'])
# def register():
# 	if session.get('logged_in'):
# 		abort(300)
# 	if request.method == 'POST':
# 		cur = g.db.execute("select count(name) from users where name = (?)", [request.form['name']])
# 		if (1,) in cur.fetchall():
# 			print 'entered here!'
# 			flash('This name is already in use')
# 			return render_template('register.html')
# 		g.db.execute('insert into users (name, password) values (?, ?)', [request.form['name'],request.form['password']])
# 		g.db.commit()
# 		flash("You're registered")
# 		return redirect(url_for('initial'))
# 	return render_template('register.html')

# @app.route('/logout')
# def logout():
# 	session.pop('logged_in', None)
# 	flash('You were logged out')
# 	return redirect(url_for('initial'))

# @app.route('/collection')
# def see_collection():
# 	pass

# @app.route('/collect')
# def add_collection():

if __name__ == "__main__":
	app.run()