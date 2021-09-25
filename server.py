from flask import Flask, session, render_template, request, redirect
import random


app = Flask(__name__)
app.secret_key = "secret"

randomNumber = random.randint(1,100)

@app.route('/', methods=['GET'])
def findNumber():
    if "randomNumber" not in session:
        session["randomNumber"] = randomNumber
    print(randomNumber)
    return render_template("index.html", guess=None, randomNumber=randomNumber)

@app.route('/validateNumber', methods=['POST'])
def validateGuess():
    if request.form['guess'] == "":
        return render_template("index.html", guess=None, randomNumber=randomNumber)
    else:
        guess=int(request.form['guess'])
        if guess == randomNumber:
            print("right")
            return render_template("index.html", guess = guess, randomNumber=randomNumber)
        elif guess > randomNumber:
            print("Too much")
            return render_template("index.html", guess = guess, randomNumber=randomNumber)
        elif guess < randomNumber:
            print("Too little")
            return render_template("index.html", guess = guess, randomNumber=randomNumber)
        else:
            return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return render_template ("index.html", guess=None, randomNumber=randomNumber)


if __name__ == "__main__":
    app.run( debug = True )