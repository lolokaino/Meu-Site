from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seu_segredo_aqui'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

users = {
    "usuario1": {"password": "senha1"},
    "usuario2": {"password": "senha2"},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username]['password'] == password:
        session['username'] = username
        return redirect(url_for('chat'))
    
    return redirect(url_for('index'))

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(data):
    socketio.send(data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
