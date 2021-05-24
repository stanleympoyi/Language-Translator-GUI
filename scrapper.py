from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import requests


def web_scrapper(keyword):
    path = 'https://en.wikipedia.org/wiki/'
    source = requests.get(path + keyword).text
    soup = BeautifulSoup(source, 'lxml')
    body = soup.find('body')
    content = body.find('div', class_='mw-content-ltr').text

    return content

