from flask import Flask, render_template, request
from src.index import openBrowser

app = Flask(__name__)


@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/battle/link', methods=["GET", "POST"])
def battleLink():
    print(request.form["link"])
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
