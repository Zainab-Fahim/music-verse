import email
from email.message import EmailMessage
import re
from click import prompt
from flask import Flask, render_template, request
import requests
import cohere
import json
import spotipy
from spotifysearch.client import Client

clientID = ''
clientSecret = ''
myclient = Client(clientID, clientSecret)

co = cohere.Client('')
app = Flask(__name__)

url = "https://api.courier.com/send"
@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        email = request.form['email']
        feelings = request.form['feelings']
        response = co.generate(
        model='xlarge',
        prompt='This program will extract information about feelings from the text\nUser: I am very sad today\nBot: Sad\n--\nUser: I am feeling low today\nBot: Sad\n--\nUser: I am feeling very happy today\nBot: Happy\n--\nUser: I am feeling Angry today\nBot: Angry\n--\nUser: I am feeling very happy today\nBot: Happy\n--\n\nUser: I am feeling Surprised today\nBot: Surprised\n--\nUser:{}\nBot:\n'.format(feelings),
        max_tokens=150,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
        txtresp= response.generations[0].text.strip("--")
        songstring= "Best {} Song".format(txtresp)
        searchsong = str.join(" ", songstring.splitlines())
        results = myclient.search(searchsong)
        tracks = results.get_tracks()
        track = tracks[0]
        songname= track.name
        songurl= track.url
        track1 = tracks[1]
        songname1= track1.name
        songurl1= track1.url
        track2 = tracks[2]
        songname2= track2.name
        songurl2= track2.url
        track3 = tracks[3]
        songname3= track3.name
        songurl3= track3.url
        track4 = tracks[4]
        songname4= track4.name
        songurl4= track4.url
        payload = {
        "message": {
            "to": { 
            "email": "{}".format(email)
            },
            "content":{
            "elements": [
                {
                "type": "meta",
                "title": "Your Music Suggestions"
                },
                {
                    "type": "image",
                     "src": "https://raw.githubusercontent.com/cyrixninja/Do-Re-Mi-Hacks-3/main/Image/email-header.png"
                     },
                {
                "type": "text",
                "content": "**{}**".format(songname)
                },
              {
                    "type": "action",
                    "style": "button",
                    "content": "Open Song",
                    "align": "left",
                    "href": "{}".format(songurl)
                },
                                {
                "type": "text",
                "content": "**{}**".format(songname1)
                },
              {
                    "type": "action",
                    "style": "button",
                    "content": "Open Song",
                    "align": "left",
                    "href": "{}".format(songurl1)
                },
                                {
                "type": "text",
                "content": "**{}**".format(songname2)
                },
              {
                    "type": "action",
                    "style": "button",
                    "content": "Open Song",
                    "align": "left",
                    "href": "{}".format(songurl2)
                },
                                {
                "type": "text",
                "content": "**{}**".format(songname3)
                },
              {
                    "type": "action",
                    "style": "button",
                    "content": "Open Song",
                    "align": "left",
                    "href": "{}".format(songurl3)

                },
                                {
                "type": "text",
                "content": "**{}**".format(songname4)
                },
              {
                    "type": "action",
                    "style": "button",
                    "content": "Open Song",
                    "align": "left",
                    "href": "{}".format(songurl4)
                }
            ],
            "version": "2022-01-01",
            }
        }
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer pk_test_"
            }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)

        print(songname4)
        print(songurl4)
        print(searchsong)
          

        print()
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)