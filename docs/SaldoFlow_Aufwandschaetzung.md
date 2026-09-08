# Projekt SaldoFlow – Modulares Haushaltsbuch
## Agiles Projekt-Backlog & Aufwandschätzung (Unterrichtsaufgabe AnwP)

---

### 1. Product-Backlog (Anforderungen in User-Stories)

Das Product-Backlog fasst alle funktionalen und technischen Anforderungen aus dem Projektantrag in machbare User-Stories (bzw. Enabler-Stories für technische Grundlagen) zusammen.

| ID | Typ | User Story / Requirement | Akzeptanzkriterien | Prio |
|---|---|---|---|---|
| **US-01** | Feature | **Einnahmen & Ausgaben erfassen**<br>_Als Anwender möchte ich Betrag, Kategorie, Datum und Beschreibung eingeben können, um Transaktionen festzuhalten._ | - Formular validiert Pflichtfelder (Betrag > 0, Datum vorhanden).<br>- Unterscheidung zwischen Einnahme (`Income`) und Ausgabe (`Expense`). | **Hoch (Must)** |
| **US-02** | Feature | **Transaktionsübersicht & Saldo anzeigen**<br>_Als Anwender möchte ich alle Buchungen in einer Liste sehen und den aktuellen Gesamtsaldo berechnet bekommen._ | - Tabelle listet alle Transaktionen chronologisch.<br>- Gesamtsaldo, Summe Einnahmen und Ausgaben werden dynamisch berechnet. | **Hoch (Must)** |
| **US-03** | Feature | **Transaktionen löschen**<br>_Als Anwender möchte ich fehlerhafte Einnahmen/Ausgaben löschen können._ | - Löschen-Button entfernt Eintrag dauerhaft aus der Datenbank.<br>- Saldo aktualisiert sich sofort nach dem Löschen. | **Hoch (Must)** |
| **US-04** | Feature | **Kategorie-Filter & Auswertung**<br>_Als Anwender möchte ich Transaktionen nach Kategorien filtern können._ | - Filter-Dropdown nach Kategorie (z.B. Miete, Lebensmittel).<br>- Summen werden je Kategorie korrekt berechnet. | **Mittel (Should)** |
| **TS-01** | Technical | **Projekt-Setup & Schichtenarchitektur**<br>_Als Entwickler erstelle ich die Grundstruktur (`src/`), Flask Application-Factory (`create_app`) und Git-Workflow._ | - Ordnerstruktur (`src/domain`, `src/persistence`, `src/web`).<br>- Flake8/Clean Code Konfiguration, Git Repository initialisiert. | **Hoch (Must)** |
| **TS-02** | Technical | **Domänenmodellierung (OOP Domain Layer)**<br>_Als Entwickler erstelle ich reine Python-Klassen `Transaction`, `Income`, `Expense` und `BudgetBook`._ | - Reine OOP ohne Framework-Abhängigkeiten.<br>- Methoden zur Saldo- und Summenberechnung enthalten. | **Hoch (Must)** |
| **TS-03** | Technical | **SQLite-Datenbank & Repository-Pattern**<br>_Als Entwickler baue ich das `TransactionRepository` mit SQLite zur Datenpersistenz._ | - SQLite Schema erstellt (`schema.sql`).<br>- Entkopplung über Repository-Pattern (CRUD-Operationen). | **Hoch (Must)** |
| **TS-04** | Technical | **Web-Frontend (Pico.css & Jinja2 Templates)**<br>_Als Entwickler gestalte ich ein responsives HTML5-UI ohne JS-Frameworks._ | - HTML5 mit semantischem Pico.css Styling.<br>- Server-seitiges Rendering über Jinja2 Templates. | **Hoch (Must)** |
| **TS-05** | Technical | **1-Klick-Start-Skripte (`start.bat` / `start.sh`)**<br>_Als Anwender möchte ich das Projekt ohne Konfiguration per Doppelklick starten._ | - Prüft Python-Installation & virtuelle Umgebung.<br>- Startet Flask-App und öffnet den Standardbrowser. | **Mittel (Should)** |
| **TS-06** | Technical | **Automatisierte Unittests (pytest / unittest)**<br>_Als Entwickler erstelle ich Tests für Finanzmathematik und Repository._ | - Unittests für Saldo-Logik & Repository-CRUD grün.<br>- Ausführbar über `pytest`. | **Hoch (Must)** |

