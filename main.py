import os.path
from os import path

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello I am GetYourMusicBuzz Backend'


@app.route('/receive',methods=['POST'])
def login():
    train_data = []
    train_label = []

    train_data.append(request.form['Aladdin'])
    train_data.append(request.form['Frozen'])
    train_data.append(request.form['Hercules'])
    train_data.append(request.form['Moana'])
    train_data.append(request.form['Raya'])
    train_data.append(request.form['StarWars'])
    train_data.append(request.form['analyst'])
    train_data.append(request.form['aries'])
    train_data.append(request.form['blue'])
    train_data.append(request.form['cancer'])
    train_data.append(request.form['capricorn'])
    train_data.append(request.form['cat'])
    train_data.append(request.form['cow'])
    train_data.append(request.form['diplomat'])
    train_data.append(request.form['dog'])
    train_data.append(request.form['elephant'])
    train_data.append(request.form['explorer'])
    train_data.append(request.form['fish'])
    train_data.append(request.form['fox'])
    train_data.append(request.form['fun'])
    train_data.append(request.form['gemini'])
    train_data.append(request.form['green'])
    train_data.append(request.form['happiness'])
    train_data.append(request.form['indigo'])
    train_data.append(request.form['leo'])
    train_data.append(request.form['libra'])
    train_data.append(request.form['meat'])
    train_data.append(request.form['nothing'])
    train_data.append(request.form['orange'])
    train_data.append(request.form['pisces'])
    train_data.append(request.form['productive'])
    train_data.append(request.form['red'])
    train_data.append(request.form['rollercoaster'])
    train_data.append(request.form['sagittarius'])
    train_data.append(request.form['scorpio'])
    train_data.append(request.form['seafood'])
    train_data.append(request.form['sentinel'])
    train_data.append(request.form['sleep'])
    train_data.append(request.form['taurus'])
    train_data.append(request.form['turtle'])
    train_data.append(request.form['veggies'])
    train_data.append(request.form['violet'])
    train_data.append(request.form['virgo'])
    train_data.append(request.form['yellow'])

    label_data.append(request.form['label_acousticness'])
    label_data.append(request.form['label_danceability'])
    label_data.append(request.form['label_energy'])
    label_data.append(request.form['label_instrumentalness'])
    label_data.append(request.form['label_key'])
    label_data.append(request.form['label_liveness'])
    label_data.append(request.form['label_loudness'])
    label_data.append(request.form['label_mode'])
    label_data.append(request.form['label_speechiness'])
    label_data.append(request.form['label_tempo'])
    label_data.append(request.form['label_time_signature'])
    label_data.append(request.form['label_track'])
    label_data.append(request.form['label_valence'])

    f1 = None
    f2 = None
    if (not path.exists("train_data.txt")):
        f1 = open("train_data.txt", "w+")
        f2 = open("train_label.txt", "w+")
    else:
        f1 = open("train_data.txt", "a+")
        f2 = open("train_label.txt", "a+")
   

    f1.write(str(train_data)[1:-1])
    f2.write(str(train_label)[1:-1])

    f1.write("\n")
    f2.write("\n")

    f1.close()
    f2.close()

    return "GOT!"

if __name__ == '__main__':
    app.run()