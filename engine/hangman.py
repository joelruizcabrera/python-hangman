from flask import Flask, request, jsonify, abort
import random as rd
import uuid
import json

# initialize Flask-Server
app = Flask(__name__)

# initialize variables
wrong_guesses = []
limit_guesses = 0
count = 0
wrong_count = 10

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

    getRandomWord()

    response = {
        "gameId": gameId,
        "status": 200,
        "data": data
    }

    startGame(userName, gameId)

    return response

def startGame(userName, gameId):
    print("\n----------------------------\nInitialize new Game")
    print("Game ID: " + str(gameId) + "\nUsername: " + userName)

    gamePreData = {
        "id": str(gameId),
        "username": userName,
        "statistics": []
    }

    gotData = {}

    with open('data/gameData.json', 'r') as jsonGameData:
        gotData = json.load(jsonGameData)

    gotData["games"].append(gamePreData)

    with open('data/gameData.json', 'w') as jsonGameData:
        json.dump(gotData, jsonGameData, indent=4)

def getRandomWord():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
