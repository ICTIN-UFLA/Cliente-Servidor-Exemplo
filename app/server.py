from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='mydatabase'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return ' ' + ', '.join([str(user[1]) for user in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
