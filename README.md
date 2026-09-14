# 💰 SaldoFlow – Modulares Haushaltsbuch

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.org/)
[![Database](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)](https://www.sqlite.org/)
[![CSS](https://img.shields.io/badge/UI-Pico.css-violet.svg)](https://picocss.com/)

**SaldoFlow** ist ein einfaches, modulares Haushaltsbuch, das im Rahmen der Umschulung (AnwP) entwickelt wird. Es dient dem Erlernen von objektorientierter Programmierung, einer sauberen **3-Schichten-Architektur** (Clean Architecture) sowie der kollaborativen Entwicklung im Team mittels **Agile Scrum**.

---

## 🚀 Quick Start (Lokaler Start)

1. **Repository klonen:**
   ```bash
   git clone https://github.com/tastenkasperle/saldoflow.git
   cd saldoflow
   ```

2. **Virtuelle Umgebung erstellen & aktivieren:**
   ```bash
   python -m venv .venv
   # Windows (PowerShell):
   .\.venv\Scripts\Activate.ps1
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Anwendung starten:**
   ```bash
   python run.py
   ```
   Die App ist anschließend im Browser unter `http://127.0.0.1:5000` erreichbar.

---

## 🏛 Architektur & Schichtenmodell

Die Anwendung folgt dem strikten **3-Schichten-Modell**:

* **Präsentationsschicht (`src/web/`):** Flask Application Factory & Jinja2 Templates mit Pico.css.
* **Geschäftslogik (`src/domain/`):** Objektorientierte Domänenmodelle (`Transaction`, `BudgetBook`).
* **Datenhaltung (`src/persistence/`):** SQLite Repository (`saldoflow.db`) mit sauberen SQL-Queries.

---

## 📚 Projekt-Dokumentation

Eine ausführliche Übersicht aller Konzepte und Anforderungsspezifikationen befindet sich im Ordner **[`docs/`](./docs/)**:

* 📋 **[Anforderungsprofil (MoSCoW & NFAs)](./docs/ANFORDERUNGSPROFIL.md):** Funktionale und Nicht-funktionale Anforderungen.
* 🏗 **[Architektur & Entwurf](./docs/ARCHITEKTUR_UND_ENTWURF.md):** Schichtenmodell, UML-Klassendiagramm, ER-Diagramm & Datenfluss.
* 🚀 **[Sprint 1 Aufgabenpakete](./docs/TASKS_SPRINT_1.md):** Kochrezepte für Entwickler A, B, C und den Teamleiter.
* 🔄 **[Scrum-Vorgehensmodell](./docs/Projektentwicklung_Scrum_Modell.md):** Ablauf der Sprints, Branching-Strategie & Standups.
* 📝 **[Projektantrag](./docs/PROJEKTANTRAG.md):** Ursprünglicher Projektantrag.

---

## 👥 Entwicklerteam

* **Teamleiter / Integration & Web-Routing:** Tastenkasperle
* **Entwickler A (Domain Layer):** Geschäftslogik & Berechnungen
* **Entwickler B (Persistence Layer):** SQLite Schema & Repository
* **Entwickler C (Presentation Layer):** HTML Formular & Dashboard Styling
