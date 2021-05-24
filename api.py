from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from scrapper import *


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/scrape', methods=['GET', 'POST'])
def api():
    try:
        player = request.args['name']
        web_scrapper("keyword")
    except:
        pass



if __name__ == '__main__':
    app.run(debug=True)
