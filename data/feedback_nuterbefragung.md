### **Feedback Nutzerbefragung**

## **Auswertungstabelle**

### Aufgabe 1-3 Ergebnisüberischt

| **Aufgabe**        | **Antwort** | **richtige Antworten** | **Prozent** |
|---------------------|-------------------|-----------------------|-------------|
| Aufgabe 1           | 4                 | 8/10                    | 80.00%      |
| Aufgabe 2           | 2                 | 8/10                    | 80.00%      |
| Aufgabe 3           | 6/3               | 9/10                    | 90.00%      |

## Ergebnisse der Umfrage zur Feedback-Qualität

| **Frage**                                     | **Proband 1** | **Proband 2** | **Proband 3** | **Proband 4** | **Proband 5** | **Proband 6** | **Proband 7** | **Proband 8** | **Proband 9** | **Proband 10** | **Durchschnitt** |
|-----------------------------------------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|----------------|------------------|
| Wie hilfreich war Feedback zu „add(0, 1)“?    | 1             | 1             | 2             | 3             | 1             | 1             | 1             | 4             | 1             | 1              | 1,7              | 
| Wie verständlich war Feedback zu „add(-2, 3)“?| 1             | 1             | 2             | 2             | 3             | 1             | 1             | 3             | 2             | 1              | 1,8              | 
| Wie hilfreich war Feedback zu Kommazahlen?    | 2             | 2             | 2             | 3             | 3             | 2             | 1             | 3             | 4             | 1              | 2,3              |

---

## **Einleitungstext**
Testfeedback Fragebogen
Mit diesem Fragebogen möchte ich herausfinden, wie hilfreich KI-generiertes Feedback zu Programmiertests in der ArTEMiS-Lernumgebung für Programmieranfänger*innen ist. Programmiertests sind kurze Codeabschnitte, die überprüfen, ob ein anderer Code wie erwartet funktioniert.
Falls dir Begriffe wie „Codeabschnitt“ und „Programmiertest“ noch kompliziert vorkommen, keine Sorge – diese Umfrage ist genau für dich gemacht!
Bitte beantworte die Fragen so genau und ehrlich wie möglich.
Vielen Dank für deine Teilnahme!

--- 

## **Aufgaben der Teilnehmenden**
Deine Aufgabe
Stell dir vor, du sollst einen Programmiercode schreiben, der zwei Zahlen addiert (Additionsfunktion). Damit deine Lösung als korrekt gilt, müssen alle Programmiertests bestanden werden. Du erhältst jedoch Fehlermeldungen, diese sind in den folgenden Fragen aufgeführt. Kannst du herausfinden, warum dein Code nicht funktioniert?

---

## **Hinweis-Einschub**
Feedback-Nachrichten
Werfen wir nun einen genaueren Blick auf die Feedback-Nachrichten, die jeweils am Anfang der Fehlermeldung nach ‘AssertionError:’ in den ersten drei Fragen zu finden sind.
(VORSICHT: Die Fragen unterscheiden sich, bitte lies sie dir genau durch!)

---

## **Frage 1**

**Warum funktioniert dein Code nicht?**

AssertionError: 0 != 1 : ‚add‘ soll mit ‚0‘ addieren können. Stelle sicher, dass der Code ‚0‘ korrekt behandelt. Hast du getestet, ob ‚0‘ als Teil der Addition funktioniert?

self = < behavior.behavior_test.TestAddFunctionBehavior testMethod=test_add_zero_and_integer >

def test_add_zero_and_integer(self):
"""
Prüft, ob ‚add‘ die Zahl ‚0‘ korrekt addiert.
"""
> self.assertEqual(
add(0, 1), 1,
"’add‘ soll mit ‚0‘ addieren können. Stelle sicher, dass der Code ‚0‘ korrekt behandelt. Hast du getestet, ob ‚0‘ als Teil der Addition funktioniert?“
)

Antwortoptionen: 
1 Weil sehr große Zahlen falsch addiert wurden.
2 Weil eine positive und eine negative Zahl falsch addiert wurden.
3 Weil zwei positive Zahlen falsch addiert wurden.
4 Weil 0 nicht richtig addiert wurde.
5 Weil nur eine Zahl, statt zwei Zahlen eingegeben wurde.
6 Keine der Optionen ist richtig.
7 Ich weiß es nicht.

Proband 1: 4
Proband 2: 4
Proband 3: 7
Proband 4: 7
Proband 5: 4
Proband 6: 4
Proband 7: 4
Proband 8: 4
Proband 9: 4
Proband 10: 4

---

## **Frage 2**

**Warum funktioniert dein Code nicht?**


