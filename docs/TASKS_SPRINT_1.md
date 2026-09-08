# 🚀 SaldoFlow – Sprint 1 Aufgabenpakete
**Projekt:** Modulares Haushaltsbuch (AnwP)  
**Zeitraum:** Vormittag (09:35 – 12:40 Uhr)  
**Ziel:** Lauffähiges MVP (Einnahme/Ausgabe erfassen, in SQLite speichern & Saldo im Web-UI anzeigen)

---

### 📌 Aufgabe 1: Projekt-Setup & Flask-Factory
**Verantwortlich:** Teamleiter (Architecture & Integration)

* **Ziel:** Projektstruktur aufsetzen, Abhängigkeiten definieren und Flask-App-Factory bereitstellen.
* **Erforderliche Dateien:**
  * `requirements.txt` (`flask`, `pytest`)
  * `.gitignore`
  * `src/__init__.py`
  * `src/web/__init__.py` (Flask Application Factory `create_app()`)
  * `src/web/routes.py` (Flask-Routen `GET /` und `POST /add`)
  * `run.py` (Startskript)
* **Zusatzaufgabe:** Support für das Team bei Import- oder Pfadproblemen.

---

### 📌 Aufgabe 2: Domänenmodelle (OOP Business-Logik)
**Verantwortlich:** Entwickler A (Domänenlogik)

* **Ziel:** Reine Python-Klassen für Einnahmen, Ausgaben und Saldo-Berechnung ohne Framework-Abhängigkeiten schreiben.
* **Zieldatei:** `src/domain/models.py`
* **Anforderungen:**
  1. **Basisklasse `Transaction`:** Attribute `id`, `description`, `amount`, `category`, `date`.
  2. **Unterklassen `Income` und `Expense`:** Erben von `Transaction`.
  3. **Verwaltungsklasse `BudgetBook`:**
     * `transactions = []` (Liste aller Buchungen)
     * `add_transaction(transaction)`
     * `get_total_income()` -> Summe aller Einnahmen
     * `get_total_expense()` -> Summe aller Ausgaben
     * `get_total_balance()` -> Einnahmen minus Ausgaben
* **Test:** Am Dateiende `if __name__ == '__main__':` einfügen und im Terminal mit Beispieldaten testen.

---

### 📌 Aufgabe 3: SQLite Datenbank & Repository-Pattern
**Verantwortlich:** Entwickler B (Persistenz & DB)

* **Ziel:** SQLite-Datenbank aufsetzen und CRUD-Operationen kapseln.
* **Zieldateien:** `src/persistence/schema.sql` & `src/persistence/repository.py`
* **Anforderungen:**
  1. **`schema.sql`:** Erstelle Tabelle `transactions`:
     * `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
     * `title` (TEXT)
     * `amount` (REAL)
     * `type` (TEXT: 'income'/'expense')
     * `category` (TEXT)
     * `created_at` (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
  2. **Klasse `TransactionRepository` (`repository.py`):**
     * Nutze Standardbibliothek `import sqlite3`.
     * `init_db()` -> Führt `schema.sql` aus (falls DB-Datei fehlt).
     * `save(type, title, amount, category)` -> Fügt Buchung ein.
     * `get_all()` -> Holt alle Einträge als Liste/Dicts.
     * `delete_by_id(id)` -> Löscht Eintrag nach ID.
* **Test:** Am Dateiende `if __name__ == '__main__':` einfügen und DB-Befehle im Terminal testen.

---

### 📌 Aufgabe 4: Web-Frontend & Pico.css Templates
**Verantwortlich:** Entwickler C (Frontend & UI)

* **Ziel:** Responsive HTML5-Oberfläche mit Formular und Saldo-Übersicht erstellen.
* **Zieldateien:** `src/web/templates/base.html` & `src/web/templates/index.html`
* **Anforderungen:**
  1. **`base.html`:** HTML5-Grundgerüst mit Pico.css CDN-Link im `<head>`:
     ```html
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
     ```
  2. **`index.html`:**
     * **Karten-Übersicht:** 3 Boxen für *Gesamtsaldo*, *Einnahmen*, *Ausgaben* (Jinja2-Variablen: `{{ balance }}`, `{{ total_income }}`, `{{ total_expense }}`).
     * **Formular:** POST an `/add` mit Feldern: Typ (Income/Expense), Titel, Betrag, Kategorie.
     * **Transaktionstabelle:** Tabelle mit Schleife `{% for t in transactions %}` zur Anzeige der bisherigen Buchungen.
* **Test:** `index.html` direkt im Browser öffnen und Design/Layout prüfen.

---


