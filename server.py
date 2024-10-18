from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seu_segredo_aqui'
socketio = SocketIO(app)

users = {
    "usuario1": {"password": "senha1", "role": "padrão"},
    "usuario2": {"password": "senha2", "role": "doador"},
    "usuario3": {"password": "senha3", "role": "STAFF"},
    "usuario4": {"password": "senha4", "role": "ADM"},
    "usuario5": {"password": "senha5", "role": "Dono"},
}

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

@app.route('/send', methods=['POST'])
def send_message():
    if 'username' not in session:
        return jsonify(success=False, error="Não autenticado")

    data = request.get_json()
    message = f"{session['username']} ({session['role']}): {data['message']}"
    messages.append(message)
    socketio.emit('message', message)
    return jsonify(success=True)

@app.route('/messages')
def get_messages():
    return jsonify(messages=messages)

def can_manage_channels(role):
    return role in ["STAFF", "ADM", "Dono"]

@app.route('/create_channel', methods=['POST'])
def create_channel():
    if 'username' not in session or not can_manage_channels(session['role']):
        return jsonify(success=False, error="Permissão negada")
    # Lógica para criar o canal

if __name__ == '__main__':
    socketio.run(app, debug=True)
