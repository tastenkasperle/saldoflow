# 📘 Projektentwicklung & Scrum-Vorgehensmodell

## 🎯 Leitphilosophie: Modulares Scrum-Sprint-Modell (Agile Light)

> **Kernprinzip:** *Übersicht, Kontrolle, echte Scrum-Praxis und Lerneffekt stehen an erster Stelle.*  
> Wir verzichten bewusst auf unübersichtliche Bürokratie und künstliche Doppelrollen. Stattdessen entwickeln wir die Anwendung **schrittweise in fokussierten, in sich geschlossenen Sprints**. Jeder Sprint liefert am Ende ein lauffähiges Software-Inkrement (MVP).

---

## 👥 Modul-Verantwortlichkeiten im Scrum-Team (4er-Team)

Jedes Teammitglied übernimmt die klare Patenschaft für ein Fachmodul, während das gesamte Team agil zusammenarbeitet:

* **Teamleiter / Integrator (Scrum Master & Architect):**  
  *(Verantwortung: Gesamtarchitektur, Ordnerstruktur, Modulintegration, Flask Application Factory, Teamkoordination & Blocker-Beseitigung)*
* **Entwickler A – Modul Domänenlogik (OOP):**  
  *(Verantwortung: Reine Geschäftslogik in Python, Objektmodellierung `Transaction`, `Income`, `Expense`, `BudgetBook`)*
* **Entwickler B – Modul Persistenz (SQLite & Repository):**  
  *(Verantwortung: Datenbankschema `schema.sql`, CRUD-Operationen im `TransactionRepository`)*
* **Entwickler C – Modul Präsentation (Web-UI & UX):**  
  *(Verantwortung: Responsive HTML5-Templates mit Pico.css, Usability, Jinja2-Dashboard)*

---

## 🧩 Das Sprint-Entwicklungsmodell

```text
┌─────────────────────────────────────────────────────────────────┐
│ SPRINT 1: Core Domain & Persistenz (Fundament & DB)             │
│ Ziel: Lauffähige OOP-Modelle & SQLite Repository mit CRUD       │
└─────────────────────────────────────────────────────────────────┘
                                │ (Inkrement 1 fertig & getestet)
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│ SPRINT 2: Web-UI & Integration (Flask & Pico.css)               │
│ Ziel: Interaktives Web-Dashboard, Formulare & Live-Saldo        │
└─────────────────────────────────────────────────────────────────┘
                                │ (Inkrement 2 fertig & getestet)
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│ SPRINT 3: Usability, Packaging & Release (1-Klick-Starter)       │
│ Ziel: start.bat / start.sh, Doku & finale Präsentation           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📖 Detailübersicht der Sprints

### 🚀 Sprint 1: Core Domain & Persistenz-Schicht
* **Fokus:** Objektorientierte Programmierung & SQLite Datenbankspeicherung.
* **Ergebnis / Inkrement:** `src/domain/models.py`, `src/persistence/schema.sql` und `src/persistence/repository.py`.
* **Qualitätscheck:** Die Logik lässt sich im Terminal testen (`if __name__ == '__main__':`). Transaktionen werden korrekt berechnet und dauerhaft in SQLite gespeichert.

### 🌐 Sprint 2: Web-Präsentationsschicht & Flask-Integration
* **Fokus:** Zusammenführen aller Bausteine in einer benutzerfreundlichen Weboberfläche.
* **Ergebnis / Inkrement:** Flask Application Factory (`src/web/__init__.py`), Formulare und Jinja2-Templates mit Pico.css (`base.html`, `index.html`).
* **Qualitätscheck:** Über das Browser-Formular eingegebene Buchungen landen in der SQLite-Datenbank und aktualisieren den Saldo live auf dem Dashboard.

### 📦 Sprint 3: Packaging, Usability & Projektabschluss
* **Fokus:** Zero-Configuration Usability für Anwender und Dozenten.
* **Ergebnis / Inkrement:** `start.bat` (Windows) / `start.sh` (Linux/macOS) für den 1-Klick-Start im Browser, finale Projektdokumentation.
* **Qualitätscheck:** Ein Klick auf die Startdatei startet den Server und öffnet die Anwendung automatisch.

---

## ✅ Definition of Done (DoD) für jeden Sprint

Ein Sprint gilt erst dann als **erledigt (Done)**, wenn folgende Kriterien erfüllt sind:

1. **Clean Code & Lesbarkeit:** Der Code hält sich an PEP 8 und ist verständlich aufgebaut.
2. **Feature-Branch Integration:** Der Code wurde vom Entwickler-Branch auf `main` gemergt.
3. **Isolierte Lauffähigkeit & Tests:** Alle Modultests laufen ohne Fehler durch.
4. **Gemeinsames Verständnis:** Alle 4 Teammitglieder können die Funktionsweise des Sprint-Ergebnisses erklären.

---

## ⏱️ Agiler Scrum-Tagesablauf (Unterrichtsfenster 09:35 – 12:40 Uhr)

* **Daily Standup (10 Min zu Beginn):** 3 Fragen ("Was habe ich gemacht?", "Was mache ich heute?", "Wo gibt es Blocker?").
* **Arbeitsphase in Feature-Branches:** Ungestörtes Entwickeln auf eigenen Git-Branches (`feature/...`).
* **Sprint Review & Demo (15 Min vor Ende):** Gemeinsame Vorführung des Tages-Inkrements im Team.
