import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='megapint',
        password='wine',
        database='flight_game'
    )
    print("Connected successfully!")
    conn.close()
except mysql.connector.Error as e:
    print("Error:", e)