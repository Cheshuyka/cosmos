from flask import Flask, render_template, redirect, request, abort


app = Flask(__name__)


@app.route('/')  # основная страница
def index():
    return render_template('base.html')


if __name__ == "__app__":
    app.run(debug=True)
