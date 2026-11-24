# 🎲 Gra w Pytania i Wyzwania +18

Aplikacja imprezowa z interfejsem Angular i API Flask. Flask serwuje gotowy frontend z katalogu `static/` oraz pytania, wyzwania i zasady z plików JSON.

## Architektura

Wdrożenie składa się z **jednego kontenera `web`** zawierającego aplikację Python, frontend i dane JSON. Projekt nie korzysta z Redis ani PostgreSQL, więc nie uruchamia dla nich dodatkowych kontenerów ani nie łączy się z usługami na hoście. Clojure nie jest używany.

JSON-y są statycznym źródłem treści gry, a nie trwałą bazą danych. Losowania nie wymagają kolejki ani współdzielonego cache.

## Uruchomienie przez Docker Compose

Wymagany jest Docker z Docker Compose.

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f web
```

Aplikacja będzie dostępna pod adresem <http://localhost:13001>. Zatrzymanie:

```bash
docker compose down
```

Compose buduje jeden obraz i uruchamia jeden serwis. Kontener działa jako użytkownik bez roota, z systemem plików tylko do odczytu i bez dodatkowych capabilities. Compose nie dodaje mapowania `host.docker.internal` ani nie montuje katalogu projektu z hosta.

## Uruchomienie lokalne bez Dockera

```bash
python -m pip install -r requirements.txt
python app.py
```

Serwer nasłuchuje na porcie `13001`.

## Funkcje

- Losowanie pytań i wyzwań przez API.
- Tajne zadania oraz endpoint z zasadami gry.
- Responsywny interfejs Angular serwowany przez Flask.

## Treść

Aplikacja jest przeznaczona dla osób pełnoletnich (18+). Zawartość pytań i wyzwań ma charakter rozrywkowy.
