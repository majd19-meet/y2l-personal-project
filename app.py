from flask import Flask, render_template, url_for, redirect, request, session
from databases import add_user, get_all_users,query_by_username

app = Flask(__name__)

app.config["SECRET_KEY"] = "your-secret-key"

# @app.route("/")
# def home_page():
# 	return render_template("home.html")

@app.route('/')
def home():
  if session.get('display_login') == True:
    session['display_login'] = False
    return render_template('home.html', logged_in=True)
  else:
    return render_template('home.html', logged_in=False)


@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/topics')
def topics():
    return render_template("topics.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/abortion')
def abortion():
    return render_template("abortion.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
  if request.method == 'GET':
    return render_template('signup.html')
  else:
    print ('Received POST request for sign up!')
    # nationality = request.form['nationality']
    name = request.form['name']
    password= request.form['password']
    
    g=query_by_username(name)

    if g!=None:
      print ('we already have a user with that name')
    else:
      add_user(name, password)
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login_route():
  if 'logged_in' in session and session['logged_in']==True:
    return redirect (url_for('home'))
  if request.method == 'POST':
    # return redirect (url_for('home'))
    print('hey')
    user=query_by_username(request.form['name'])
    if user==None:
      return redirect (url_for('signup_route'))
    else:
      # if request.form.get('password') and
      if request.form['password']== user.password:
        session["logged_in"] = True
        session["user_id"] = user.name
        session["display_login"] = True

      # session['logged_in'] == True
      # session['user_id']== user_id
      # session['display_login'] == True
        # return redirect(url_for('home'))

        return render_template('home.html')
  else:
    return render_template('login.html') 

# @app.route('/signup')
# def signup():
#     return render_template("signup.html")


@app.route('/logout')
def logout_route():
  if 'user_id' in session:
    del session['user_id']
    session['logged_in']=False
  return redirect(url_for('home'))
  print('logged out')


if __name__ == "__main__":
	app.run(debug=True)