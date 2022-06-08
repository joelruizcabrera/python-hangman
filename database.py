import mysql
import mysql.connector

db = mysql.connector.connect(host = "127.0.0.1",
                                    user = "root",
                                    passwd = "",
                                    db = "hangman")

cursor = db.cursor()

cursor.execute("SELECT * from Test")

ergebnis = cursor.fetchall()

cursor.close()

for data in ergebnis:

    print ("Nummer: " + str(data[0]) + "; Text: " + data[1])

db.close()