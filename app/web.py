from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        users = requests.get('http://api:5000/').text
        user_list = users.split(', ')
        return render_template('index.html', users=user_list)
    except requests.exceptions.RequestException as e:
        return f"Error connecting to the API: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)