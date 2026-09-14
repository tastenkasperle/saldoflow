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

## 🏛 Architektur-Philosophie: Strikte Schichtentrennung (Clean Architecture)

SaldoFlow setzt auf eine bewusste **Entkopplung der Komponenten (Clean Architecture)**. Das Herzstück der Anwendung ist vollkommen unabhängig von Frameworks, Datenbanken oder Benutzeroberflächen.

```
       +---------------------------------------------+
       |   Präsentationsschicht (Flask / Jinja2 UI)  |
       +----------------------+----------------------+
                              | (nutzt)
                              v
       +----------------------+----------------------+
       |   Geschäftslogik / Domäne (Pure Python OOP)  |
       +----------------------+----------------------+
                              ^ (nutzt)
                              |
       +----------------------+----------------------+
       |   Persistenzschicht (SQLite Repository)     |
       +---------------------------------------------+
```

### 💡 Warum dieser Aufbau? (Didaktischer & Architektonischer Nutzen)

1. **Strikte Unabhängigkeit & Testbarkeit (Lose Kopplung):**  
   Die Geschäftslogik (`src/domain/models.py`) enthält reine Python-Objekte. Sie benötigt weder Flask noch SQLite. Das bedeutet: Wenn die Datenbank von SQLite auf PostgreSQL umgestellt wird, bleibt der gesamte Domänencode unberührt.
2. **Didaktischer Verzicht auf ORM (z. B. SQLAlchemy) in Sprint 1:**  
   Um die Kernkonzepte der **objektorientierten Programmierung (OOP)** sowie **reines SQL** (`schema.sql` & `sqlite3`) tiefgehend zu verstehen, erfolgt das Datenmapping bewusst manuell im Repository-Pattern. *Ein Refactoring auf ein ORM ist als Lernziel für Folgesprints vorgesehen.*
3. **Parallele Entwicklung im Team:**  
   Durch die klare Trennung der 3 Schichten können alle Teammitglieder zeitgleich auf eigenen Feature-Branches entwickeln, ohne dass es zu Konflikten im Code kommt.

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
* **Entwickler A (Domain Layer / OOP):** André
* **Entwickler B (Persistence Layer / SQLite DB):** Christopher
* **Entwickler C (Presentation Layer / Web-UI):** Julija
