from flask import Flask, render_template, redirect, request, abort


app = Flask(__name__)


@app.route('/')  # основная страница
def index():
    return render_template('base.html')