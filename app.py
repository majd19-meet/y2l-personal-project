from flask import Flask, render_template, url_for, redirect, request, session
from databases import query_by_topic, add_article, get_all_articles, add_user, get_all_users,query_by_username
import smtplib
from string import Template
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

app.config["SECRET_KEY"] = "your-secret-key"

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

@app.route('/abortion', methods=["POST", "GET"])
def abortion():
  article= query_by_topic("abortion")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('abortion.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"abortion")
        return render_template('abortion.html',articles=article)
  return redirect(url_for('login_route'))       

@app.route('/G1', methods=["POST", "GET"])
def G1():
  article= query_by_topic("G1")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('G1.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"G1")
        return render_template('G1.html',articles=article)
  return redirect(url_for('login_route'))   


@app.route('/G2', methods=["POST", "GET"])
def G2():
  article= query_by_topic("G2")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('G2.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"G2")
        return render_template('G2.html',articles=article)
  return redirect(url_for('login_route')) 
    # return render_template("G2.html")

@app.route('/racism', methods=["POST", "GET"])
def racism():
  article= query_by_topic("racism")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('racism.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"racism")
        return render_template('racism.html',articles=article)
  return redirect(url_for('login_route')) 
    # return render_template("racism.html")

@app.route('/homo1', methods=["POST", "GET"])
def homo1():
  article= query_by_topic("homo1")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('homo1.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"homo1")
        return render_template('homo1.html',articles=article)
  return redirect(url_for('login_route')) 
    # return render_template("homo1.html")

@app.route('/homo2', methods=["POST", "GET"])
def homo2():
  article= query_by_topic("homo2")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('homo2.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"homo2")
        return render_template('homo2.html',articles=article)
  return redirect(url_for('login_route')) 
    # return render_template("homo2.html")

@app.route('/rape', methods=["POST", "GET"])
def rape():
  article= query_by_topic("rape")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('rape.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"rape")
        return render_template('rape.html',articles=article)
  return redirect(url_for('login_route')) 
    # return render_template("rape.html")

@app.route('/death', methods=["POST", "GET"])
def death():
  article= query_by_topic("death")
  if 'logged_in' in session:
    if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('death.html',articles=article)
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        comments= request.form["comments"]
        user_id=session['user_id']
        add_article(comments,user_id,"death")
        return render_template('death.html',articles=article)
  return redirect(url_for('login_route'))
    # return render_template("death.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
  if request.method == 'GET':
    return render_template('signup.html')
  else:
    print ('Received POST request for sign up!')
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

        return render_template('home.html')
      else:
        return redirect(url_for('login_route'))
  else:
    return render_template('login.html') 


@app.route('/logout')
def logout_route():
  if 'user_id' in session:
    del session['user_id']
    session['logged_in']=False
  return redirect(url_for('home'))
  print('logged out')

@app.route('/email', methods=["POST", "GET"])
def send_email():
  return render_template("home.html")


if __name__ == "__main__":
	app.run(debug=True)