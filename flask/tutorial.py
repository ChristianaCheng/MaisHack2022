from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

# <name> in the route captures a value from the URL and passes it to the view function. 
@app.route("/<question>/")
def user(question):
	# pass the var question to the question var in the html file
	return render_template("index.html",content = ['a','b','c'])

# access page by admin or admin/
# redirect if people want to get inside this admin page
@app.route("/admin/")
def admin():
	return redirect(url_for("user",question="Admin!"))

if __name__ == "__main__":
	app.run()


# flask --app helpium run
#As a shortcut, if the file is named app.py or wsgi.py
# flask run

# If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply 
# by adding --host=0.0.0.0 to the command line:
# $ flask run --host=0.0.0.0
# This tells your operating system to listen on all public IPs.