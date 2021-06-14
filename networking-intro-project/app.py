from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game, sword

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()


@app.route("/")
def index():
    map = game.getMap()
    return render_template("index.html", mapdata=map, n_row=len(map), n_col=len(map[0]) )

@socketio.on("move")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]
    life = game._player._life
    coin = game._player._coins
    sword = game._player._swords

    data, ret = game.move(dx,dy)
    Data = [data, life, coin, sword]
    if ret:
        socketio.emit("response", Data)


if __name__=="__main__":
    socketio.run(app, port=5001)


