from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def home_page():
	return render_template("home.html")


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/topics')
def topics():
    return render_template("topics.html")

@app.route('/contact')
def contact():
    return render_template("cont.html")




if __name__ == "__main__":
	app.run(debug=True)