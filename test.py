# this file will test if flask is installed and working.

from flask import Flask
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    return "Welcome to the OSU CS 340 - Flask Tutorial!"

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 2019)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port) 
