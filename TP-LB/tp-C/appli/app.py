# tp-C/appli/app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    container_id = os.environ.get('HOSTNAME')
    return f'Serveur {container_id}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
