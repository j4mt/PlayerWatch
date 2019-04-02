#!/usr/bin/env python3

from flask import Flask, render_template
from data import Teams

app = Flask(__name__)

articles = Teams()

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/teams')
def teams():
    return render_template('teams.html', teams=Teams())

@app.route('/team/<string:id>')
def team(id):
    return render_template('teams.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
