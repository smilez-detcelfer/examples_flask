from flask import Flask, redirect, url_for

app = Flask(__name__)

# routing creation
@app.route("/")
def home():
	return "Hello! This is the home page <h1>HELLO</h1>"
#-----------------------------------------
#dynamic routing creation:
@app.route("/<name>")
def user(name):
	return f"Hello user {name}!"
#-----------------------------------------
#redirection creation:
@app.route("/redirect_from")
def redirect_from():
	return redirect(url_for("home")) # "home" is FUNCTION NAME, not path
#-----------------------------------------
#redirection with passing argument
@app.route("/admin")
def admin():
	return redirect(url_for("user", name="admin_userpage"))
	# Now we when we go to /admin we will redirect to user with the argument "Admin!"

@app.route
if __name__ == "__main__":
	app.run()