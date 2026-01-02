# 🎲 Gra w Pytania i Wyzwania +18

Kompleksowa aplikacja webowa typu "Party Game", zaprojektowana jako nowoczesne narzędzie rozrywkowe na spotkania towarzyskie. Projekt łączy backend w **Pythonie (Flask)** z dynamicznym frontendem w **Angularze**.

![Status](https://img.shields.io/badge/Status-MVP-success)
![Target](https://img.shields.io/badge/Audience-18%2B-red)
![Tech](https://img.shields.io/badge/Stack-Angular_%2B_Python-blue)

## 🎯 Cel i Kontekst Projektu

Celem projektu było stworzenie skalowalnej aplikacji webowej, która odchodzi od statycznych stron na rzecz architektury **Client-Server**. Aplikacja oferuje płynne doświadczenie użytkownika (UX), obsługę różnych trybów gry oraz dynamiczne ładowanie treści z bazy danych.

### ⚠️ Nota dotycząca treści
**Aplikacja jest projektem skierowanym do osób pełnoletnich (18+).**
Ze względu na specyfikę gatunku "Truth or Dare", baza danych zawiera treści o charakterze bezpośrednim, satyrycznym i kontrowersyjnym, dostosowanym do docelowej grupy odbiorców.

> **Dla Rekruterów / Code Reviewers:**
> Proszę o ocenę projektu przez pryzmat **umiejętności technicznych, architektury i jakości kodu**. Warstwa tekstowa aplikacji (pytania/wyzwania) stanowi jedynie "wsad danych" (content placeholder) mający na celu odwzorowanie realnego scenariusza użycia aplikacji na imprezach dla dorosłych i nie powinna wpływać na ocenę kompetencji inżynieryjnych autora. Dodatkowo aplikacja była ***tworzona w 2 dni*** na impreze sylwestrową

## 🛠️ Stack Technologiczny

### Backend (API Logic)
* **Python 3.13 / Flask:** Lekkie REST API obsługujące logikę losowania.
* **Struktura danych:** JSON (jako szybka baza NoSQL dla wersji MVP).

### Frontend (User Interface)
* **Angular 21:** Wykorzystanie najnowszych funkcji frameworka.
* **TypeScript:** Pełne typowanie dla zachowania spójności kodu.
* **Angular Material / SCSS:** Responsywny design (Mobile First), dostosowany do obsługi na telefonach podczas rozgrywki.

## 🚀 Kluczowe Funkcjonalności

1.  **Dynamic Content Loading:** Asynchroniczne pobieranie pytań bez przeładowania strony.
2.  **Tryb "Tajne Zadania":** Mechanika ukrytych wyzwań z osobnym widokiem.
3.  **Responsywność:** Interfejs zoptymalizowany pod ekrany dotykowe.

## ⚙️ Instalacja i Uruchomienie

Projekt składa się z dwóch niezależnych modułów (Backend i Frontend), które należy uruchomić równolegle.

### 1. Backend (Python Flask + Angular build)
```bash
# W katalogu głównym backendu
pip install flask
python app.py # Serwer wystartuje na http://localhost:13001 (we wzgladu na cel ustawiony w Angular skorzysta on z mojego serwera backend do zapytań) 
