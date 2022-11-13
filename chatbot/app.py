import re
from click import prompt
from flask import Flask, render_template, request
import requests
import os
import cohere
co = cohere.Client('')
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    txt= request.args.get('msg')
    response = co.generate( 
    model='large', 
    prompt='MusicBot is a Music Chatbot that loves to talk to talk about music\nMe: Hi\nMusicBot: Hi, I am MusicBot\n--\nMe: What do you love?\nMusicBot: I love singing\n--\nMe: You play any instruments?\nMusicBot: Yea I used to play piano\n--\nMe: Does classical music have a future?\nMusicBot: Yes, people still love classical music\n--\nMe: {}\nMusicBot:'.format(txt), 
    max_tokens=50, 
    temperature=0.9, 
    k=0, 
    p=0.75, 
    frequency_penalty=0, 
    presence_penalty=0, 
    stop_sequences=["--"], 
    return_likelihoods='NONE') 
    answer = format(response.generations[0].text).strip("--")
    return answer



if __name__ == "__main__":
    app.run()