---

### 2. Sprint-Backlog (Sprint 1 – MVP Core Functionality)

Für den ersten Sprint wählen wir die Kern-Stories aus, die für eine lauffähige Basisanwendung (MVP - Minimum Viable Product) zwingend erforderlich sind.

* **Sprint-Ziel:** Lauffähige 3-Schichten-Webanwendung, mit der Transaktionen erfasst, in SQLite gespeichert und als Saldo im Browser angezeigt werden können.

#### Ausgewählte Stories für den Sprint-Backlog:
1. **TS-01:** Projekt-Setup & Schichtenarchitektur
2. **TS-02:** Domänenmodellierung (OOP Domain Layer)
3. **TS-03:** SQLite-Datenbank & Repository-Pattern
4. **US-01:** Einnahmen & Ausgaben erfassen
5. **US-02:** Transaktionsübersicht & Saldo anzeigen
6. **TS-04:** Web-Frontend (Pico.css & Jinja2 Templates)
7. **TS-06:** Automatisierte Unittests

---

### 3. Aufwandschätzung für das Sprint-Backlog

Die Schätzung erfolgt in **Story Points** (Relativer Aufwand nach Fibonacci-Folge: 1, 2, 3, 5, 8) sowie in **Idealstunden / Personenstunden** (basierend auf dem Projektbudget von 4 Personen × 40h = 160h Gesamtaufwand).

| Task-ID | Beschreibung | Story Points | Schätzung (Stunden) | Verantwortlich (Rolle laut Antrag) |
|---|---|:---:|:---:|---|
| **TS-01** | Grundgerüst Flask, Application Factory, Git-Branching Setup | **3 SP** | 6 h | Projektleitung & Systemarchitektur |
| **TS-02** | Klassen `Transaction`, `Income`, `Expense`, `BudgetBook` inkl. Business-Logik | **5 SP** | 10 h | Domänenlogik & OOP |
| **TS-03** | SQLite-Datenbankschema, `TransactionRepository` (CRUD) | **5 SP** | 12 h | Datenpersistenz & Testing |
| **US-01** | Flask-Routes `POST /add`, Formular-Handling & Validierung | **3 SP** | 8 h | Frontend & UX / Domänenlogik |
| **US-02** | Flask-Routes `GET /`, Berechnung von Saldo & Anzeige in UI | **3 SP** | 6 h | Frontend & UX |
| **TS-04** | HTML5 Jinja2 Templates mit Pico.css responsive stylen | **5 SP** | 10 h | Frontend & UX |
| **TS-06** | Unit-Tests für Domänenmodelle & Repository schreiben | **3 SP** | 8 h | Datenpersistenz & Testing |
| **SUMME** | **Sprint 1 Kern-Aufwände** | **27 SP** | **60 h** | **Team (4 Personen)** |

---

### 💡 Methodische Erklärung für den Unterricht (Didaktik-Notiz)

- **Product-Backlog:** Sammelt **alle** Wünsche und Anforderungen des Projekts.
- **Sprint-Backlog:** Eine Teilmenge des Product-Backlogs für einen festgelegten Zeitraum (Sprint), sortiert nach der höchsten Priorität (**Must-Haves**).
- **Story Points (SP):** Beschreiben die **relativ wahrgenommene Komplexität und den Risikograd** einer Aufgabe im Vergleich zu anderen Aufgaben (nicht primär Zeitdauer).
- **Stundenschätzung:** Ergänzt die Story Points um konkrete Personenstunden (Kapazitätsplanung), um abzugleichen, ob der Sprint in die verfügbare Arbeitszeit des 4-köpfigen Teams passt.
