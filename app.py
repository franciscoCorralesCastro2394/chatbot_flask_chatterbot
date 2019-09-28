
from flask import Flask, render_template, request #
from flask_socketio import SocketIO, send # 
from chatterbot import ChatBot #
from chatterbot.trainers import ChatterBotCorpusTrainer#
from chatterbot.trainers import ListTrainer#
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

bot = ChatBot("Walter Mitty")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.spanish")
trainer.train("chatterbot.corpus.spanish.greetings")
trainer.train("chatterbot.corpus.spanish.conversations")



@app.route('/')
def home():
    return render_template('index.html')



@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == '__main__':
    socketio.run(app)



