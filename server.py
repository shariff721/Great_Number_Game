
from flask import Flask, render_template, session, request, redirect, url_for
import random

app = Flask(__name__)

app.secret_key = "riffdini"

@app.route('/')
def startScreen():
    session['number'] = random.randrange(0,100)
    print(session['number'])
    return render_template("index.html")

@app.route('/checkAnswer', methods =["GET", "POST"]) 
def checkAnswer():
    if request.method == "POST":
        if session['number'] == int(request.form.get("usernumber")):
            return "Correct"
        elif session['number'] < int(request.form.get("usernumber")):
            return "Too High"
        elif session['number'] > int(request.form.get("usernumber")):
            return "Too Low"
    return redirect(url_for("index.html"))





if __name__ == '__main__':
    app.run(debug=True, port = 5001)