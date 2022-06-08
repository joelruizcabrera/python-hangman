import mysql
import mysql.connector

#Verbindung zur MySQL Datenbank herstellen
db = mysql.connector.connect(host = "127.0.0.1",
                                    user = "root",
                                    passwd = "",
                                    db = "hangman")

#Cursor zur Ausführung von SQL Statements einrichten
cursor = db.cursor()

#Ausführen von SQL Statements
cursor.execute("SELECT * from Test")

#Auslesen von Daten und Speichern in einer Variable
ergebnis = cursor.fetchall()

cursor.close()

#Ausgabe der Daten aus der Variable
for data in ergebnis:

    print ("Nummer: " + str(data[0]) + "; Text: " + data[1])

db.close()