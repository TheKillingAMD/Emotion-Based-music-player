from flask import Flask, render_template, request, url_for, redirect
from capture import getEmotion, video_capture
from flask_pymongo import PyMongo, ObjectId
from flask.json import JSONEncoder
from flask_cors import CORS, cross_origin
from bson import ObjectId
import easygui
import random

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config["MONGO_URI"] = "mongodb+srv://Ayush:mongodb@cluster0.0ngc1.mongodb.net/Playlists"
mongo = PyMongo(app)
db_happy = mongo.db.Happy
db_neutral = mongo.db.Neutral
db_sad = mongo.db.Sad
db_angry = mongo.db.Angry
db_count = mongo.db.Count


def count(num):
    happy = db_count.find_one({"Type": "Happy"})
    neutral = db_count.find_one({"Type": "Neutral"})
    sad = db_count.find_one({"Type": "Sad"})
    angry = db_count.find_one({"Type": "Angry"})
    happy = happy["Count"]
    neutral = neutral["Count"]
    sad = sad["Count"]
    angry = angry["Count"]
    if num == 1:
        return happy
    elif num == 2:
        return neutral
    elif num == 3:
        return sad
    else:
        return angry


def luck(num):
    return random.randint(1, num)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        # video_capture.release()
        return render_template("main.html")
    else:
        try:
            emotion = getEmotion()
            if emotion == "happy":
                return redirect(url_for('happy'))
            elif emotion == "neutral":
                return redirect(url_for('neutral'))
            elif emotion == "sad":
                return redirect(url_for('sad'))
            else:
                return redirect(url_for('angry'))
        except:
            easygui.msgbox("No Face Found, Please clean your camera or increase lighting of Surroudings", title="Face Not Found")
            return redirect(url_for('home'))
            


@app.route('/happy', methods=['GET', 'POST'])
def happy():
    if request.method == 'GET':
        num = count(1)
        num = luck(num)
        song = db_happy.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("happy.html", Name=Name, Link=Link)
    else:
        num = count(1)
        num = luck(num)
        song = db_happy.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("happy.html", Name=Name, Link=Link)


@app.route('/neutral', methods=['GET', 'POST'])
def neutral():
    if request.method == 'GET':
        num = count(2)
        num = luck(num)
        song = db_neutral.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("neutral.html", Name=Name, Link=Link)
    else:
        num = count(2)
        num = luck(num)
        song = db_neutral.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("neutral.html", Name=Name, Link=Link)


@app.route('/sad', methods=['GET', 'POST'])
def sad():
    if request.method == 'GET':
        num = count(3)
        num = luck(num)
        song = db_sad.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("sad.html", Name=Name, Link=Link)
    else:
        num = count(3)
        num = luck(num)
        song = db_sad.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("sad.html", Name=Name, Link=Link)


@app.route('/angry', methods=['GET', 'POST'])
def angry():
    if request.method == 'GET':
        num = count(4)
        num = luck(num)
        song = db_angry.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("angry.html", Name=Name, Link=Link)
    else:
        num = count(4)
        num = luck(num)
        song = db_angry.find_one({"song#": num})
        Name = song["Name"]
        Link = song["youtube link"]
        return render_template("angry.html", Name=Name, Link=Link)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        name = request.form.get('name')
        emotion = request.form.get('emotion')
        link = request.form.get('link')
        if emotion == "happy":
            num = count(1)
            db_count.update_one({'Type': 'Happy'}, {"$set": {'Count': num+1}})
        elif emotion == "neutral":
            num = count(2)
            db_count.update_one({'Type': 'Neutral'}, {"$set": {'Count': num+1}})
        elif emotion == "sad":
            num = count(3)            
            db_count.update_one({'Type': 'Sad'}, {"$set": {'Count': num+1}})            
        else:
            num = count(4)
            db_count.update_one({'Type': 'Angry'}, {"$set": {'Count': num+1}})
        song = {
            "song#": num+1,
            "youtube link": link,
            "Name": name
        }
        if emotion == "happy":
            db_happy.insert_one(song)
        elif emotion == "neutral":
            db_neutral.insert_one(song)
        elif emotion == "sad":
            db_sad.insert_one(song)
        else:
            db_angry.insert_one(song)
        return redirect(url_for('home'))


# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=True)
