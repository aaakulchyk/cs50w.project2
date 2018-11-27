import os, requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/channels')
def show_channels():
    return render_template('channels_list.html')


@app.route('/channels/<int:id>')
def come_in(id):
    return render_template('channel.html', id=id)