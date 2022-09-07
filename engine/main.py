import random

from flask import Flask, request
import uuid
import json

# initialize Flask-Server
app = Flask(__name__)

config = {
    "apiVersion": "1",
    "apiPrefix": "api"
}

apiUrlPrefix = "/" + config["apiPrefix"] + "/v" + config["apiVersion"] + "/"

@app.route(apiUrlPrefix + 'start', methods=['POST'])
def initGame():
    data = request.get_json()

    userName = data["userName"]
    gameId = uuid.uuid4()

    word = getRandomWord()

    response = {
        "gameId": gameId,
        "status": 200,
        "word": word,
        "data": data
    }

    startGame(userName, gameId, word)

    return response

def startGame(userName, gameId, word):
    print("\n----------------------------\nInitialize new Game")
    print("Game ID: " + str(gameId) + "\nUsername: " + userName + "\n" + word + "\n")

    gamePreData = {
        "id": str(gameId),
        "username": userName,
        "word": word,
        "data": {
            "trys": 0,
            "usedLetter": [],
            "lifes": 12
        }
    }

    gotData = {}

    with open('data/gameData.json', 'r') as jsonGameData:
        gotData = json.load(jsonGameData)

    gotData["games"].append(gamePreData)

    with open('data/gameData.json', 'w') as jsonGameData:
        json.dump(gotData, jsonGameData, indent=4)

def getRandomWord():
    words = []
    with open('data/words.json', 'r') as jsonWords:
        words = json.load(jsonWords)['words']

    randIndex = random.randint(0, len(words))
    return words[randIndex]

@app.route(apiUrlPrefix + '/add', methods=['POST'])
def addLetter():
    data = request.get_json()

    gameId = data["gameId"]
    letter = data["letter"]

    with open('data/gameData.json', 'r') as jsonGameData:
        data = json.load(jsonGameData)["games"]
        for game in data:
            if game["id"] == gameId:
                isContaining = checkIfLetterContains(game["word"], letter)
                if isContaining == True:
                    res = letterSuccess(gameId, letter, game["data"], data.index(game))
                    return res
                else:
                    res = letterDenied(gameId, letter, game["data"], data.index(game))
                    return res
            else:
                return error("Something went wrong")

def checkIfLetterContains(word, letter):
    if letter.lower() in word.lower():
        return True
    else:
        return False

def letterSuccess(gameId, letter, data, dataIndex):
    if letter not in data["usedLetter"]:
        data["usedLetter"].append(letter.lower())
    data["trys"] = data["trys"] + 1

    jsonFile = {}

    with open('data/gameData.json', 'r') as jsonGameData:
        jsonFile = json.load(jsonGameData)


    jsonFile['games'][dataIndex]["data"] = data

    with open('data/gameData.json', 'w') as jsonGameData:
        json.dump(jsonFile, jsonGameData, indent=4)

    return {
        "status": 2,
        "letter": letter,
        "lifes": data["lifes"],
        "trys": data["trys"],
        "gameId": gameId,
    }
def letterDenied(gameId, letter, data, dataIndex):
    data["usedLetter"].append(letter.lower())
    data["trys"] = data["trys"] + 1
    if data["lifes"] > 1:
        data["lifes"] = data["lifes"] - 1
    elif data["lifes"] == 1:
        data["lifes"] = data["lifes"] - 1
        isDead(data["lifes"], gameId)
    else:
        isDead(data["lifes"], gameId)

    jsonFile = {}

    with open('data/gameData.json', 'r') as jsonGameData:
        jsonFile = json.load(jsonGameData)

    jsonFile['games'][dataIndex]["data"] = data

    with open('data/gameData.json', 'w') as jsonGameData:
        json.dump(jsonFile, jsonGameData, indent=4)

    return {
        "status": 1,
        "letter": letter,
        "lifes": data["lifes"],
        "trys": data["trys"],
        "gameId": gameId,
    }

def error(msg):
    return {
        "status": "ERROR",
        "message": msg
    }

def isDead(trys, gameId):
    return {
        "status": 0,
        "trys": data["trys"],
        "gameId": gameId,
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