AssertionError: 3 != 1 : ‚add‘ soll eine negative und eine positive Zahl addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden. Wie behandelst du Vorzeichen in deinem Code?

self = < behavior.behavior_test.TestAddFunctionBehaviortestMethod=test_add_positive_and_negative_integer >

def test_add_positive_and_negative_integer(self):
"""
Prüft, ob ‚add‘ eine positive und eine negative Zahl korrekt addiert.
"""
> self.assertEqual(
add(-2, 3), 1,
"’add‘ soll eine negative und eine positive Zahl addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden. Wie behandelst du Vorzeichen in deinem Code?“
)

Antwortoptionen: 
1 Weil sehr große Zahlen falsch addiert wurden.
2 Weil eine positive und eine negative Zahl falsch addiert wurden.
3 Weil zwei positive Zahlen falsch addiert wurden.
4 Weil 0 nicht richtig addiert wurde.
5 Weil nur eine Zahl, statt zwei Zahlen eingegeben wurde.
6 Keine der Optionen ist richtig.
7 Ich weiß es nicht.

Proband 1: 2
Proband 2: 2
Proband 3: 1
Proband 4: 7
Proband 5: 2
Proband 6: 2
Proband 7: 2
Proband 8: 2
Proband 9: 2
Proband 10: 2

---

## **Frage 3**

**Warum funktioniert dein Code nicht?**

AssertionError: 4.5 != 4.0 : ‚add‘ soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt summiert werden. Wird das Ergebnis auf die richtige Genauigkeit geprüft?

self = < behavior.behavior_test.TestAddFunctionBehavior testMethod=test_add_two_floats >

def test_add_two_floats(self):
"""
Prüft, ob ‚add‘ zwei Kommazahlen korrekt addiert.
"""
> self.assertEqual(
add(1.5, 2.5), 4.0,
"’add‘ soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt summiert werden. Wird das Ergebnis auf die richtige Genauigkeit geprüft?“
)

Antwortoptionen: 
1 Weil sehr große Zahlen falsch addiert wurden.
2 Weil eine positive und eine negative Zahl falsch addiert wurden.
3 Weil zwei positive Zahlen falsch addiert wurden.
4 Weil 0 nicht richtig addiert wurde.
5 Weil nur eine Zahl, statt zwei Zahlen eingegeben wurde.
6 Keine der Optionen ist richtig.
7 Ich weiß es nicht.

Proband 1: 6
Proband 2: 6
Proband 3: 3
Proband 4: 7
Proband 5: 3
Proband 6: 3
Proband 7: 6
Proband 8: 6
Proband 9: 6
Proband 10: 6

---

## **Frage 4**

**Wie hilfreich fandest du diesen Satz, um bei der ersten Frage herauszufinden, warum dein Code nicht funktioniert?**

‚add‘ soll mit ‚0‘ addieren können. Stelle sicher, dass der Code ‚0‘ korrekt behandelt. Hast du getestet, ob ‚0‘ als Teil der Addition funktioniert?

Antwortoptionen:
1 Sehr hilfreich
2 Hilfreich
3 Neutral
4 eher nicht hilfreich
5 Gar nicht Hilfreich

Proband 1: 1
Proband 2: 1
Proband 3: 2
Proband 4: 3
Proband 5: 1
Proband 6: 1
Proband 7: 1
Proband 8: 4
Proband 9: 1
Proband 10: 1

---

## **Frage 5**

**Wie verständlich findest du diesen Satz aus Frage zwei?**

‚add‘ soll eine negative und eine positive Zahl addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden. Wie behandelst du Vorzeichen in deinem Code?

1 Sehr verständlich
2 verständlich
3 Neutral
4 eher nicht verständlich
5 Gar nicht verständlich

Proband 1: 1
Proband 2: 1
Proband 3: 2
Proband 4: 2
Proband 5: 3
Proband 6: 1
Proband 7: 1
Proband 8: 3
Proband 9: 2
Proband 10: 1

---

## **Frage 6**

**Wie hilfreich würdest du diesen Satz aus Frage drei finden, um an einer Lösung der Aufgabe weiterzuarbeiten?**

‚add‘ soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt summiert werden. Wird das Ergebnis auf die richtige Genauigkeit geprüft?

1 Sehr hilfreich
2 Hilfreich
3 Neutral
4 eher nicht hilfreich
5 Gar nicht Hilfreich

Proband 1: 2
Proband 2: 2
Proband 3: 2
Proband 4: 3
Proband 5: 3
Proband 6: 2
Proband 7: 1
Proband 8: 3
Proband 9: 4
Proband 10: 1
