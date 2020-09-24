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


@app.route('/post_field', methods=["GET", "POST"])
def post_field():
    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))
        openBrowser()
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
