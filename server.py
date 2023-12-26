from flask import Flask, render_template, redirect, request, abort


app = Flask(__name__)


@app.route('/')  # основная страница
def index():
    return render_template('base.html')


@app.route('/map')  # основная страница
def map():
    return render_template('map.html')


@app.route('/video')  # страница с видео
def video():
    return render_template('video.html')


@app.route('/video1')  # страница 2 с видео
def video1():
    return render_template('video1.html')


@app.route('/video2')  # страница 2 с видео
def video2():
    return render_template('video2.html')


@app.route('/video3')  # страница 2 с видео
def video3():
    return render_template('video3.html')


@app.route('/video4')  # страница 2 с видео
def video4():
    return render_template('video4.html')


if __name__ == "__app__":
    app.run()
