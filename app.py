import PySimpleGUI as sg
from googletrans import Translator, constants
from bs4 import BeautifulSoup
import requests
import googletrans
translator = Translator()


# Add some color
# to the window
sg.theme('SandyBeach')
l = googletrans.LANGUAGES
langlist = []
testt = {}
for language in l:
    langlist.append(l[language])
    testt[l[language]] = language

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
    [sg.Text('Please enter the article name')],
    [sg.Text('Article Name', size=(15, 1)), sg.InputText()],
    [sg.Text('Language', size=(15, 1)), sg.Combo(langlist, size=(10, 1))],
    [sg.Submit(), sg.Cancel()],
    [sg.Text("Display Translated Text:")],
    [sg.Multiline(size=(100, 20), key='textbox')]
]

window = sg.Window('Language data entry window', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event == 'Submit':
        if values[0] == '':
            sg.Popup("Article Name is Empty")
        elif values[1] == '':
            sg.Popup("Select a Language")
        else:
            source = requests.get('https://en.wikipedia.org/wiki/' + values[0]).text
            soup = BeautifulSoup(source, 'lxml')
            body = soup.find('body')
            content = body.find('div', class_='mw-content-ltr').text
            translation = translator.translate(content, dest=testt[values[1]])
            print(translation)

            window['textbox'].update(translation.text)
    if event == 'Cancel':
        window.Close()

    if event in (None, 'Exit'):
        break

window.Close()
