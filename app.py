import os
import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('newlogin')
def on_newlogin(data):
    print("Got an event for new user", data['uname'])
    uname = data['uname']
    password = data['password']
    socketio.emit('new user', {
        'user': uname
    })
    
@socketio.on('newmessage')
def on_newmessage(data):
    print("Got new message")
    message=data['txt']
    answer = ''
    #if message[0:2] == '!!': answer = botmessage(message)
    #else 
    socketio.emit('newmessage', {
        'answer':answer
    })
if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
