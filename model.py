import numpy as np
import json
import pickle
from sklearn.linear_model import LinearRegression

label_names = ["label_acousticness", "label_danceability", "label_energy", 
"label_instrumentalness", "label_key", "label_loudness", "label_mode",
"label_speechiness", "label_tempo", "label_time_signature", "label_valence"]

def getTrainArray(jsonobj):
    train = []
    label = []

    train.append(jsonobj["red"])
    train.append(jsonobj["orange"])
    train.append(jsonobj["yellow"])
    train.append(jsonobj["green"])
    train.append(jsonobj["blue"])
    train.append(jsonobj["indigo"])
    train.append(jsonobj["violet"])
    train.append(jsonobj["happiness"] / 10)
    train.append(jsonobj["meat"])
    train.append(jsonobj["seafood"])
    train.append(jsonobj["veggies"])
    train.append(jsonobj["nothing"])
    train.append(jsonobj["elephant"])
    train.append(jsonobj["fish"])
    train.append(jsonobj["turtle"])
    train.append(jsonobj["fox"])
    train.append(jsonobj["cow"])
    train.append(jsonobj["dog"])
    train.append(jsonobj["cat"])
    train.append(jsonobj["StarWars"])
    train.append(jsonobj["Frozen"])
    train.append(jsonobj["Moana"])
    train.append(jsonobj["Hercules"])
    train.append(jsonobj["Raya"])
    train.append(jsonobj["Aladdin"])
    train.append(jsonobj["sleep"] / 10)
    train.append(jsonobj["fun"])
    train.append(jsonobj["productive"])
    train.append(jsonobj["rollercoaster"])
    train.append(jsonobj["analyst"])
    train.append(jsonobj["diplomat"])
    train.append(jsonobj["explorer"])
    train.append(jsonobj["sentinel"])
    train.append(jsonobj["aries"])
    train.append(jsonobj["taurus"])
    train.append(jsonobj["gemini"])
    train.append(jsonobj["leo"])
    train.append(jsonobj["cancer"])
    train.append(jsonobj["libra"])
    train.append(jsonobj["virgo"])
    train.append(jsonobj["scorpio"])
    train.append(jsonobj["sagittarius"])
    train.append(jsonobj["capricorn"])
    train.append(jsonobj["aquarius"])
    train.append(jsonobj["pisces"])

    try:
        label.append(jsonobj["label_acousticness"])
        label.append(jsonobj["label_danceability"])
        label.append(jsonobj["label_energy"])
        label.append(jsonobj["label_instrumentalness"])
        label.append(jsonobj["label_key"])
        label.append(jsonobj["label_loudness"])
        label.append(jsonobj["label_mode"])
        label.append(jsonobj["label_speechiness"])
        label.append(jsonobj["label_tempo"])
        label.append(jsonobj["label_time_signature"])
        label.append(jsonobj["label_valence"])
    except:
        pass

    try:
        train.append(jsonobj["username"])
    except:
        train.append("")

    return train, label

def train_entire_model():
    ########################## Input File ##########################

    f = open("train_data.txt", "r")
    lines = f.readlines()
    instances = [l.strip() for l in lines]

    jsoninstances = []

    for instance in instances:
        instance = instance.replace('\'', '\"')
        jsoninstances.append(json.loads(instance))

    # get usernames here

    # datasets w different usernames

    ########################## Extract Data features ##########################


    ########### Get training instances ###########


    
    list_usernames = {'': [[], []]} # [[train], [label]]
    for j in jsoninstances:
        t, l = getTrainArray(j)
        username = t[-1]

        if(username in list_usernames):
            if(len(l) != 11):
              continue
            print(t[0:-1])
            list_usernames[username][0].append(t[0:-1])  
            list_usernames[username][1].append(l)  
            list_usernames[''][0].append(t[0:-1])  
            list_usernames[''][1].append(l)  
        else:
            list_usernames[username] = [[], []]
            list_usernames[username][0].append(t[0:-1])  
            list_usernames[username][1].append(l)  
            list_usernames[''][0].append(t[0:-1])  
            list_usernames[''][1].append(l)  
    
    # train = np.array(train)
    # y_label_values = []
    train = []
    label = []
    
    for username in list_usernames:
        train = np.array(list_usernames[username][0])
        label = np.array(list_usernames[username][1])


        if(len(train) < 2):
            continue

        def train_lin_model(label_index):
            y_label_values = []
            for y_label in label:
                y_label_values.append(y_label[label_index])

            y_label_values = np.array(y_label_values)

            model = LinearRegression(normalize=True)
            reg = model.fit(train, y_label_values)
            score = reg.score(train, y_label_values)
            return reg, score, model

        for label_index in range(len(label_names)):
            reg, score, model = train_lin_model(label_index)
            print(label_names[label_index] + " Score = " + str(score))

            filename = username +"_" + label_names[label_index] + '.model'
            pickle.dump(model, open(filename, 'wb'))

    return
    ########### Train models ###########

    def train_lin_model(label_index):
        y_label_values = []
        for y_label in label:
            y_label_values.append(y_label[label_index])

        y_label_values = np.array(y_label_values)

        model = LinearRegression()
        reg = model.fit(train, y_label_values)
        score = reg.score(train, y_label_values)
        return reg, score, model

    for label_index in range(len(label_names)):
        reg, score, model = train_lin_model(label_index)
        print(label_names[label_index] + " Score = " + str(score))

        filename = label_names[label_index] + '.model'
        pickle.dump(model, open(filename, 'wb'))

# features is just a single dim array of features
def predict_w_features(features, modelname = ""):
    results = {}
    for i in range(len(label_names)):
        inputs = [features]
        loaded_model = pickle.load(open(modelname + "_" + label_names[i] + ".model", 'rb'))
        result = loaded_model.predict(inputs)
        results[label_names[i]] = result[0]
        print(label_names[i] + " predicted result = " + str(result))
    return results

def predict(jsonobj):
    username = jsonobj['username']
    input, _ = getTrainArray(jsonobj)
    # jsonobj.getAsJsonObject.remove("email")
    input = input[0:-1]
    # del input['username'] 
    prediction = predict_w_features(input, username)
    return prediction

#train_entire_model()
#predict_w_features([1, 0.0 , 0, 0, 0, 0.5, 0.5, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
#predict_w_features([0, 1, 1, 0, 1, 0, 0, 0.8, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1.0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

#train_entire_model()
