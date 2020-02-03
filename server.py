from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__);


@app.route('/')
def return_index():
    return render_template("index.html");


@app.route('/game', methods=['GET', 'POST'])
def return_game():
    if request.method == "POST":
        number_of_cards = request.form["exampleFormControlSelect1"]
        arr_10 = ["fas fa-baby-carriage fa-5x", "fas fa-baby-carriage fa-5x", "fas fa-pegasus fa-5x",
                  "fas fa-pegasus fa-5x",
                  "fas fa-dragon fa-5x", "fas fa-dragon fa-5x", "fas fa-skull-cow fa-5x", "fas fa-skull-cow fa-5x",
                  "fas fa-fighter-jet fa-5x",
                  "fas fa-fighter-jet fa-5x"]

        arr_20 = ["fas fa-baby-carriage fa-5x", "fas fa-baby-carriage fa-5x", "fas fa-pegasus fa-5x",
                  "fas fa-pegasus fa-5x",
                  "fas fa-dragon fa-5x", "fas fa-dragon fa-5x", "fas fa-skull-cow fa-5x", "fas fa-skull-cow fa-5x",
                  "fas fa-fighter-jet fa-5x",
                  "fas fa-fighter-jet fa-5x", "fas fa-baseball-ball", "fas fa-baseball-ball", "fas fa-anchor fa-5x",
                  "fas fa-anchor fa-5x", "fas fa-lemon fa-5x", "fas fa-lemon fa-5x", "fas fa-sun fa-5x",
                  "fas fa-sun fa-5x", "fas fa-industry fa-5x", "fas fa-industry fa-5x"]

        random.shuffle(arr_10)
        random.shuffle(arr_20)


       
        return render_template("game.html", cards=int(number_of_cards))


if __name__ == "__main__":
    app.run(debug=True);
