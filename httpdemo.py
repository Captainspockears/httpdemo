from flask import Flask, redirect, url_for, render_template, request, send_file, session

#CODE STARTS HERE
app = Flask(__name__, template_folder='static', static_folder='static')
app.secret_key = 'key'

savedname = "";

@app.route("/", methods=["POST", "GET"])
def home():

	global savedname

	if request.method == "POST":
		name = request.form["name"]
		session['user'] = name
		savedname = name
			

	return render_template("name.html", currentname=request.form["name"])

@app.route("/whatisname")
def whatisname():

	global savedname

	name = session.get('user')

	if name == "":
		name = "No name was given!"

	if name == None:
		name = savedname

	print(name)
	return name

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, use_reloader=True)
