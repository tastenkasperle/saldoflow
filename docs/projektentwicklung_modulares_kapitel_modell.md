# 📘 Projektentwicklung & Vorgehensmodell

## 🎯 Leitphilosophie: Modulares Kapitel-Modell (Agile Light)

> **Kernprinzip:** *Übersicht, Kontrolle und Lerneffekt stehen an erster Stelle.*  
> Wir verzichten bewusst auf unübersichtliche Scrum-Bürokratie und künstliche Doppelrollen. Stattdessen bauen wir die Anwendung **schrittweise in isolierten, in sich geschlossenen Kapiteln** auf. Ein Kapitel wird erst abgeschlossen und im Team verstanden, bevor das nächste begonnen wird.

---

## 👥 Modul-Verantwortlichkeiten (4er-Team)

Statt theoretischer Scrum-Doppelrollen hat jedes Teammitglied die klare Patenschaft für ein Fachmodul:

* **Projektleitung & Systemarchitektur:**  
  *(Verantwortung: Gesamtarchitektur, Ordnerstruktur, Modulintegration, Start-Skripte, Teamkoordination)*
* **Modul Domänenlogik (OOP):**  
  *(Verantwortung: Reine Geschäftslogik in Python, Objektmodellierung `Transaction`, `Income`, `Expense`, `BudgetBook`)*
* **Modul Persistenz (SQLite & Repository):**  
  *(Verantwortung: Datenbankschema `schema.sql`, CRUD-Operationen im `TransactionRepository`)*
* **Modul Präsentation (Web-UI & UX):**  
  *(Verantwortung: HTML5-Templates mit Pico.css, Usability, Jinja2-Dashboard)*

---

## 🧩 Das 4-Kapitel-Entwicklungsmodell

```text
┌─────────────────────────────────────────────────────────────────┐
│ KAPITEL 1: Domänenmodellierung (OOP Kernlogik)                  │
│ Ziel: Reine Python-Klassen & Unittests (100% ohne DB / Web)     │
└─────────────────────────────────────────────────────────────────┘
                                │ (Fertig & im Team verstanden)
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│ KAPITEL 2: Persistenzschicht (SQLite & Repository)              │
│ Ziel: Entkoppeltes TransactionRepository & DB-Funktionen        │
└─────────────────────────────────────────────────────────────────┘
                                │ (Fertig & im Team verstanden)
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│ KAPITEL 3: Web-Präsentationsschicht (Flask & Pico.css)          │
│ Ziel: Flask-App Factory, Routes & Jinja2 Web-Dashboard          │
└─────────────────────────────────────────────────────────────────┘
                                │ (Fertig & im Team verstanden)
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│ KAPITEL 4: Usability & Packaging (1-Klick-Starter)             │
│ Ziel: start.bat / start.sh & finale Projektdokumentation        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📖 Detailübersicht der Kapitel

### 1️⃣ Kapitel 1: Domänenmodell (OOP Kernlogik)
* **Fokus:** Objektorientierte Programmierung in reinem Python.
* **Ergebnis:** `src/domain/models.py` funktioniert vollständig isoliert.
* **Qualitätscheck:** Unittests für Saldo-, Einnahmen- und Ausgabenberechnungen laufen grün durch. Jeder im Team versteht die Klassenstruktur.

### 2️⃣ Kapitel 2: Datenpersistenz (SQLite & Repository-Pattern)
* **Fokus:** Dauerhafte Datenspeicherung ohne Verflechtung mit der Kernlogik.
* **Ergebnis:** `src/persistence/schema.sql` und `src/persistence/repository.py`.
* **Qualitätscheck:** Einnahmen/Ausgaben können per Skript in SQLite gespeichert, ausgelesen und gelöscht werden.

### 3️⃣ Kapitel 3: Web-UI & Integration (Flask & Pico.css)
* **Fokus:** Zusammenführen der Bausteine in einer übersichtlichen Weboberfläche.
* **Ergebnis:** Flask Application Factory (`src/web/__init__.py`), Formulare und Jinja2-Templates mit Pico.css.
* **Qualitätscheck:** Über das Browser-Formular eingegebene Transaktionen landen in der Datenbank und aktualisieren den Saldo live.

### 4️⃣ Kapitel 4: Packaging & Projektabschluss
* **Fokus:** Zero-Configuration Usability für Anwender und Dozenten.
* **Ergebnis:** `start.bat` (Windows) / `start.sh` (Linux/macOS) für den 1-Klick-Start im Standardbrowser.
* **Qualitätscheck:** Ein Klick auf die Startdatei öffnet die funktionierende Anwendung auf jedem Zielrechner.

---

## ✅ Definition of Done (DoD) für ein Kapitel

Ein Kapitel gilt erst dann als **erledigt (Done)**, wenn folgende Punkte erfüllt sind:

1. **Clean Code & Lesbarkeit:** Der Code hält sich an PEP 8 und ist verständlich aufgebaut.
2. **Isolierte Lauffähigkeit:** Das Modul lässt sich unabhängig von den anderen Schichten testen.
3. **Gemeinsames Verständnis:** Alle 4 Teammitglieder können die Funktionsweise des Moduls erklären.
4. **Git-Sauberkeit:** Änderungen sind lokal getestet und sauber im Git-Repository gesichert.

---

## ⏱️ Schlanke Team-Kommunikation

* **5-Minuten-Kickoff zu Beginn der Unterrichtszeit:** Kurzer Check im Team ("An welchem Kapitel/Modul arbeiten wir heute und gibt es Fragen?").
* **Erfolgs-Review am Ende des Kapitels:** Gemeinsamer Durchlauf des fertigen Bausteins im Gruppenraum.
