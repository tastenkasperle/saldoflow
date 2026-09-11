# 📋 Anforderungsprofil: SaldoFlow – Modulares Haushaltsbuch

**Projekt:** SaldoFlow (AnwP)  
**Version:** 1.0 (Sprint 1 MVP)  
**Status:** In Abstimmung mit dem Entwicklerteam  

---

## 🎯 1. Zweck & Zielsetzung

Dieses Dokument beschreibt das **Anforderungsprofil (Spezifikation)** für die Anwendung *SaldoFlow*. Es dient dem 4-köpfigen Entwicklerteam als verbindliche Arbeits- und Abnahmegrundlage.

---

## 🛠 2. Funktionale Anforderungen (Functional Requirements)

Die funktionalen Anforderungen beschreiben, **welche Fachfunktionen** das System bereitstellen muss. Die Priorisierung erfolgt nach der **MoSCoW-Methode** (*Must, Should, Could, Won't*).

### 2.1 Kernfunktionen (MVP - Must-Have)

| ID | Anforderung | Beschreibung | Zuordnung Rolle |
| :--- | :--- | :--- | :--- |
| **FA-01** | **Transaktionen erfassen** | Nutzer kann eine neue Buchung mit *Titel*, *Betrag* (> 0), *Typ* (Einnahme oder Ausgabe) und *Kategorie* über ein Webformular eingeben. | Entwickler C (UI) & Entwickler A (Domain) |
| **FA-02** | **Finanzmathematik** | Das System berechnet automatisch *Gesamteinnahmen*, *Gesamtausgaben* und den *Gesamtsaldo* ($Saldo = Einnahmen - Ausgaben$). | Entwickler A (Domain) |
| **FA-03** | **Daten-Persistenz** | Alle eingegebenen Buchungen werden dauerhaft in einer lokalen SQLite-Datenbank (`saldoflow.db`) gespeichert. | Entwickler B (DB) |
| **FA-04** | **Dashboard-Anzeige** | Sämtliche gespeicherten Transaktionen werden in einer übersichtlichen Tabelle im Web-Dashboard angezeigt. | Entwickler C (UI) & Teamleiter (Routes) |
| **FA-05** | **Transaktion löschen** | Einzelne Transaktionen können per Klick über ihre eindeutige ID aus der Datenbank entfernt werden. | Entwickler B (DB) & Teamleiter (Routes) |

### 2.2 Erweiterte Funktionen (Zukunft - Should / Could)

| ID | Anforderung | Beschreibung | Priorität |
| :--- | :--- | :--- | :--- |
| **FA-06** | **Kategorien-Filter** | Filtern der angezeigten Transaktionen nach bestimmten Kategorien (z.B. nur "Wohnen" oder "Lebensmittel"). | **SHOULD** (Sprint 2) |
| **FA-07** | **Monatsansicht** | Einschränkung der Berechnung und Anzeige auf einen gewählten Kalendermonat. | **COULD** (Sprint 3) |

---

## ⚡ 3. Nicht-Funktionale Anforderungen (Non-Functional Requirements)

Die nicht-funktionalen Anforderungen definieren die **Qualitätskriterien, Leistungseigenschaften und Randbedingungen** des Systems.

| ID | Qualitätskriterium | Beschreibung |
| :--- | :--- | :--- |
| **NFA-01** | **Usability & Responsive Design** | Die Oberfläche basiert auf HTML5 und Pico.css. Sie ist klar strukturiert, übersichtlich und passt sich ohne Scrollbalken-Frust an Desktop- und Tablet-Auflösungen an. |
| **NFA-02** | **Architektur & Schichtentrennung** | Strikte Entkopplung nach dem 3-Schichten-Modell: *Domain* (Geschäftslogik), *Persistence* (SQLite Repository) und *Web* (Flask & Templates). Keine SQL-Queries in HTML-Templates! |
| **NFA-03** | **Performance** | Das Laden der Startseite und das Verarbeiten von Formulareingaben im lokalen Webserver erfolgen unter 100 ms. |
| **NFA-04** | **Zero-Configuration Portabilität** | Die Anwendung erfordert keine komplexe Serverinstallation. Sie lässt sich plattformübergreifend (Windows/Linux/macOS) über ein simples Startskript starten. |
| **NFA-05** | **Testbarkeit & Clean Code** | Die Kernberechnungen und Datenbankfunktionen sind durch isolierte Tests im Quellcode abgedeckt. Der Code folgt den PEP 8 Konventionen. |

---

## 🚫 4. Abgrenzung / Nicht-Ziele (Out of Scope / Won't-Have)

Folgende Funktionen sind **explizit ausgeschlossen**, um den Fokus und den Zeitrahmen im Umschulungsunterricht nicht zu sprengen:

* ❌ **Kein Multi-User / Login-System:** Es gibt keine Benutzerverwaltung oder Passwort-Authentifizierung. Die App läuft lokal als Single-User-Anwendung.
* ❌ **Keine Banken-APIs:** Keine PSD2-/FinTS-Schnittstellen zu realen Bankkonten.
* ❌ **Keine Belegerkennung (OCR):** Kein Scannen oder Auswerten von Kassenzetteln per Bildverarbeitung.
* ❌ **Kein schweres JavaScript-Framework:** Kein Einsatz von React, Vue oder Angular. Serverseitiges Rendering mit Flask & Jinja2 genügt.

---

## 🏁 5. Akzeptanzkriterien für die Abnahme (Definition of Done)

Das Anforderungsprofil gilt als erfüllt, wenn:
1. Eine eingegebene Ausgabe den Gesamtsaldo und die Ausgabensumme auf dem Dashboard sofort korrekt reduziert.
2. Nach einem Neustart des Flask-Servers alle zuvor eingegebenen Daten in SQLite erhalten bleiben.
3. Der Code sauber auf die 4 Entwickler-Module aufgeteilt und auf GitHub gemergt wurde.
