import os.path
from os import path
from flask_cors import CORS

from flask import Flask, request
from model import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello I am GetYourMusicBuzz Backend'

@app.route('/train')
def train():
    train_entire_model()
    return 'Hello I am GetYourMusicBuzz Backend'

@app.route('/reset')
def reset():
    f1 = open("train_data.txt", "w+")
    f1.write("")
    f1.close()
    return 'Hello I am GetYourMusicBuzz Backend'

@app.route('/predict',methods=['POST', 'OPTION'])
def p():
    if(request.method != 'POST'):
      return "BAD"

    data = (request.get_json())
    result = predict(data)

    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/receive',methods=['POST', 'OPTION'])
def receive():
    if(request.method != 'POST'):
      return "BAD"

    data = (request.get_json())

    f1 = None

    f1 = open("train_data.txt", "a+")
   

    f1.write(str(data))
    f1.write("\n")

    f1.close()

    return "GOT!"

if __name__ == '__main__':
  app.run(threaded=True, port=5000)
