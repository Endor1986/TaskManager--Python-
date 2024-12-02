Task Manager App
Dies ist ein einfaches Python-Projekt für einen Task Manager, der in Python mit Tkinter entwickelt wurde. Die Anwendung ermöglicht das Erstellen, Verwalten, Markieren als erledigt und Löschen von Aufgaben. Zusätzlich können Aufgaben einem Benutzer zugewiesen, mit einem Fälligkeitsdatum versehen und priorisiert (high, medium, low) werden.

Das Projekt ist so gestaltet, dass es die Grundprinzipien guter Softwarearchitektur (z. B. SOLID) demonstriert und einfach erweiterbar ist.

Funktionen
Aufgaben hinzufügen:
Name, Benutzer, Fälligkeitsdatum und Priorität (high, medium, low) eingeben.
Aufgaben anzeigen:
Darstellung in einer übersichtlichen Liste mit Status und Priorität.
Aufgaben als erledigt markieren:
Status ändern (erledigt/nicht erledigt).
Aufgaben löschen:
Entfernt Aufgaben direkt aus der Übersicht.

Verzeichnisstruktur

TaskManager/
├── TaskManager.py         # Hauptdatei und Einstiegspunkt
│
├── models/                # Modelle
│   └── task.py            # Definition der Task-Klasse
│
├── services/              # Geschäftslogik
│   ├── interfaces.py      # Definition der abstrakten Methoden für den TaskManager
│   └── task_manager.py    # Implementierung der Aufgabenverwaltung
│
├── ui/                    # Benutzeroberfläche
│   └── app.py             # TaskManagerApp-Klasse
│
└── utils/                 # Hilfsfunktionen (optional)
    └── date_utils.py      # Datumshilfsfunktionen (optional)

Voraussetzungen
Python 3.10 oder höher

Prüfen Sie die Python-Version:
python --version

Falls nicht installiert, laden Sie Python von python.org herunter.
Benötigte Python-Bibliotheken

Installieren Sie die erforderlichen Abhängigkeiten:

pip install tkcalendar

Entwicklungsumgebung

Eine beliebige IDE wie Visual Studio Code, PyCharm oder Visual Studio.
Installation

Schritt 1: Projekt herunterladen
Laden Sie die Projektdateien herunter oder klonen Sie das Repository:

git clone https://github.com/endor1986/TaskManager.git
cd TaskManager
Schritt 2: Abhängigkeiten installieren
Öffnen Sie ein Admin-Terminal (CMD) und installieren Sie die erforderlichen Bibliotheken:

pip install tkcalendar
Schritt 3: Anwendung starten

Starten Sie die Anwendung aus dem Projektverzeichnis:
python TaskManager.py

Projektstruktur
1. models/task.py
Enthält die Klasse Task, die die Struktur einer Aufgabe definiert.
Eigenschaften:
name: Name der Aufgabe.
user: Benutzer, dem die Aufgabe zugewiesen wurde.
due_date: Fälligkeitsdatum der Aufgabe.
priority: Priorität der Aufgabe (high, medium, low).
done: Status der Aufgabe (erledigt/nicht erledigt).
Methoden:
mark_done(): Markiert die Aufgabe als erledigt.

2. services/
Enthält die Geschäftslogik für das Management von Aufgaben.
interfaces.py:
Definiert die abstrakten Methoden:
add_task(task)
mark_task_done(index)
delete_task(index)
get_tasks()
Diese Methoden bieten eine klare Struktur für die Implementierung.
task_manager.py:
Implementiert die abstrakten Methoden:
Fügt Aufgaben hinzu, markiert sie als erledigt und löscht sie.

3. ui/app.py
Verantwortlich für die Benutzeroberfläche.
Verwendet Tkinter, um Eingaben und Ausgaben zu verwalten.
Hauptfunktionen:
Eingabefelder: Für Name, Benutzer und Datum.
Dropdown-Menü: Für Prioritätenauswahl.
Buttons: Für Aufgabenverwaltung.
Liste: Zeigt alle Aufgaben mit Priorität und Status.

Besonderheiten
Modularität:
Der Code ist in separate Module unterteilt, um Wartbarkeit und Erweiterbarkeit zu gewährleisten.
Abstraktion:

Die Geschäftslogik ist von der Benutzeroberfläche getrennt.
Einfachheit:
Das Projekt ist leicht zu verstehen und zu erweitern.
Mögliche Erweiterungen
Persistente Datenspeicherung (SQLite oder JSON).
Filterung von Aufgaben nach Priorität oder Datum.
Verbesserung des GUI-Designs.

Hinweis
Dieses Projekt dient ausschließlich der Demonstration von Programmierfähigkeiten. Die gesamte Entwicklung hat ca. 50-70 Minuten in Anspruch genommen


