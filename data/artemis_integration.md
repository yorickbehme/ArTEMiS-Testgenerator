## **Nutzerstudie Erstellung für ArTEMiS**

Im folgenden wird Struktueriert aufgezeigt, wie mit Hilfe des Programmes 'ArTEMiS-Testgenerator' Aufgabenstellungen für die Artemis-Lernplattform in Kurse umgesetzt werden können. Der Prozess gliedert sich in folgende Schritte: 
1. Aufgabenstellung entwickeln
3. Aufgabenstellung für ArTEMiS optimieren
4. Musterlösung entwickeln
5. Testscript mit 'ArTEMiS-Testgenerator' generieren
6. Einpflegen in ArTEMiS

## **Aufgabe 1:**

### **Orginal aus Altaufgabensammlug**

---

Implementiere ein Pythonprogramm, das den Umfangs eines Rechtecks berechnet. Dabei sollen zuerst die zwei Seiten a und b mit der Funktion input eingelesen werden und anschließend das Ergebnis ausgegeben werden. Gib dem Benutzer entsprechend Auskunft, was eingelesen wird und was die Ausgabe bedeutet.

---

### **ArTEMiS-Aufgabenstellung**

---
# Implementiere ein Rechteck-Umfang-Berechnungsprogramm

[task][Implementiere ein Pythonprogramm, das **den Umfang eines Rechtecks berechnet**.](test_positive_input,test_negative_input,test_large_input,test_output_contains_correct_phrase)
Dabei sollen folgende Schritte durchgeführt werden:

1. Lese die beiden Seitenlängen `a` und `b` des Rechtecks mit der Funktion `input()` ein.
2. Berechne den Umfang des Rechtecks mit der Formel `u = 2 * (a + b)`.
3. Gib das Ergebnis in einer verständlichen Nachricht aus, die den Benutzer über den berechneten Umfang informiert.


---

### **Musterlösung**

---

```
# Calculates the perimeter of a rectangle based on user input.
a = int(input("Gib bitte die Länge der Seite 1 ein:"))
b = int(input("Gib bitte die Länge der Seite 2 ein:"))
u = 2*(a+b)
ausgabe = "Der Umfang des Rechtecks beträgt: "+ str(u)
print(ausgabe)
```

---

### **Testgenerierung**

***Mit 'Input/Output ohne Funktion' Prompt***

---

```
import unittest
from unittest.mock import patch
from io import StringIO
import importlib

class TestRectanglePerimeterBehavior:
    """
    Testklasse für das Verhalten der Rechteckumfangsberechnung.
    """

    def test_positive_input(self):
        """
        Testet die Berechnung bei positiven Längen-Eingaben.
        """
        with patch('builtins.input', return_value='5'), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            import assignment.rectangle_perimeter
            importlib.reload(assignment.rectangle_perimeter)
            output = mock_stdout.getvalue().strip()

            # Überprüfe die Ausgabe
            assert "Der Umfang des Rechtecks beträgt: 20." in output, (
                "Das Programm sollte positive Input korrekt berechnen und ausgeben. "
                "Hast du überprüft, ob die Berechnung korrekt implementiert ist?"
            )

    def test_negative_input(self):
        """
        Testet die Berechnung bei negativen Längen-Eingaben.
        """
        with patch('builtins.input', return_value='-3'), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            import assignment.rectangle_perimeter 
            importlib.reload(assignment.rectangle_perimeter)
            output = mock_stdout.getvalue().strip()

            # Überprüfe die Ausgabe
            assert "Der Umfang des Rechtecks beträgt: 10." in output, (
                "Das Programm sollte negative Input korrekt berechnen und ausgeben. "
                "Wird bei negativen Werten die Berechnung richtig angewendet und die Ausgabe korrekt formatiert?"
            )

    def test_large_input(self):
        """
        Testet die Berechnung bei sehr großen Längen-Eingaben.
        """
        with patch('builtins.input', return_value='1000000'), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            import assignment.rectangle_perimeter 
            importlib.reload(assignment.rectangle_perimeter)
            output = mock_stdout.getvalue().strip()

            # Überprüfe die Ausgabe
            assert "Der Umfang des Rechtecks beträgt: 4000000." in output, (
                "Das Programm sollte mit großem Input korrekt umgehen. "
                "Hast du darauf geachtet, dass der Code keine Fehler bei sehr großen Zahlen wirft?"
            )

    def test_float_input(self):
        """
        Testet die Berechnung bei einer Fließkommazahl als Länge-Eingabe.
        """
        with patch('builtins.input', return_value='37.5'), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            import assignment.rectangle_perimeter
            importlib.reload(assignment.rectangle_perimeter)
            output = mock_stdout.getvalue().strip()

            # Überprüfe die Ausgabe
            assert "Der Umfang des Rechtecks beträgt: 95.0." in output, (
                "Das Programm sollte gleitkomma Input korrekt berechnen und ausgeben. "
                "Überprüfe, ob die Berechnung für nicht-ganzzahlige Werte exakt ist."
            )


class TestRectanglePerimeterStructure:
    """
    Testklasse für die Struktur der Rechteckumfangsberechnung.
    """

    def test_output_contains_correct_phrase(self):
        """
        Prüft, ob die Ausgabe die richtige Formulierung enthält.
        """
        with patch('builtins.input', return_value='25'), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            import assignment.rectangle_perimeter
            importlib.reload(assignment.rectangle_perimeter)
            output = mock_stdout.getvalue().strip()

            # Strukturprüfung der Ausgabe
            assert "Der Umfang des Rechtecks beträgt: " in output, (
                "Die Ausgabe sollte den Text 'Der Umfang des Rechtecks beträgt: ' enthalten. "
                "Ist sichergestellt, dass die Ausgabe einheitlich formatiert ist?"
            )
```

