from flask import Flask, render_template

app = Flask(__name__)


# main page
@app.route("/")
def home():
    return render_template("index.html")

# about page
@app.route("/about")
def about():
    return render_template("about.html")

# design page
@app.route("/design")
def design():
    return render_template("Design.html")

# code page
@app.route("/code")
def code():
    return render_template("code.html")

# cont page
@app.route("/cont")
def cont():
    return render_template("cont.html")


app.run(debug=True)
# app.run(host='192.168.43.20', debug=True)
