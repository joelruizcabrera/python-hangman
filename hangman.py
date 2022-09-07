from flask import Flask, request, jsonify, abort
import random as rd
import uuid

# initialize Flask-Server
app = Flask(__name__)

# initialize variables
wrong_guesses = []
limit_guesses = 0
count = 0
wrong_count = 10


# definiere Route für Hauptseite
# - generiert eine uuid
# - ein wort wird generiert
# - Länge der Liste
@app.route('/api/v1/start', methods=['GET'])
def startgame():
    # playername
    playername = input('Geben sie ihren Namen ein: ')

    # uuid
    id = uuid.uuid4()

    # get the guessword
    word_list = ['Auto', 'Wetter', 'Schwein']
    item_index = rd.randint(0, 2)  # display the selection item in each category
    correct_word = str(word_list[item_index])
    correct_word_list = list(correct_word)
    print(correct_word_list)

    # length of correct_word_list
    correct_word_list_length = len(correct_word_list)
    print(correct_word_list_length)

    # list that the player sees
    display_list = [char.replace(char, '_') for char in correct_word]  # displaying to the users

    return jsonify(playername, correct_word_list, id, correct_word_list_length), 200


@app.route('/api/v1/{uuid}/add/{player_guess}', methods=['POST'])
def user_input(correct_word_list, display_list, wrong_count):
    global limit_guesses, count

    def result():
        if '_' not in display_list:
            print('Gewonnen! Du hast ' + str(count) + 'Versuche benötigt'), quit()
        if wrong_count <= 0:
            print('Verloren! Du bist gehängt worden!')

    while True:
        # input guess
        player_guess = input('Bitte gebe einen Buchstaben ein: ')
        # validation of the input guess
        if len(player_guess) > 1:
            print('Nur ein Buchstabe eingeben!')
            player_guess = input('Bitte gebe einen Buchstaben ein: ')
        for item in correct_word_list:
            count += 1
            if item == player_guess:
                guess_index = correct_word_list.index(player_guess)  # finding the index of the correct alphabet
                correct_word_list[guess_index] = '-'
                display_list[guess_index] = player_guess  # replace the dash with the correct alphabet user had input
                result()
            else:
                wrong_count -= 1
                if player_guess not in wrong_guesses:
                    wrong_guesses.append(player_guess)
                    wrong_guesses.sort()
                    result()
                else:
                    result()

        return jsonify(guess_index), 200


# - gibt den wert einer Bestenliste zurück
@app.route('/api/v1/board', methods=['GET'])
def board():
    pass


if __name__ == '__main__':
    # starte Flask-Server
    app.run(host='0.0.0.0', port=5000)
