from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__);


@app.route('/')
def return_index():
    return render_template("index.html");

@app.route('/game', methods=['GET','POST'])
def return_game():
    if request.method == "POST":
        number_of_cards = request.form["exampleFormControlSelect1"]
        print(number_of_cards)
        return render_template("game.html", cards = int(number_of_cards))


if __name__ == "__main__":
    app.run(debug=True);