---

### **Einpflegen in ArTEMiS**

---

Das Einpflegen in ArTEMiS funktioniert in folgenden Schritten: 
1. TestKlassen in den jeweils passenden vordefinierten File kopieren (behavior_test.py bzw. structural_test.py)
2. float Testcase entfernen 
3. Leichte Veränderungen an  den erwarteten Ausgaben machen ('.' entfernen und Ergebnis für test_negativ_input korregieren)

---

## **Aufgabe 2:**

### **Original aus Altaufgabensammlung**

---

Implementiere eine Funktion, die eine Liste als Parameter erhält und die Länge der Liste zurückliefert.

---

### **ArTEMiS-Aufgabenstellung**

---

# Implementiere Listen längen Funktionen

[task][Implementiere eine Funktion namens `list_length`, die die Länge einer Liste zurückgebt.](test_function_exists, test_list_length_for_empty_list, test_list_length_for_mixed_types, test_list_length_for_multiple_elements, test_list_length_for_single_element)
Dabei sollen folgende Schritte durchgeführt werden:

1. Erstelle Eine funktion mit dem namen `list_length`, die eine Liste als Parameter entgegen nimmt.
2. Berechne die Länge der Liste und gib diese zurück.



---

### **Musterlösung**

---

```
def list_length(lst):
    return len(lst)
```

---

### **Testgenerierung**

***Mit 'Einfache Funktion' (Standardprompt) generiert***

---

```
import unittest
from assignment.list import ...  # Importiere den zu testenden Code

class TestListFunctionBehavior(unittest.TestCase):

    def test_list_length_for_empty_list(self):
        """
        Prüft, ob 'list_length' eine leere Liste korrekt auf 0 setzt.
        """
        self.assertEqual(
            list_length([]), 0,
            "'list_length' soll eine leere Liste auf 0 setzen. Überprüfe, ob die Funktion für einfache Listenkorrektheit funktioniert."
        )

    def test_list_length_for_single_element(self):
        """
        Prüft, ob 'list_length' eine Liste mit einem Element korrekt auf 1 setzt.
        """
        self.assertEqual(
            list_length([1]), 1,
            "'list_length' soll eine Liste mit einem Element auf 1 setzen. Vergewissere dich, dass die Funktion für Listen mit einem Element funktioniert."
        )

    def test_list_length_for_multiple_elements(self):
        """
        Prüft, ob 'list_length' eine Liste mit mehreren Elementen korrekt auf die Anzahl der Elemente setzt.
        """
        self.assertEqual(
            list_length([1, 2, 3]), 3,
            "'list_length' soll eine Liste mit mehreren Elementen auf die Anzahl der Elemente setzen. Überprüfe, ob die Funktion für Listen mit mehreren Elementen funktioniert."
        )

    def test_list_length_for_mixed_types(self):
        """
        Prüft, ob 'list_length' eine Liste mit verschiedenen Typen korrekt auf die Anzahl der Elemente setzt.
        """
        self.assertEqual(
            list_length([1, "a", 2.5]), 3,
            "'list_length' soll eine Liste mit verschiedenen Typen auf die Anzahl der Elemente setzen. Überprüfe, ob die Funktion für Listen mit verschiedenen Typen funktioniert."
        )

class TestListFunctionStructure(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'list_length' existiert.
        """
        self.assertTrue(
            callable(list_length),
            "'list_length' soll existieren. Vergewissere dich, dass die Funktion definiert ist. Hast du überprüft, ob die Funktion richtig geschrieben wurde?"
        )
```

