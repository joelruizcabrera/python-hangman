import mysql
import mysql.connector

# SQL Connection try
db = mysql.connector.connect(host = "127.0.0.1",
                                    user = "root",
                                    passwd = "",
                                    db = "hangman")

# Fetching data
stmt = db.cursor()
stmt.execute("SELECT * from hang_words")
results = stmt.fetchall()

stmt.close()

# Go into words
for hangmanWord in results:
    print ("ID: " + str(hangmanWord[0]) + "\nSchwierigkeit: " + str(hangmanWord[1]) + "\nWort: " + hangmanWord[2] + "\n------------------------------------")

db.close()