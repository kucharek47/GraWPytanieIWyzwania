import json
import random
from flask_cors import CORS
from flask import Flask, jsonify, render_template, abort, send_from_directory
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

pytania_lista = json.load(open('pytania.json', encoding='utf-8'))
wyzwania_lista = json.load(open('wyzwania.json', encoding='utf-8'))
tajne_zadania_lista = json.load(open('tajne_zadania.json', encoding='utf-8'))
zasady_tekst = """
1.	Czas na wykonanie zadania tajnego to max 15 min (nie możesz zostać przyłapany).
2.	Osoba, która skłamię w pytaniu, a ktoś ją na tym przyłapie pije podwójna liczbę szotów niż te pokazane przy pytaniu. Osoba która przyłapała nie musi pić tylu szotów ile warte jest pytanie.
3.	Za zmianę wylosowanej osoby pijesz karnego szota.
4.	Nikt nie może się dowiedzieć jakie miałeś tajne wyzwanie podczas gry dlaczego pamiętaj aby je ukrywać (klikniecie w pole tekstowe), na koniec wszystkie zostaną ujawnione i rozliczone (jeśli nie chcesz go wykonać pokazujesz i pijesz od razu w swojej kolejce).
5.	Pijesz podaną liczbę szotów jeżeli nie chcesz wykonać zadania lub nie dasz rady.
6.	Przy jednomyślnym przegłosowaniu można zmienić liczbę szotów w danym pytaniu lub wyzwaniu.
7.	Nie możesz wziąć więcej niż 3 razy tej samej opcji (pytanie/wyzwanie).
8.	Jest możliwości wylosowania jednego kielisza wiecej lub mniej kiedy ma sie 2 (kilknij na kieliszki)
9.	Za każde czepianie się apki, osoba czepiająca pije karnego szota!
"""

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
        if cos > 5:
            wynik = random.choice(tajne_zadania_lista)
        else:
            wynik = {"ilosc_shotow":1, "tresc":"Masz szczęście i nic nie robisz"}
        wynik["tajne"] = True
    return jsonify(wynik)
@app.route('/api/zasady', methods=['GET'])
def zasady():
    return jsonify({"tresc": str(zasady_tekst)})

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>')
def spa_fallback(path):
    if path.startswith('api'):
        abort(404)

    full_path = os.path.join(app.static_folder, path)
    if os.path.isfile(full_path):
        return send_from_directory(app.static_folder, path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=13001)
