# **ArTEMiS-Testgenerierung**

Diese Python-Anwendung nutzt ein lokal mit Ollama betriebenes **Llama3-Modell**, um automatisch Testscripte für vorgegebene Musterlösungen zu erstellen. Die generierten Tests sind speziell für den Einsatz in der **ArTEMiS-Lernumgebung** konzipiert.

Ziel ist es, **Kursentwicklerinnen und -entwickler** zu entlasten, die Erstellung neuer Kurse zu vereinfachen und die Qualität der Kurse durch automatisierte Testgenerierung zu steigern.

Vor jeder Anfrage wird die Eingabe optional auf **syntaktische Korrektheit** und das Vorhandensein von **testbaren Strukturen** überprüft. Anschließend wird die Anfrage mittels eines speziell entwickelten **Kombinations-Prompts** oder einem belibigen **Spezialisierungs Prompts** an das lokale Llama3-Modell übergeben. Das Modell verarbeitet die Anfrage und liefert einen generiertes Testscript zurück.

---

## **Features**
- **Automatisierte Testgenerierung**: Basierend auf einer Musterlösung werden Testskripte generiert.
- **ArTEMiS-Integration**: Speziell für den Einsatz in der ArTEMiS-Lernumgebung optimiert.
- **Flexible Eingaben**: Unterstützt verschiedene Python-Programmieraufgaben.
- **Lokale Ausführung**: Modell läuft lokal ohne Internetverbindung.
- **Validierung**: Eingaben werden vor der Verarbeitung überprüft (syntaktische Korrektheit, testbare Strukturen).

---

## **Voraussetzungen**
- Python **3.10** oder höher
- Ollama **0.3.14** oder höher mit installiertem Llama3-Modell

---

## **Installation**
1. **Python installieren:**  
   Stelle sicher, dass Python 3.10 oder höher installiert ist. Du kannst Python [hier herunterladen](https://www.python.org/).  
2. **Ollama installieren:**  
   Installiere Ollama, um das Llama3-Modell lokal auszuführen:
   ```bash
   pip install ollama
   ```
3. **Llama3-Modell laden:**  
   Lade das Modell lokal herunter:
   ```bash
   ollama pull llama3.1:8b
   ```
4. **Repository klonen:**  
   Lade das Projekt herunter:
   ```bash
   git clone https://github.com/yorickbehme/ArTEMiS-Testgenerator.git
   ```
5. **Ins Code-Verzeichnis wechseln:**  
   Navigiere in das Hauptverzeichnis des Projekts:
   ```bash
   cd ArTEMiS-Testgenerator/src
   ```
5. **Programm starten:**  
   Führe die Anwendung aus:
   ```bash
   python3 main.py
   ```
 
---

## **Projektstruktur**

```plaintext
├── data/
│   ├── artemis_integration.md
│   ├── beispiel_optimierung.md
│   ├── modelfileuntersuchung.md
│   ├── modellauswertung.md
│   ├── modelluntersuchung.md
│   ├── modellvergleich.md
│   └── promptuntersuchung.md
├── src/
│   ├── ai_generator.py  
│   ├── main.py
│   ├── prompts.json
│   ├── prompts.py
│   ├── ui_elements.py
│   ├── ui_testgenerator.py
│   └── validator.py
├── LICENSE
└── README.md
```

---

## **Hinweise**
- **Version:** Diese Anwendung basiert auf Prototyp-Version `version-42`.
- **Einschränkungen:** Derzeit wird nur Python-Code und nur das Model Llama3 unterstützt.
- **Feedback:** Für Fragen, Fehlerberichte oder Vorschläge kannst du ein [Issue](https://github.com/yorickbehme/ArTEMiS-Testgenerator.git) erstellen.

## **Lizenz**
Dieses Projekt steht unter der [MIT-Lizenz](./LICENSE). Details dazu findest du in der Datei `LICENSE`.