---

### **Einpflegen in ArTEMiS**

---

Das Einpflegen in ArTEMiS funktioniert in folgenden Schritten: 
1. TestKlassen in den jeweils passenden vordefinierten File kopieren (behavior_test.py bzw. structural_test.py)
2. Import mit passendem File und Funktionsnamen anpassen

---

## **Aufgabe 3:**

### **Original aus Altaufgabensammlung**

---

Implementiere ein Programm, dass die Zahlen der übergebenen Liste [2,5,7,86,1,0] nacheinander ausgibt. Die Funktion bekommt als ersten Parameter eine 0 und als zweiten Parameter die Liste übergeben. Löse dies rekursiv.

---

### **ArTEMiS-Aufgabenstellung**

---

# Implementiere ein Programm zur Ausgabe einer Zahlenliste

[task][Implementiere ein Pythonprogramm, das die Zahlen einer übergebenen Liste nacheinander ausgibt.](test_print_positive_numbers_rec,test_print_zero_rec,test_print_of_positive_numbers_it,test_print_of_zero_it,test_print_of_negative_numbers_it,test_function_exists_rec,test_is_recursive,test_function_exists_it,test_is_iterative)
 Dabei sollen folgende Schritte durchgeführt werden:

1. Schreibe eine **rekursive Funktion** namens `print_list_recursive`, die folgende Parameter erhält:
   - `index`: Der Startindex, der initial den Wert `0` hat.
   - `lst`: Die Liste, deren Zahlen ausgegeben werden sollen.
2. Die Funktion soll:
   - Die aktuelle Zahl an der Position `index` ausgeben.
   - Sich selbst mit dem nächsten Index aufrufen, bis das Ende der Liste erreicht ist.

3. Schreibe eine **iterative Funktion** namens `print_list_iterative`, die:
   - Die Liste als Parameter erhält.
   - Eine Schleife verwendet, um die Zahlen der Liste nacheinander auszugeben.

4. Teste beide Funktionen mit der Liste `[2, 5, 7, 86, 1, 0]`.
5. Stelle sicher, dass jede Zahl in einer neuen Zeile ausgegeben wird.

---

### **Musterlösung**

```
# Rekursive Funktion
def print_list_recursive(index, lst):
    if index < len(lst):
        print(lst[index])
        print_list_recursive(index + 1, lst)

# Iterative Funktion
def print_list_iterative(lst):
    for number in lst:
        print(number)
```

---

### **Testgenerierung**

***Mit 'Rekursive Funktion mit Output' und 'Iterative Funktion mit Output' generiert***

---

