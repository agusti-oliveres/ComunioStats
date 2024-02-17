from flask import Flask, render_template
from flask import request as f_request

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import json


app = Flask(__name__)

def get_data(username, password):
    # GET TOKEN
    s = requests.session()
    req = s.post(
        "https://www.comunio.es/api/login",
        data = {
            'username': str(username),
            'password': str(password),
            'tzoffset': '1'
        },
    )
    token = json.loads(req.content)['access_token']
    
    res = s.get(
        'https://www.comunio.es/api/',
        headers= {'authorization': f'Bearer {token}'}
    )
    d = json.loads(res.content)

@app.route('/', methods=['GET', 'POST'])
def login():
    if f_request.method == 'POST':
        username = f_request.form['username']
        password = f_request.form['password']



        # # Dummy authentication (replace it with proper authentication logic)
        # if any(user['username'] == username and user['password'] == password for user in users):
        #     return "Logged in successfully!"  # Redirect to dashboard or another page
        # else:
        #     return "Invalid username or password. Try again."

    return render_template(
        "index.html"
        )

if __name__ == '__main__':
    app.run(debug=True)
