import os.path
from os import path
from flask_cors import CORS

from flask import Flask, request
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello I am GetYourMusicBuzz Backend'


@app.route('/receive',methods=['POST', 'OPTION'])
def login():
    if(request.method != 'POST'):
      return "BAD"

    data = (request.get_json())

    f1 = None
    f2 = None
    if (not path.exists("train_data.txt")):
        f1 = open("train_data.txt", "w+")
        f2 = open("train_label.txt", "w+")
    else:
        f1 = open("train_data.txt", "a+")
        f2 = open("train_label.txt", "a+")
   

    f1.write(str(data))
    f1.write("\n")

    f1.close()
    f2.close()

    return "GOT!"

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
