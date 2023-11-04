from flask import Flask, render_template, redirect, request, abort


app = Flask(__name__)


@app.route('/')  # основная страница
def index():
    return render_template('base.html')


@app.route('/video')  # страница с видео
def video():
    return render_template('video.html')


if __name__ == "__app__":
    app.run(debug=True)
