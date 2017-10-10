from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")


@app.route('/ninja')
def ninja():
    return render_template("ninja.html")


@app.route('/ninja/blue')
def Blue():
    return render_template("blue.html")

@app.route('/ninja/orange')
def Orange():
    return render_template("orange.html")

@app.route('/ninja/red')
def Red():
    return render_template("red.html")

@app.route('/ninja/purple')
def Purple():
    return render_template("purple.html")

@app.route('/ninja/<vararg>')
def Random(vararg):
    return render_template("notapril.html")

app.run(debug=True)