```
import unittest
from unittest.mock import patch
from io import StringIO
from assignment.print_list_recursive import print_list_recursive  # Ersetze mit der tatsächlichen Datei und Funktion

class TestPrintListRecursiveBehavior(unittest.TestCase):
    """
    Testklasse für das Verhalten der Funktion 'print_list_recursive'.
    """

    def test_print_positive_numbers(self):
        """
        Prüft die Ausgabe bei positiven Zahlen.
        """
        expected_output = "1\n2\n3\n4\n5\n" 
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_list_recursive(0, [1, 2, 3, 4, 5])
            self.assertEqual(
                mock_stdout.getvalue(),
                expected_output,
                "'print_list_recursive' soll die Zahlen korrekt ausgeben. "
                "Überprüfe, ob die Zahlen bei jedem Schritt korrekt berechnet und ausgegeben werden."
            )

    def test_print_zero(self):
        """
        Prüft die Ausgabe bei der Eingabe 0.
        """
        expected_output = "" 
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_list_recursive(5, [1, 2, 3, 4, 5])
            self.assertEqual(
                mock_stdout.getvalue(),
                expected_output,
                "'print_list_recursive' soll keine Ausgabe erzeugen, wenn die Eingabe 0 ist. "
                "Falls du eine Ausgabe erzeugest, überprüfe, ob dies korrekt implementiert ist."
            )

class TestPrintListRecursiveStructure(unittest.TestCase):
    """
    Testklasse für die strukturellen Aspekte der Funktion 'print_list_recursive'.
    """

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'print_list_recursive' existiert.
        """
        self.assertTrue(
            callable(print_list_recursive),
            "'print_list_recursive' soll existieren. Vergewissere dich, dass die Funktion im Modul korrekt definiert ist."
        )

    def test_is_recursive(self):
        """
        Prüft, ob die Funktion 'print_list_recursive' rekursiv implementiert wurde.
        """
        import inspect
        source_code = inspect.getsource(print_list_recursive)
        occurrences = source_code.count("print_list_recursive(")

        self.assertGreaterEqual(
            occurrences,
            2,
            "'print_list_recursive' soll rekursiv implementiert sein. Der rekursive Aufruf wurde nicht gefunden. "
            "Stelle sicher, dass die Funktion sich selbst korrekt aufruft."
        )
        self.assertNotIn(
            "for",
            source_code,
            "'print_list_recursive' soll rekursiv implementiert sein. Schleifen (z. B. 'for') sind nicht erlaubt. "
            "Falls du eine Schleife verwendest, ersetze sie durch einen rekursiven Aufruf."
        )
        self.assertNotIn(
            "while",
            source_code,
            "'print_list_recursive' soll rekursiv implementiert sein. Schleifen (z. B. 'while') sind nicht erlaubt. "
            "Falls du eine Schleife verwendest, überprüfe, wie sie durch Rekursion ersetzt werden kann."
        )


import unittest
from io import StringIO
from unittest.mock import patch


class TestPrintListIterativeBehavior(unittest.TestCase):

    def test_print_of_positive_numbers(self):
        """
        Prüft die Ausgabe bei positiven Zahlen.
        """
        expected_output = "1\n2\n3\n" 
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_list_iterative([1, 2, 3])
            self.assertEqual(
                mock_stdout.getvalue(),
                expected_output,
                "'print_list_iterative' soll die Elemente korrekt ausgeben. "
                "Hast du sichergestellt, dass alle Elemente korrekt ausgegeben werden?"
            )

    def test_print_of_zero(self):
        """
        Prüft die Ausgabe bei der Eingabe 0.
        """
        expected_output = "" 
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_list_iterative([0])
            self.assertEqual(
                mock_stdout.getvalue(),
                expected_output,
                "'print_list_iterative' soll keine Ausgabe machen, wenn 0 eingegeben wird. "
                "Wird der Sonderfall für die Eingabe 0 korrekt behandelt?"
            )

    def test_print_of_negative_numbers(self):
        """
        Prüft die Ausgabe bei negativen Zahlen.
        """
        expected_output = "-1\n-2\n" 
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_list_iterative([-1, -2])
            self.assertEqual(
                mock_stdout.getvalue(),
                expected_output,
                "'print_list_iterative' soll die Elemente korrekt ausgeben. "
                "Hast du sichergestellt, dass alle Elemente korrekt ausgegeben werden?"
            )


class TestPrintListIterativeStructure(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'print_list_iterative' existiert.
        """
        self.assertTrue(
            callable(print_list_iterative),
            "'print_list_iterative' soll existieren. Vergewissere dich, dass die Funktion im Modul korrekt definiert ist."
        )

    def test_is_iterative(self):
        """
        Prüft, ob die Funktion 'print_list_iterative' iterativ implementiert wurde.
        """
        import inspect
        source_code = inspect.getsource(print_list_iterative)
        self.assertNotIn(
            "return print_list_iterative",
            source_code,
            "'print_list_iterative' soll iterativ implementiert sein. Es wurden rekursive Aufrufe gefunden. "
            "Hast du überprüft, ob eine Schleife zur Ausgabe verwendet wird?"
        )
        self.assertIn(
            "for",
            source_code,
            "'print_list_iterative' soll iterativ implementiert sein. Eine Schleife (z. B. 'for') wird erwartet. "
            "Überprüfe, ob der Code tatsächlich iterativ arbeitet."
        )
```

---

### **Einpflegen in ArTEMiS**

---

Das Einpflegen in ArTEMiS funktioniert in folgenden Schritten: 
1. TestKlassen in den jeweils passenden vordefinierten File kopieren (behavior_test.py bzw. structural_test.py)
2. Import mit passendem File und Funktionsnamen anpassen
3. TestPrintListIterativeBehavior::test_print_of_zero Erwartung von '' auf '0\n' ändern. 
4. Doppel vergebene Namen eindeutig gemacht

---
