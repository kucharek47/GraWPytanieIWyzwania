import json
import random
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

pytania_lista = json.load(open('pytania.json', encoding='utf-8'))
wyzwania_lista = json.load(open('wyzwania.json', encoding='utf-8'))
tajne_zadania_lista = json.load(open('tajne_zadania.json', encoding='utf-8'))


@app.route('/api/pytanie', methods=['GET'])
def pytania():
    wynik = random.choice(pytania_lista)
    return jsonify(wynik)
@app.route('/api/wyzwania', methods=['GET'])
def wyzwania():
    cos = random.randint(0,100)
    print(cos)
    if cos > 20:
        wynik = random.choice(wyzwania_lista)
        wynik["tajne"] = False
    else:
        wynik = random.choice(tajne_zadania_lista)
        wynik["tajne"] = True
    return jsonify(wynik)

if __name__ == '__main__':
    app.run()
