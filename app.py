from flask import Flask, flash, render_template, url_for, redirect, request, session as flask_session
from database import *
# from database import *

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/create-post',methods=['GET','POST'])
# def create_post(): 
#     if 'username' in flask_session:
#         if request.method == 'GET':
#             return render_template('create_post.html')
#         else:
#             post_string = request.form['post_submit']
#             add_Post(post_string)
#             return redirect(url_for('home'))
#     else:
#         return redirect(url_for('log_in'))

# @app.route('/about-us')
# def about_us():
#     return render_template('aboutus.html')

# @app.route('/log-out')
# def log_out():
#     posts = query_all_posts()
#     posts = posts[::-1]
#     if 'username' in flask_session:
#         del flask_session['username']
#         return render_template('home.html',name="",posts=posts)
#     else:
#         return redirect(url_for('home'))

# @app.route('/log-in', methods=['GET','POST'])
# def log_in():
#     if request.method == 'POST':
#         name = request.form['uname']
#         password = request.form['psw']
#         posts = query_all_posts()
#         posts = posts.reverse()

#         user = query_by_name_and_password(name, password)
#         if user is not None and user.password == password:
#             flask_session['username'] = user.name
#             return redirect(url_for('home'))
#         else :
#             error = 'Username & Password do not match , Please try again'
#             flash(error)
#             return render_template('log_in.html')
#     else:       
#         return render_template('log_in.html')

# @app.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         name = request.form['username'] 
#         password = request.form['psw']
#         add_user(name,password)
#         flash('You were successfully signed up')
#         return redirect(url_for('log_in'))

#     else:
#         return render_template('sign_up.html')

@app.route('/store', methods=['GET'])
def store():
    items=query_all_items()
    return render_template('store.html', items=items)

@app.route('/band')
def band():
    return render_template('home.html')

@app.route('/tour')
def tour():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)



