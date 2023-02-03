from flask import Flask, redirect, url_for

app = Flask(__name__)

# routing creation
@app.route("/")
def home():
	return "Hello! This is the home page <h1>HELLO</h1>"

#dynamic routing creation:
@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

#redirect creation:
@app.route("/admin")
def admin():
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()