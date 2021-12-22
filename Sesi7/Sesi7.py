from flask import Flask,render_template,request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
 return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
 # show the user profile for that user
 return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
 # show the post with the given id, the id is an integer
 return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
 # show the subpath after /path/
 return f'Subpath {escape(subpath)}'

@app.route('/login', methods=['GET', 'POST'])
def login():
 if request.method == 'POST':
    return do_login()
 else:
    return show_login_form()

def do_login():
    return f"login sukses dengan request {request.method}"
    
def show_login_form():
    return f"login form dengan request {request.method}"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
 return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()