# 🚀 SaldoFlow – Sprint 1 Aufgabenpakete & Kochrezepte

**Projekt:** Modulares Haushaltsbuch (AnwP)  
**Zeitraum:** Vormittag (09:35 – 12:40 Uhr)  
**Ziel:** Lauffähiges MVP (Einnahme/Ausgabe erfassen, in SQLite speichern & Saldo im Web-UI anzeigen)

---

## ⚡ SCHRITT 0: Für ALLE Teammitglieder (Git Setup & Branching)

Jedes Teammitglied führt zum Start des Sprints folgende Befehle im Terminal aus:

- [ ] **1. Neuesten Code vom Teamleiter holen:**
  ```bash
  git checkout main
  git pull origin main
  ```
- [ ] **2. Eigenen Feature-Branch erstellen und wechseln:**
  * **Teamleiter:** `git checkout -b feature/flask-routes`
  * **Entwickler A:** `git checkout -b feature/domain-models`
  * **Entwickler B:** `git checkout -b feature/sqlite-repository`
  * **Entwickler C:** `git checkout -b feature/pico-templates`

---

## 👨‍💻 KOCHREZEPTE NACH ROLLEN

---

### 📌 Aufgabe 1: Projekt-Setup & Flask-Factory (Kochrezept)
**Verantwortlich:** Teamleiter (Architecture & Integration)  
**Branch:** `feature/flask-routes`

- [ ] **Schritt 1:** Virtuelle Umgebung aktivieren & Abhängigkeiten in `requirements.txt` sicherstellen (`flask`, `pytest`).
- [ ] **Schritt 2:** Flask-Factory in `src/web/__init__.py` schreiben (`create_app()`).
- [ ] **Schritt 3:** Hauptrouten in `src/web/routes.py` anlegen:
  * `GET /` -> Rendert `index.html` mit Saldo, Einnahmen, Ausgaben und Transaktionsliste.
  * `POST /add` -> Nimmt Formular-Daten entgegen und übergibt sie an das Repository.
- [ ] **Schritt 4:** `run.py` im Wurzelverzeichnis testen: `python run.py`.
- [ ] **Schritt 5:** Team-Support & Code-Integration (Merge der Feature-Branches der Entwickler A, B, C auf `main`).

---

### 📌 Aufgabe 2: Domänenmodelle (OOP Business-Logik)
**Verantwortlich:** Entwickler A (Domänenlogik)  
**Branch:** `feature/domain-models`  
**Zieldatei:** `src/domain/models.py`

- [ ] **Schritt 1:** Datei `src/domain/models.py` erstellen.
- [ ] **Schritt 2:** Basisklasse `Transaction` schreiben:
  * Attribute: `id`, `title`, `amount`, `category`, `date`.
- [ ] **Schritt 3:** Unterklassen `Income` und `Expense` anlegen (Erben von `Transaction`).
- [ ] **Schritt 4:** Verwaltungsklasse `BudgetBook` erstellen:
  * `transactions = []` (Liste aller Buchungen)
  * Methode `add_transaction(transaction)`
  * Methode `get_total_income()` -> Summe aller Einnahmen
  * Methode `get_total_expense()` -> Summe aller Ausgaben
  * Methode `get_total_balance()` -> Einnahmen minus Ausgaben
- [ ] **Schritt 5 (Test):** Am Dateiende `if __name__ == '__main__':` einfügen, Beispiel-Objekte erstellen und Summen im Terminal ausgeben lassen.
- [ ] **Schritt 6 (Git Push):**
  ```bash
  git add src/domain/models.py
  git commit -m "feat: Domänenmodelle und BudgetBook Logik implementiert"
  git push origin feature/domain-models
  ```

---

### 📌 Aufgabe 3: SQLite Datenbank & Repository-Pattern
**Verantwortlich:** Entwickler B (Persistenz & DB)  
**Branch:** `feature/sqlite-repository`  
**Zieldateien:** `src/persistence/schema.sql` & `src/persistence/repository.py`

- [ ] **Schritt 1:** Datei `src/persistence/schema.sql` anlegen & SQL-Tabelle `transactions` definieren:
  * `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  * `title` (TEXT NOT NULL)
  * `amount` (REAL NOT NULL)
  * `type` (TEXT NOT NULL) -- 'income' oder 'expense'
  * `category` (TEXT)
  * `created_at` (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
- [ ] **Schritt 2:** Datei `src/persistence/repository.py` anlegen & Klasse `TransactionRepository` erstellen.
- [ ] **Schritt 3:** Methoden in `TransactionRepository` implementieren:
  * `init_db()` -> Liest `schema.sql` ein und führt `executescript()` auf `saldoflow.db` aus.
  * `save(type, title, amount, category)` -> `INSERT INTO transactions ...`
  * `get_all()` -> `SELECT * FROM transactions ORDER BY created_at DESC`
  * `delete_by_id(id)` -> `DELETE FROM transactions WHERE id = ?`
- [ ] **Schritt 4 (Test):** Am Dateiende `if __name__ == '__main__':` einfügen, `init_db()` aufrufen, Test-Daten einfügen und per `get_all()` auf der Konsole ausdrucken.
- [ ] **Schritt 5 (Git Push):**
  ```bash
  git add src/persistence/
  git commit -m "feat: SQLite Schema und Repository Pattern erstellt"
  git push origin feature/sqlite-repository
  ```

---

### 📌 Aufgabe 4: Web-Frontend & Pico.css Templates
**Verantwortlich:** Entwickler C (Frontend & UI)  
**Branch:** `feature/pico-templates`  
**Zieldateien:** `src/web/templates/base.html` & `src/web/templates/index.html`

- [ ] **Schritt 1:** Ordner `src/web/templates/` anlegen (falls nicht vorhanden).
- [ ] **Schritt 2:** Base-Template `base.html` erstellen:
  * HTML5-Grundgerüst.
  * Pico.css per CDN-Link im `<head>` einbinden:
    `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">`
  * Jinja2 Block `{% block content %}{% endblock %}` definieren.
- [ ] **Schritt 3:** `index.html` erstellen (erbt von `base.html` mit `{% extends 'base.html' %}`):
  * **Karten/Grid-Übersicht (3 Boxen):** Gesamtsaldo (`{{ balance }}`), Einnahmen (`{{ total_income }}`), Ausgaben (`{{ total_expense }}`).
  * **Eingabeformular (`<form action="/add" method="POST">`):**
    * Feld `type` (Select: Einnahme / Ausgabe)
    * Feld `title` (Text)
    * Feld `amount` (Number, step="0.01")
    * Feld `category` (Text)
    * Submit-Button ("Buchen")
  * **Tabelle der Buchungen:**
    * Schleife `{% for t in transactions %}` für Reihen.
- [ ] **Schritt 4 (Test):** `index.html` im Browser öffnen und Layout/Responsive-Design prüfen.
- [ ] **Schritt 5 (Git Push):**
  ```bash
  git add src/web/templates/
  git commit -m "feat: Base und Index Templates mit Pico.css und Jinja2 Variablen erstellt"
  git push origin feature/pico-templates
  ```
