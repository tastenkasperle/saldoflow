# 🏗 Architektur & Entwurf: SaldoFlow

**Projekt:** SaldoFlow (Modulares Haushaltsbuch – AnwP)  
**Version:** 1.0 (Sprint 1)  
**Status:** In Erstellung / Begleitende Entwicklungsdokumentation  

---

## 📐 1. Gesamtarchitektur (3-Schichten-Modell)

SaldoFlow basiert auf einer klaren **3-Schichten-Architektur** (Clean Architecture), um Geschäftslogik, Datenhaltung und Benutzeroberfläche strikt voneinander zu entkoppeln.

```mermaid
graph TD
    subgraph UI ["Schicht 3: Präsentation (Web UI)"]
        HTML["Jinja2 HTML Templates (Pico.css)"]
        Routes["Flask Routes (src/web/routes.py)"]
    end

    subgraph Domain ["Schicht 1: Geschäftslogik (Domain)"]
        Models["Python Objekte (Transaction, BudgetBook)"]
    end

    subgraph Persistence ["Schicht 2: Datenhaltung (Persistence)"]
        Repo["SQLite Repository (repository.py)"]
        DB[(SQLite DB: saldoflow.db)]
    end

    HTML <-->|HTTP Request / Formular| Routes
    Routes <-->|Nutzt| Models
    Routes <-->|Nutzt| Repo
    Repo <-->|SQL Queries| DB
```

---

## 🗄 2. Datenbankschema (Persistence Layer)

Die Datenhaltung erfolgt in einer lokalen **SQLite-Datenbank** (`saldoflow.db`). Für Sprint 1 wird eine zentrale Tabelle `transactions` verwendet.

```mermaid
erDiagram
    TRANSACTIONS {
        INTEGER id PK "Auto Increment"
        TEXT title "Titel der Buchung"
        REAL amount "Betrag in EUR (> 0)"
        TEXT type "INCOME oder EXPENSE"
        TEXT category "Kategorie (z.B. Wohnen, Gehalt)"
        TEXT created_at "Erstellungsdatum (ISO-8601)"
    }
```

### DDL Schema (`src/persistence/schema.sql`)
```sql
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('INCOME', 'EXPENSE')),
    category TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🧩 3. Domänenmodell (Domain Layer)

Die Geschäftslogik ist unabhängig von Flask und SQLite in reinen Python-Klassen kapselt (`src/domain/models.py`).

```mermaid
classDiagram
    class Transaction {
        +int id
        +str title
        +float amount
        +str type
        +str category
        +is_income() bool
        +is_expense() bool
    }

    class BudgetBook {
        +list~Transaction~ transactions
        +add_transaction(t: Transaction)
        +get_total_income() float
        +get_total_expenses() float
        +get_balance() float
    }

    BudgetBook "1" *-- "n" Transaction : enthält
```

---

## 🌐 4. Web & Routing (Presentation Layer)

Der Webserver verwendet das **Application Factory Pattern** (`src/web/__init__.py`).

### Endpunkte (Routes):
| HTTP Methode | Pfad | Beschreibung | Beteiligte Komponenten |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Zeigt das Dashboard mit Saldo-Berechnung & Buchungstabelle | `routes.py`, `index.html`, `repository.py` |
| `POST` | `/add` | Verarbeitet das Formular zur Erfassung neuer Transaktionen | `routes.py`, `models.py`, `repository.py` |
| `POST` | `/delete/<id>` | Löscht eine bestimmte Transaktion | `routes.py`, `repository.py` |

---

## 🔄 5. Datenfluss bei einer Buchung (Beispiel: Transaktion hinzufügen)

```mermaid
sequenceDiagram
    autonumber
    actor User as Benutzer (Browser)
    participant Flask as Flask Route (/add)
    participant Domain as Domain (models.py)
    participant Repo as Repository (repository.py)
    participant DB as SQLite DB

    User->>Flask: POST /add (Formulardaten)
    Flask->>Domain: Validierung & Erstellung Transaction-Objekt
    Flask->>Repo: save_transaction(transaction)
    Repo->>DB: INSERT INTO transactions ...
    DB-->>Repo: Bestätigung (ID)
    Flask-->>User: HTTP 302 Redirect auf '/' (Dashboard aktualisiert)
```

---

## 📝 6. Zuständigkeiten im Entwicklerteam

* **Entwickler A:** Pflege & Tests von Kap. 3 (`src/domain/models.py`)
* **Entwickler B:** Pflege & Tests von Kap. 2 (`src/persistence/schema.sql`, `repository.py`)
* **Entwickler C:** Gestaltung von Kap. 4 UI (`src/web/templates/base.html`, `index.html`)
* **Teamleiter (Du):** Gesamtarchitektur, Kap. 4 Routes (`src/web/routes.py`), Integration & Doku-Schirmherrschaft
