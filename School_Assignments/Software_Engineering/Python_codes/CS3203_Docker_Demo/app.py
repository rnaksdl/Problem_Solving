from flask import Flask
import os
audience = os.environ['AUDIENCE']
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, ' + audience