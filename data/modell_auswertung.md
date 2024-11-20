# **Modellauswertung**

In der folgenden Analyse werden die Modelle **Llama3** (lokal installiert mit Ollama) und **GPT-4o** hinsichtlich ihrer Leistungsfähigkeit bei der Testgenerierung untersucht. Jedes Modell wird mit fünf repräsentativen **Testfällen** getestet, wobei jeder Testfall in drei Durchläufen evaluiert wird. Als Eingabe dient der zuvor in der **Promptuntersuchung** entwickelte **Kombinationsprompt**, der mit den jeweiligen Testfällen ergänzt und den Modellen übergeben wird.

Die Ergebnisse der Modelle werden anschließend mit einer vordefinierten Liste von **Standard-Testfällen** abgeglichen, bewertet und in ein Punktesystem überführt. Abschließend werden die Ergebnisse in einer Vergleichstabelle zusammengefasst und gegenübergestellt.

---


## **Llama3**

### **Test 1:**

---

Here is the complete Python test suite for the provided code:

```
import unittest

class TestSubFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(4, 1), 3, "'sub' soll zwei positive Ganzzahlen subtrahieren können. Überprüfe, ob der Code für einfache Differenzen funktioniert.")

    def test_sub_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-2, -3), 1, "'sub' soll zwei negative Ganzzahlen subtrahieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_sub_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(3, -2), 5, "'sub' soll eine negative und eine positive Zahl subtrahieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_sub_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(4.5, 2.0), 2.5, "'sub' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt subtrahiert werden.")

    def test_sub_float_and_integer(self):
        """
        Prüft, ob 'sub' eine Kommazahl und eine Ganzzahl korrekt subtrahiert.
        """
        self.assertEqual(sub(3.5, 1), 2.5, "'sub' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_sub_zero_and_integer(self):
        """
        Prüft, ob 'sub' die Zahl '0' korrekt subtrahiert.
        """
        self.assertEqual(sub(1, 0), 1, "'sub' soll mit '0' subtrahieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_sub_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(float('inf'), float('-inf')), 0, "'sub' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub(1, None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 10/10**

---

```
import unittest

class TestSubFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(4, 2), 2, "'sub' soll zwei positive Ganzzahlen subtrahieren können. Überprüfe, ob der Code für einfache Differenzen funktioniert.")

    def test_sub_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-2, -3), 1, "'sub' soll zwei negative Ganzzahlen subtrahieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_sub_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(3, -2), 5, "'sub' soll eine positive und eine negative Zahl subtrahieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_sub_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(3.5, 2.0), 1.5, "'sub' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt subtrahiert werden.")

    def test_sub_float_and_integer(self):
        """
        Prüft, ob 'sub' eine Kommazahl und eine Ganzzahl korrekt subtrahiert.
        """
        self.assertEqual(sub(3.0, 1), 2.0, "'sub' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_sub_zero_and_integer(self):
        """
        Prüft, ob 'sub' die Zahl '0' korrekt subtrahiert.
        """
        self.assertEqual(sub(1, 0), 1, "'sub' soll mit '0' subtrahieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_sub_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(float('inf'), 1), float('inf'), "'sub' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub(1, None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 10/10**

---

Here is the complete Python test suite for the provided code:

```
import unittest
from your_module import add  # Assuming the function 'add' is defined in this module

class TestAddFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'add' existiert.
        """
        self.assertTrue(callable(add), "'add' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_add_two_positive_integers(self):
        """
        Prüft, ob 'add' zwei positive Ganzzahlen korrekt addiert.
        """
        self.assertEqual(add(1, 2), 3, "'add' soll zwei positive Ganzzahlern addieren können. Überprüfe, ob der Code für einfache Summen funktioniert.")

    def test_add_two_negative_integers(self):
        """
        Prüft, ob 'add' zwei negative Ganzzahlen korrekt addiert.
        """
        self.assertEqual(add(-1, -2), -3, "'add' soll zwei negative Ganzzahlen addieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_add_positive_and_negative_integer(self):
        """
        Prüft, ob 'add' eine positive und eine negative Zahl korrekt addiert.
        """
        self.assertEqual(add(-2, 3), 1, "'add' soll eine negative und eine positive Zahl addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_add_two_floats(self):
        """
        Prüft, ob 'add' zwei Kommazahlen korrekt addiert.
        """
        self.assertEqual(add(1.5, 2.5), 4.0, "'add' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt summiert werden.")

    def test_add_float_and_integer(self):
        """
        Prüft, ob 'add' eine Kommazahl und eine Ganzzahl korrekt addiert.
        """
        self.assertEqual(add(1.5, 1), 2.5, "'add' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_add_zero_and_integer(self):
        """
        Prüft, ob 'add' die Zahl '0' korrekt addiert.
        """
        self.assertEqual(add(0, 1), 1, "'add' soll mit '0' addieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_add_large_number(self):
        """
        Prüft, ob 'add' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(add(float('inf'), 1), float('inf'), "'add' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'add' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): add("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'add' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): add(1, None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "sub" Funkton existiert ❌
2. Subtrahiert zwei positive Ganzzahlen ❌
3. Subtrahiert zwei negative Ganzzahlen ❌
4. Subtrahiert eine positive und eine negative Ganzzahlen ❌
5. Subtrahiert zwei Gleitkommazahlen ❌
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Subtrahiert eine Ganzzahl mit 0 ❌
8. Subtrahiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Bemerkungen:
- Alle Testfälle wurden auf 'add' Bezogen, daher alle Fehlerhaft

**Punkte: 1/10**

**Total: 21/30**
'''


Test 2:
1. ###
Here is the Python test suite for the provided code:

```
import unittest
from your_module import add, sub, mul, div  # replace 'your_module' with the actual name of the module containing the functions

class TestFunctions(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktionen 'add', 'sub', 'mul', und 'div' existieren.
        """
        self.assertTrue(callable(add), "'add' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")
        self.assertTrue(callable(mul), "'mul' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")
        self.assertTrue(callable(div), "'div' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_add_function(self):
        """
        Prüft, ob 'add' korrekt addiert.
        """
        self.assertEqual(add(1, 2), 3, "'add' soll einfache Additionen durchführen. Überprüfe, ob die Funktionalität für Ganzzahlen und Kommazahlen umgeht.")
        self.assertEqual(add(-1, -2), -3, "'add' soll negative Zahlen addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")
        self.assertEqual(add(0, 1), 1, "'add' soll die Zahl '0' korrekt addieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_sub_function(self):
        """
        Prüft, ob 'sub' korrekt subtrahiert.
        """
        self.assertEqual(sub(1, 2), -1, "'sub' soll einfache Subtraktionen durchführen. Überprüfe, ob die Funktionalität für Ganzzahlen und Kommazahlen umgeht.")
        self.assertEqual(sub(-1, -2), 1, "'sub' soll negative Zahlen subtrahieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_mul_function(self):
        """
        Prüft, ob 'mul' korrekt multipliziert.
        """
        self.assertEqual(mul(1, 2), 2, "'mul' soll einfache Multiplikationen durchführen. Überprüfe, ob die Funktionalität für Ganzzahlen und Kommazahlen umgeht.")
        self.assertEqual(mul(-1, -2), 2, "'mul' soll negative Zahlen multiplizieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_div_function(self):
        """
        Prüft, ob 'div' korrekt dividiert.
        """
        self.assertEqual(div(1, 2), 0.5, "'div' soll einfache Divisionen durchführen. Überprüfe, ob die Funktionalität für Ganzzahlen und Kommazahlen umgeht.")
        with self.assertRaises(ZeroDivisionError, msg="'div' soll bei nullteilen einen Fehler werfen. Überprüfe, ob der Code für solche Fälle bereit ist."): div(1, 0)
        self.assertEqual(div(-1, -2), 0.5, "'div' soll negative Zahlen dividieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_invalid_type_string(self):
        """
        Prüft, ob die Funktionen bei String-Eingaben einen Typfehler auslösen.
        """
        with self.assertRaises(TypeError, msg="Die Funktionen sollen für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): add("a", 1)
        with self.assertRaises(TypeError, msg="Die Funktionen sollen für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob die Funktionen bei 'None'-Eingaben einen Typfehler auslösen.
        """
        with self.assertRaises(TypeError, msg="Die Funktionen sollen für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): add(1, None)
        with self.assertRaises(TypeError, msg="Die Funktionen sollen für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub(1, None)

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ❌
5. Subtrahiert zwei Gleitkommazahlen ❌
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Subtrahiert eine Ganzzahl mit 0 ❌
8. Subtrahiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "mul" Funkton existiert ✅
2. Multipliziert zwei positive Ganzzahlen ✅
3. Multipliziert zwei negative Ganzzahlen ✅
4. Multipliziert eine positive und eine negative Ganzzahlen ❌
5. Multipliziert zwei Gleitkommazahlen ❌
6. Multipliziert eine Gleitkommazahl und eine Ganzzahl ❌
7. Multipliziert eine Ganzzahl mit 0 ❌
8. Multipliziert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "div" Funkton existiert ✅
2. Dividiert zwei positive Ganzzahlen ✅
3. Dividiert zwei negative Ganzzahlen ✅
4. Dividiert eine positive und eine negative Ganzzahlen ❌
5. Dividiert zwei Gleitkommazahlen ❌
6. Dividiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Wirft einen Error für Division mit 0❌
8. Dividiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:
- 'add' Testfälle wurden fälschlicherweise mit implementiert. 

Punkte: 13/30
'''

2. ###
Here is the Python test suite for the provided code:

```
import unittest

class TestOperations(unittest.TestCase):

    def test_sub_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(2, 1), 1, "'sub' soll zwei positive Ganzzahlen subtrahieren können. Überprüfe, ob der Code für einfache Differenzen funktioniert.")

    def test_sub_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-2, -1), -1, "'sub' soll zwei negative Ganzzahlen subtrahieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_sub_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(3, -2), 5, "'sub' soll eine negative und eine positive Zahl subtrahieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_sub_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(2.5, 1.0), 1.5, "'sub' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt subtrahiert werden.")

    def test_sub_float_and_integer(self):
        """
        Prüft, ob 'sub' eine Kommazahl und eine Ganzzahl korrekt subtrahiert.
        """
        self.assertEqual(sub(2.5, 1), 1.5, "'sub' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_sub_zero_and_integer(self):
        """
        Prüft, ob 'sub' die Zahl '0' korrekt subtrahiert.
        """
        self.assertEqual(sub(2, 1), 1, "'sub' soll mit '0' subtrahieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_sub_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(float('inf'), 1), float('inf'), "'sub' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_sub_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub("a", 1)

    def test_sub_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub(1, None)

    def test_mul_function_exists(self):
        """
        Prüft, ob die Funktion 'mul' existiert.
        """
        self.assertTrue(callable(mul), "'mul' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_mul_two_positive_integers(self):
        """
        Prüft, ob 'mul' zwei positive Ganzzahlen korrekt multipliziert.
        """
        self.assertEqual(mul(2, 3), 6, "'mul' soll zwei positive Ganzzahlen multiplizieren können. Überprüfe, ob der Code für einfache Multiplikationen funktioniert.")

    def test_mul_two_negative_integers(self):
        """
        Prüft, ob 'mul' zwei negative Ganzzahlen korrekt multipliziert.
        """
        self.assertEqual(mul(-2, -3), 6, "'mul' soll zwei negative Ganzzahlen multiplizieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_mul_positive_and_negative_integer(self):
        """
        Prüft, ob 'mul' eine positive und eine negative Zahl korrekt multipliziert.
        """
        self.assertEqual(mul(-2, 3), -6, "'mul' soll eine negative und eine positive Zahl multiplizieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_mul_two_floats(self):
        """
        Prüft, ob 'mul' zwei Kommazahlen korrekt multipliziert.
        """
        self.assertEqual(mul(2.5, 1.0), 2.5, "'mul' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt multipliziert werden.")

    def test_mul_float_and_integer(self):
        """
        Prüft, ob 'mul' eine Kommazahl und eine Ganzzahl korrekt multipliziert.
        """
        self.assertEqual(mul(2.5, 1), 2.5, "'mul' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_mul_zero_and_integer(self):
        """
        Prüft, ob 'mul' die Zahl '0' korrekt multipliziert.
        """
        self.assertEqual(mul(2, 0), 0, "'mul' soll mit '0' multiplizieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_mul_large_number(self):
        """
        Prüft, ob 'mul' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(mul(float('inf'), 1), float('inf'), "'mul' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_mul_invalid_type_string(self):
        """
        Prüft, ob 'mul' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'mul' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): mul("a", 1)

    def test_mul_invalid_type_none(self):
        """
        Prüft, ob 'mul' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'mul' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): mul(1, None)

    def test_div_function_exists(self):
        """
        Prüft, ob die Funktion 'div' existiert.
        """
        self.assertTrue(callable(div), "'div' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_div_two_positive_integers(self):
        """
        Prüft, ob 'div' zwei positive Ganzzahlen korrekt dividiert.
        """
        self.assertEqual(div(6, 3), 2, "'div' soll zwei positive Ganzzahlen dividieren können. Überprüfe, ob der Code für einfache Divisionen funktioniert.")

    def test_div_two_negative_integers(self):
        """
        Prüft, ob 'div' zwei negative Ganzzahlen korrekt dividiert.
        """
        self.assertEqual(div(-6, -3), 2, "'div' soll zwei negative Ganzzahlen dividieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_div_positive_and_negative_integer(self):
        """
        Prüft, ob 'div' eine positive und eine negative Zahl korrekt dividiert.
        """
        self.assertEqual(div(-6, 3), -2, "'div' soll eine negative und eine positive Zahl dividieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_div_two_floats(self):
        """
        Prüft, ob 'div' zwei Kommazahlen korrekt dividiert.
        """
        self.assertEqual(div(2.5, 1.0), 2.5, "'div' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt dividieren werden.")

    def test_div_float_and_integer(self):
        """
        Prüft, ob 'div' eine Kommazahl und eine Ganzzahl korrekt dividiert.
        """
        self.assertEqual(div(2.5, 1), 2.5, "'div' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_div_zero_and_integer(self):
        """
        Prüft, ob 'div' die Zahl '0' korrekt dividiert.
        """
        self.assertRaises(ZeroDivisionError, lambda: div(2, 0))

    def test_div_large_number(self):
        """
        Prüft, ob 'div' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(div(float('inf'), 1), float('inf'), "'div' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_div_invalid_type_string(self):
        """
        Prüft, ob 'div' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'div' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): div("a", 1)

    def test_div_invalid_type_none(self):
        """
        Prüft, ob 'div' bei 'None'-Eingangen einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'div' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): div(1, None)
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Subtrahiert eine Ganzzahl mit 0 ❌
8. Subtrahiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "mul" Funkton existiert ✅
2. Multipliziert zwei positive Ganzzahlen ✅
3. Multipliziert zwei negative Ganzzahlen ✅
4. Multipliziert eine positive und eine negative Ganzzahlen ✅
5. Multipliziert zwei Gleitkommazahlen ✅
6. Multipliziert eine Gleitkommazahl und eine Ganzzahl ✅
7. Multipliziert eine Ganzzahl mit 0 ✅
8. Multipliziert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "div" Funkton existiert ✅
2. Dividiert zwei positive Ganzzahlen ✅
3. Dividiert zwei negative Ganzzahlen ✅
4. Dividiert eine positive und eine negative Ganzzahlen ✅
5. Dividiert zwei Gleitkommazahlen ✅
6. Dividiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Wirft einen Error für Division mit 0 ✅
8. Dividiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:
- Feedback für 'div' durch 0 fehlt

Punkte: 29/30
'''

3. ###
Here is the Python test suite for the provided code:

```
import unittest
from your_module import add, sub, mul, div

class TestMathFunctions(unittest.TestCase):

    def test_sub_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(2, 1), 1, "'sub' soll zwei positive Ganzzahlen subtrahieren können. Überprüfe, ob der Code für einfache Differenzen funktioniert.")

    def test_sub_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-2, -1), 1, "'sub' soll zwei negative Ganzzahlen subtrahieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_sub_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(2, -1), 3, "'sub' soll eine positive und eine negative Zahl subtrahieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_sub_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(2.5, 1.5), 1.0, "'sub' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt subtrahiert werden.")

    def test_sub_float_and_integer(self):
        """
        Prüft, ob 'sub' eine Kommazahl und eine Ganzzahl korrekt subtrahiert.
        """
        self.assertEqual(sub(1.5, 1), 0.5, "'sub' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_sub_zero_and_integer(self):
        """
        Prüft, ob 'sub' die Zahl '0' korrekt subtrahiert.
        """
        self.assertEqual(sub(1, 0), 1, "'sub' soll mit '0' subtrahieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_sub_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(float('inf'), -1), float('inf'), "'sub' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_sub_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub("a", 1)

    def test_sub_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): sub(1, None)

    # Test for mul and div functions
    def test_mul_function_exists(self):
        """
        Prüft, ob die Funktion 'mul' existiert.
        """
        self.assertTrue(callable(mul), "'mul' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_div_function_exists(self):
        """
        Prüft, ob die Funktion 'div' existiert.
        """
        self.assertTrue(callable(div), "'div' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    # Test for mul function
    def test_mul_two_positive_integers(self):
        """
        Prüft, ob 'mul' zwei positive Ganzzahlen korrekt multipliziert.
        """
        self.assertEqual(mul(2, 3), 6, "'mul' soll zwei positive Ganzzahlen multiplizieren können. Überprüfe, ob der Code für einfache Produkte funktioniert.")

    def test_mul_two_negative_integers(self):
        """
        Prüft, ob 'mul' zwei negative Ganzzahlen korrekt multipliziert.
        """
        self.assertEqual(mul(-2, -3), 6, "'mul' soll zwei negative Ganzzahlen multiplizieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_mul_positive_and_negative_integer(self):
        """
        Prüft, ob 'mul' eine positive und eine negative Zahl korrekt multipliziert.
        """
        self.assertEqual(mul(2, -3), -6, "'mul' soll eine positive und eine negative Zahl multiplizieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_mul_two_floats(self):
        """
        Prüft, ob 'mul' zwei Kommazahlen korrekt multipliziert.
        """
        self.assertEqual(mul(2.5, 3.0), 7.5, "'mul' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt subtrahiert werden.")

    def test_mul_float_and_integer(self):
        """
        Prüft, ob 'mul' eine Kommazahl und eine Ganzzahl korrekt multipliziert.
        """
        self.assertEqual(mul(1.5, 2), 3.0, "'mul' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    # Test for div function
    def test_div_two_positive_integers(self):
        """
        Prüft, ob 'div' zwei positive Ganzzahlen korrekt dividiert.
        """
        self.assertEqual(div(6, 2), 3, "'div' soll zwei positive Ganzzahlen dividieren können. Überprüfe, ob der Code für einfache Quotienten funktioniert.")

    def test_div_two_negative_integers(self):
        """
        Prüft, ob 'div' zwei negative Ganzzahlen korrekt dividiert.
        """
        self.assertEqual(div(-6, -2), 3, "'div' soll zwei negative Ganzzahlen dividieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_div_positive_and_negative_integer(self):
        """
        Prüft, ob 'div' eine positive und eine negative Zahl korrekt dividiert.
        """
        self.assertEqual(div(6, -2), -3, "'div' soll eine positive und eine negative Zahl dividieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_div_invalid_type_string(self):
        """
        Prüft, ob 'div' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'div' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): div("a", 1)

    def test_div_invalid_type_none(self):
        """
        Prüft, ob 'div' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'div' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): div(1, None)

if __name__ == '__main__':
    test_suite = unittest.TestSuite([test_subtract, test_multiply, test_divide])
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ❌
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "mul" Funkton existiert ✅
2. Multipliziert zwei positive Ganzzahlen ✅
3. Multipliziert zwei negative Ganzzahlen ✅
4. Multipliziert eine positive und eine negative Ganzzahlen ✅
5. Multipliziert zwei Gleitkommazahlen ✅
6. Multipliziert eine Gleitkommazahl und eine Ganzzahl ✅
7. Multipliziert eine Ganzzahl mit 0 ❌
8. Multipliziert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "div" Funkton existiert ✅
2. Dividiert zwei positive Ganzzahlen ✅
3. Dividiert zwei negative Ganzzahlen ✅
4. Dividiert eine positive und eine negative Ganzzahlen ✅
5. Dividiert zwei Gleitkommazahlen ❌
6. Dividiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Wirft einen Error für Division mit 0 ❌
8. Dividiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste)✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 21/30

Total: 63/90
'''


Test 3: 
1. ###
```
import unittest
from your_module import add, MathOperations  # Import the code under test

class TestAddFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'add' existiert.
        """
        self.assertTrue(callable(add), "'add' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_add_two_positive_integers(self):
        """
        Prüft, ob 'add' zwei positive Ganzzahlen korrekt addiert.
        """
        self.assertEqual(add(1, 2), 3, "'add' soll zwei positive Ganzzahlen addieren können. Überprüfe, ob der Code für einfache Summen funktioniert.")

    def test_add_two_negative_integers(self):
        """
        Prüft, ob 'add' zwei negative Ganzzahlen korrekt addiert.
        """
        self.assertEqual(add(-1, -2), -3, "'add' soll zwei negative Ganzzahlen addieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_add_positive_and_negative_integer(self):
        """
        Prüft, ob 'add' eine positive und eine negative Zahl korrekt addiert.
        """
        self.assertEqual(add(-2, 3), 1, "'add' soll eine negative und eine positive Zahl addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_add_two_floats(self):
        """
        Prüft, ob 'add' zwei Kommazahlen korrekt addiert.
        """
        self.assertEqual(add(1.5, 2.5), 4.0, "'add' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt summiert werden.")

    def test_add_float_and_integer(self):
        """
        Prüft, ob 'add' eine Kommazahl und eine Ganzzahl korrekt addiert.
        """
        self.assertEqual(add(1.5, 1), 2.5, "'add' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_add_zero_and_integer(self):
        """
        Prüft, ob 'add' die Zahl '0' korrekt addiert.
        """
        self.assertEqual(add(0, 1), 1, "'add' soll mit '0' addieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_add_large_number(self):
        """
        Prüft, ob 'add' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(add(float('inf'), 1), float('inf'), "'add' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'add' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): add("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'add' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): add(1, None)

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "MathOperations" Klasse existiert ❌
2. "squere_root" Funkton existiert ❌
4. Wirft einen ValueError für eine negativen Ganzzahl ❌
4. Berechnet die Qadratwurzel einer negativen Ganzzahl ❌
5. Berechnet die Quadarwurzel von einer Gleitkommazahl ❌
6. Berechnet die Qadratwurzel von 0 ❌
7. Berechnet die Qadratwurzel von einer sehr großen Zahl ❌
8. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
9. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Fehlerhafte Testfälle:

Bemerkungen:
- Test fäschlicherweise für 'add' implementiert

Punkte: 0/9
'''

2. ###
Here is the Python test suite for the provided code:
```
import unittest
from your_module import MathOperations, add  # Replace 'your_module' with the actual module name

class TestMathOperations(unittest.TestCase):

    def test_square_root_function_exists(self):
        """
        Prüft, ob die Funktion 'square_root' existiert.
        """
        self.assertTrue(callable(MathOperations.square_root), "'square_root' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_square_root_positive_integer(self):
        """
        Prüft, ob 'square_root' eine positive Ganzzahl korrekt berechnet.
        """
        self.assertAlmostEqual(MathOperations.square_root(4), 2.0, places=5, msg="'square_root' soll eine positive Ganzzahl berechnen können. Überprüfe, ob der Code für einfache Wurzeln funktioniert.")

    def test_square_root_zero(self):
        """
        Prüft, ob 'square_root' die Zahl '0' korrekt berechnet.
        """
        self.assertAlmostEqual(MathOperations.square_root(0), 0.0, places=5, msg="'square_root' soll mit '0' berechnen können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_square_root_negative_integer(self):
        """
        Prüft, ob 'square_root' eine negative Ganzzahl korrekt berechnet.
        """
        with self.assertRaises(ValueError, msg="'square_root' soll für negative Zahlen einen Fehler werfen. Überprüfe, ob die Wurzelberechnung korrekt implementiert ist."): MathOperations.square_root(-1)

    def test_square_root_non_numeric_input(self):
        """
        Prüft, ob 'square_root' bei nicht-numeric-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'square_root' soll für nicht-numeric-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): MathOperations.square_root("a")

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "MathOperations" Klasse existiert ❌
2. "squere_root" Funkton existiert ✅
3. Berechnet die Qadratwurzel einer positiven Ganzzahl ✅
4. Wirft einen ValueError für eine negativen Ganzzahl ✅
5. Berechnet die Quadarwurzel von einer Gleitkommazahl ❌
6. Berechnet die Qadratwurzel von 0 ✅
7. Berechnet die Qadratwurzel von einer sehr großen Zahl ❌
8. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
9. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 6/9
'''

3. ###
Here is the comprehensive Python test suite for the provided code:

```python
import unittest
import math

class TestMathOperations(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'square_root' existiert.
        """
        self.assertTrue(callable(MathOperations.square_root), "'square_root' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_square_root_positive_integer(self):
        """
        Prüft, ob 'square_root' eine positive Ganzzahl korrekt berechnet.
        """
        self.assertAlmostEqual(MathOperations.square_root(4), 2, msg="'square_root' soll eine positive Ganzzahl berechnen können. Überprüfe, ob die Funktion für einfache Wurzeln funktioniert.")

    def test_square_root_negative_integer(self):
        """
        Prüft, ob 'square_root' eine negative Ganzzahl korrekt berechnet.
        """
        self.assertAlmostEqual(MathOperations.square_root(-4), -2, msg="'square_root' soll eine negative Ganzzahl berechnen können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_square_root_zero(self):
        """
        Prüft, ob 'square_root' die Zahl '0' korrekt berechnet.
        """
        self.assertAlmostEqual(MathOperations.square_root(0), 0, msg="'square_root' soll mit der Zahl '0' umgehen können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_square_root_large_number(self):
        """
        Prüft, ob 'square_root' mit sehr großen Zahlen umgehen kann.
        """
        self.assertAlmostEqual(MathOperations.square_root(float('inf')), math.inf, msg="'square_root' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_square_root_invalid_type_string(self):
        """
        Prüft, ob 'square_root' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'square_root' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): MathOperations.square_root("a")

    def test_square_root_invalid_type_none(self):
        """
        Prüft, ob 'square_root' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'square_root' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): MathOperations.square_root(None)

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "MathOperations" Klasse existiert ❌
2. "squere_root" Funkton existiert ✅
3. Berechnet die Qadratwurzel einer positiven Ganzzahl ✅
4. Wirft einen ValueError für eine negativen Ganzzahl ❌
5. Berechnet die Quadarwurzel von einer Gleitkommazahl ❌
6. Berechnet die Qadratwurzel von 0 ✅
7. Berechnet die Qadratwurzel von einer sehr großen Zahl ✅
8. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
9. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:
- def test_square_root_negative_integer(self):

Bemerkungen:

Punkte: 6/9

Total: 12/27
'''


Test 4: 
1. ###
```
import unittest

class TestCalculateMeanFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_calculate_mean_with_positive_integers(self):
        """
        Prüft, ob 'calculate_mean' mit positiven Ganzzahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll positive Ganzzahlen korrekt berechnen. Überprüfe, ob der Code für einfache Mittelwerte funktioniert.")

    def test_calculate_mean_with_negative_integers(self):
        """
        Prüft, ob 'calculate_mean' mit negativen Ganzzahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([-1, -2, -3]), -2.0, "'calculate_mean' soll negative Ganzzahlen korrekt berechnen. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_calculate_mean_with_mixed_integers(self):
        """
        Prüft, ob 'calculate_mean' mit gemischten positiven und negativen Zahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([-1, 0, 1]), 0.0, "'calculate_mean' soll gemischte positive und negative Zahlen korrekt berechnen. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_calculate_mean_with_floats(self):
        """
        Prüft, ob 'calculate_mean' mit Kommazahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5, "'calculate_mean' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt berechnet werden.")

    def test_calculate_mean_with_zero(self):
        """
        Prüft, ob 'calculate_mean' die Zahl '0' korrekt berechnet.
        """
        self.assertEqual(calculate_mean([0]), 0.0, "'calculate_mean' soll mit '0' addieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_calculate_mean_with_empty_list(self):
        """
        Prüft, ob 'calculate_mean' eine leere Liste korrekt berechnet.
        """
        self.assertIsNone(calculate_mean([]), "'calculate_mean' soll für leere Listen 'None' zurückgeben. Überprüfe, ob die Eingaben korrekt validiert werden.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean(["a", 1])

    def test_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, None])

    def test_invalid_type_non_numeric(self):
        """
        Prüft, ob 'calculate_mean' bei nicht numerischen Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für nicht numerische Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, "a", 2])

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 8/10
'''

2. ###
```
import unittest

class TestCalculateMean(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_calculate_mean_empty_list(self):
        """
        Prüft, ob 'calculate_mean' eine leere Liste korrekt behandelt.
        """
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll eine leere Liste als ungültig erkennen. Überprüfe die Rückgabewerte.")

    def test_calculate_mean_single_element(self):
        """
        Prüft, ob 'calculate_mean' für Listen mit einem Element korrekt addiert.
        """
        self.assertEqual(calculate_mean([1]), 1, "'calculate_mean' soll eine Liste mit einem Element addieren können. Überprüfe die Typenkompatibilität.")

    def test_calculate_mean_two_positive_integers(self):
        """
        Prüft, ob 'calculate_mean' zwei positive Ganzzahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2]), 1.5, "'calculate_mean' soll zwei positive Ganzzahlen addieren können. Überprüfe die Typenkompatibilität.")

    def test_calculate_mean_two_negative_integers(self):
        """
        Prüft, ob 'calculate_mean' zwei negative Ganzzahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([-1, -2]), -1.5, "'calculate_mean' soll zwei negative Ganzzahlen addieren können. Überprüfe die Typenkompatibilität.")

    def test_calculate_mean_positive_and_negative_integer(self):
        """
        Prüft, ob 'calculate_mean' eine positive und eine negative Zahl korrekt addiert.
        """
        self.assertEqual(calculate_mean([-2, 3]), 0.5, "'calculate_mean' soll eine negative und eine positive Zahl addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_calculate_mean_two_floats(self):
        """
        Prüft, ob 'calculate_mean' zwei Kommazahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 2.5]), 2.0, "'calculate_mean' soll mit Kommazahlen umgehen können. Überprüfe die Typenkompatibilität.")

    def test_calculate_mean_float_and_integer(self):
        """
        Prüft, ob 'calculate_mean' eine Kommazahl und eine Ganzzahl korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 1]), 1.25, "'calculate_mean' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_calculate_mean_zero_and_integer(self):
        """
        Prüft, ob 'calculate_mean' die Zahl '0' korrekt addiert.
        """
        self.assertEqual(calculate_mean([0, 1]), 0.5, "'calculate_mean' soll mit '0' addieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_calculate_mean_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean(["a", 1])

    def test_calculate_mean_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 9/10
'''

3. ###
```
import unittest

class TestCalculateMeanFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_calculate_mean_empty_list(self):
        """
        Prüft, ob 'calculate_mean' eine leere Liste korrekt mit None zurückgibt.
        """
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll eine leere Liste mit None zurückgeben. Überprüfe den Code für leerer Listen.")

    def test_calculate_mean_single_value(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit einem Wert korrekt zurückgibt.
        """
        self.assertEqual(calculate_mean([5]), 5, "'calculate_mean' soll eine Liste mit einem Wert korrekt zurückgeben. Überprüfe den Code für Listen mit einzelnen Werten.")

    def test_calculate_mean_two_values(self):
        """
        Prüft, ob 'calculate_mean' zwei Zahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2]), 1.5, "'calculate_mean' soll zwei Zahlen korrekt addieren und den Mittelwert berechnen.")

    def test_calculate_mean_mixed_type(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit verschiedenen Typen korrekt behandelt.
        """
        self.assertEqual(calculate_mean([1, 2.5, -3]), -0.3333333333333333, "'calculate_mean' soll Listen mit verschiedenen Typen korrekt verarbeiten.")

    def test_calculate_mean_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean(["a", 1])

    def test_calculate_mean_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 6/10

Total: 23/30
'''


Test 5:
1. ###
```
import unittest

class TestIsLeapYearFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'is_leap_year' existiert.
        """
        self.assertTrue(callable(is_leap_year), "'is_leap_year' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_leap_years(self):
        """
        Prüft, ob 'is_leap_year' Jahre korrekt als Schaltjahre erkennt.
        """
        self.assertTrue(is_leap_year(2000), "'is_leap_year' soll Jahre als Schaltjahr erkennen können. Überprüfe die Logik für Schaltjahre.")
        self.assertTrue(is_leap_year(1992), "'is_leap_year' soll Jahre als Schaltjahr erkennen können. Überprüfe die Logik für Schaltjahre.")
        self.assertFalse(is_leap_year(1900), "'is_leap_year' soll Jahre als Schaltjahr erkennen können. Überprüfe die Logik für Schaltjahre.")

    def test_non_leap_years(self):
        """
        Prüft, ob 'is_leap_year' Jahre korrekt als Nicht-Schaltjahre erkennt.
        """
        self.assertFalse(is_leap_year(1999), "'is_leap_year' soll Jahre als Nicht-Schaltjahr erkennen können. Überprüfe die Logik für nicht-Schaltjahre.")
        self.assertFalse(is_leap_year(1700), "'is_leap_year' soll Jahre als Nicht-Schaltjahr erkennen können. Überprüfe die Logik für nicht-Schaltjahre.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'is_leap_year' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year("a")

    def test_invalid_type_none(self):
        """
        Prüft, ob 'is_leap_year' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year(None)

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "is_leap_year" Funkton existiert ✅
2. Mehrere Schaltjahre werden richtig als Schaltjahr erkannt ✅
3. Mehrere nicht Schaltjahre richtig als nicht Schaltjahre erkannt ✅
4. Ein Jahre das durch 100 aber nicht durch 400 teilbar ist wird richtig als nicht Schaltjahr erkannt ✅
5. Wirft einen Typfehler für nicht integer Eingaben (z.B. Gleitkommazahlen oder Strings) ✅
6. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:


Bemerkungen:
- 1900 Test ist zwar richtig als Falsch gekennzeichnet, aber der Kommentar und die Zuordnung ist falsch. 

Punkte: 6/6
'''

2. ###
```
import unittest

class TestLeapYearFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'is_leap_year' existiert.
        """
        self.assertTrue(callable(is_leap_year), "'is_leap_year' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_leap_year_2020(self):
        """
        Prüft, ob 2020 ein Schaltjahr ist.
        """
        self.assertTrue(is_leap_year(2020), "2020 sollte als Schaltjahr erkannt werden. Überprüfe die Implementierung der 'is_leap_year'-Funktion.")

    def test_non_leap_year_2019(self):
        """
        Prüft, ob 2019 kein Schaltjahr ist.
        """
        self.assertFalse(is_leap_year(2019), "2019 sollte nicht als Schaltjahr erkannt werden. Überprüfe die Implementierung der 'is_leap_year'-Funktion.")

    def test_leap_year_2000(self):
        """
        Prüft, ob 2000 ein Schaltjahr ist.
        """
        self.assertTrue(is_leap_year(2000), "2000 sollte als Schaltjahr erkannt werden. Überprüfe die Implementierung der 'is_leap_year'-Funktion.")

    def test_non_leap_year_2017(self):
        """
        Prüft, ob 2017 kein Schaltjahr ist.
        """
        self.assertFalse(is_leap_year(2017), "2017 sollte nicht als Schaltjahr erkannt werden. Überprüfe die Implementierung der 'is_leap_year'-Funktion.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'is_leap_year' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year("a")

    def test_invalid_type_none(self):
        """
        Prüft, ob 'is_leap_year' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year(None)

    def test_invalid_type_integer_zero(self):
        """
        Prüft, ob 'is_leap_year' bei Integer-Eingabe 0 einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für Integer-Eingabe 0 einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year(0)

    def test_invalid_type_integer_negative(self):
        """
        Prüft, ob 'is_leap_year' bei negativer Integer-Eingabe einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für negative Integer-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year(-1)

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "is_leap_year" Funkton existiert ✅
2. Mehrere Schaltjahre werden richtig als Schaltjahr erkannt ✅
3. Mehrere nicht Schaltjahre richtig als nicht Schaltjahre erkannt ✅
4. Ein Jahre das durch 100 aber nicht durch 400 teilbar ist wird richtig als nicht Schaltjahr erkannt ❌
5. Wirft einen Typfehler für nicht integer Eingaben (z.B. Gleitkommazahlen oder Strings) ✅
6. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle: 

Bemerkungen:

Punkte: 5/6
'''

3. ###
```
import unittest

class TestIsLeapYearFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'is_leap_year' existiert.
        """
        self.assertTrue(callable(is_leap_year), "'is_leap_year' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_is_leap_year_divisible_by_4(self):
        """
        Prüft, ob 'is_leap_year' eine Schaltjahreszahl korrekt erkennt.
        """
        self.assertTrue(is_leap_year(2020), "'is_leap_year' soll Schaltjahreszahlen korrekt erkennen. Überprüfe, ob die Funktionalität für einfache Fälle funktioniert.")

    def test_is_leap_year_divisible_by_100(self):
        """
        Prüft, ob 'is_leap_year' eine durch 100 teilbare Jahrzahl korrekt erkennt.
        """
        self.assertFalse(is_leap_year(1900), "'is_leap_year' soll keine durch 100 teilbaren Jahrzahlen als Schaltjahre erkennen. Überprüfe, ob die Funktionalität für spezielle Fälle funktioniert.")

    def test_is_leap_year_divisible_by_400(self):
        """
        Prüft, ob 'is_leap_year' eine durch 400 teilbare Jahrzahl korrekt erkennt.
        """
        self.assertTrue(is_leap_year(2000), "'is_leap_year' soll durch 400 teilbare Jahrzahlen als Schaltjahre erkennen. Überprüfe, ob die Funktionalität für spezielle Fälle funktioniert.")

    def test_is_leap_year_invalid_type(self):
        """
        Prüft, ob 'is_leap_year' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year("a")

    def test_is_leap_year_invalid_type_none(self):
        """
        Prüft, ob 'is_leap_year' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): is_leap_year(None)

if __name__ == "__main__":
    unittest.main()
```
###
'''
1. "is_leap_year" Funkton existiert ✅
2. Mehrere Schaltjahre werden richtig als Schaltjahr erkannt ✅
3. Mehrere nicht Schaltjahre richtig als nicht Schaltjahre erkannt ❌
4. Ein Jahre das durch 100 aber nicht durch 400 teilbar ist wird richtig als nicht Schaltjahr erkannt ✅
5. Wirft einen Typfehler für nicht integer Eingaben (z.B. Gleitkommazahlen oder Strings) ✅
6. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 5/6

Total: 16/18
'''




GPT-4o

Test 1:
1. ###
import unittest

class TestSubFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5, 3), 2, "'sub' soll zwei positive Ganzzahlen subtrahieren können. Überprüfe, ob die Berechnung korrekt ist.")

    def test_sub_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-5, -3), -2, "'sub' soll zwei negative Ganzzahlen subtrahieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_sub_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5, -3), 8, "'sub' soll eine positive und eine negative Zahl subtrahieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_sub_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5.5, 3.2), 2.3, "'sub' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt subtrahiert werden.")

    def test_sub_float_and_integer(self):
        """
        Prüft, ob 'sub' eine Kommazahl und eine Ganzzahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5.5, 3), 2.5, "'sub' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_sub_zero_and_integer(self):
        """
        Prüft, ob 'sub' die Zahl '0' korrekt subtrahiert.
        """
        self.assertEqual(sub(5, 0), 5, "'sub' soll mit '0' korrekt subtrahieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_sub_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(1e18, 1), 1e18 - 1, "'sub' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_sub_resulting_in_negative(self):
        """
        Prüft, ob 'sub' korrekt subtrahiert, wenn das Ergebnis negativ ist.
        """
        self.assertEqual(sub(3, 5), -2, "'sub' soll korrekt subtrahieren, auch wenn das Ergebnis negativ ist. Überprüfe die Berechnung.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            sub("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            sub(None, 1)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 10/10
'''
'''

2. ###
import unittest

class TestSubFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5, 3), 2, "'sub' soll zwei positive Ganzzahlen korrekt subtrahieren. Überprüfe die Implementierung.")

    def test_sub_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-5, -3), -2, "'sub' soll zwei negative Ganzzahlen korrekt subtrahieren. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_sub_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5, -3), 8, "'sub' soll eine positive und eine negative Zahl korrekt subtrahieren. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_sub_negative_and_positive_integer(self):
        """
        Prüft, ob 'sub' eine negative und eine positive Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(-5, 3), -8, "'sub' soll eine negative und eine positive Zahl korrekt subtrahieren können. Überprüfe die Implementierung.")

    def test_sub_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5.5, 3.2), 2.3, "'sub' soll zwei Kommazahlen korrekt subtrahieren. Überprüfe die Präzision der Fließkommazahlen.")

    def test_sub_float_and_integer(self):
        """
        Prüft, ob 'sub' eine Kommazahl und eine Ganzzahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5.5, 3), 2.5, "'sub' soll eine Kommazahl und eine Ganzzahl korrekt subtrahieren. Achte auf die Typenkompatibilität.")

    def test_sub_zero_and_integer(self):
        """
        Prüft, ob 'sub' die Zahl '0' korrekt subtrahiert.
        """
        self.assertEqual(sub(5, 0), 5, "'sub' soll korrekt mit '0' umgehen können. Überprüfe, ob der Code '0' korrekt behandelt.")

    def test_sub_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(1e15, 1e10), 999990000000000.0, "'sub' soll mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): 
            sub("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): 
            sub(1, None)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 10/10
'''

3. ###
import unittest

class TestSubFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_subtract_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5, 3), 2, "'sub' soll zwei positive Ganzzahlen korrekt subtrahieren. Überprüfe die Berechnungslogik.")

    def test_subtract_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-5, -3), -2, "'sub' soll zwei negative Ganzzahlen korrekt subtrahieren. Achte darauf, dass die Vorzeichen korrekt berücksichtigt werden.")

    def test_subtract_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5, -3), 8, "'sub' soll eine positive und eine negative Zahl korrekt subtrahieren. Überprüfe die Behandlung der Vorzeichen.")

    def test_subtract_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5.5, 3.2), 2.3, "'sub' soll zwei Kommazahlen korrekt subtrahieren. Achte auf die Genauigkeit der Berechnung.")

    def test_subtract_float_and_integer(self):
        """
        Prüft, ob 'sub' eine Kommazahl und eine Ganzzahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5.5, 2), 3.5, "'sub' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_subtract_zero_and_integer(self):
        """
        Prüft, ob 'sub' die Zahl '0' korrekt behandelt.
        """
        self.assertEqual(sub(5, 0), 5, "'sub' soll mit der Zahl '0' korrekt umgehen können. Vergewissere dich, dass keine Sonderfälle ausgelassen werden.")

    def test_subtract_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(1e10, 1e9), 9e9, "'sub' soll auch mit sehr großen Zahlen umgehen können. Überprüfe die Stabilität bei großen Werten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): 
            sub("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): 
            sub(1, None)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 10/10

Total: 30/30
'''


Test 2:
1. ###
import unittest

class TestMathFunctions(unittest.TestCase):

    def test_sub_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_typical_inputs(self):
        """
        Prüft, ob 'sub' typische Werte korrekt verarbeitet.
        """
        self.assertEqual(sub(5, 3), 2, "'sub' soll zwei positive Ganzzahlen korrekt subtrahieren.")
        self.assertEqual(sub(-3, -5), 2, "'sub' soll zwei negative Ganzzahlen korrekt subtrahieren.")
        self.assertEqual(sub(5, -3), 8, "'sub' soll eine positive und eine negative Zahl korrekt subtrahieren.")

    def test_sub_edge_cases(self):
        """
        Prüft, ob 'sub' Randfälle korrekt behandelt.
        """
        self.assertEqual(sub(0, 0), 0, "'sub' soll '0 - 0' korrekt berechnen.")
        self.assertEqual(sub(1.5, 0.5), 1.0, "'sub' soll Kommazahlen korrekt subtrahieren.")

    def test_sub_type_errors(self):
        """
        Prüft, ob 'sub' Typfehler korrekt auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll bei String-Eingaben einen Typfehler auslösen."):
            sub("a", 1)
        with self.assertRaises(TypeError, msg="'sub' soll bei 'None'-Eingaben einen Typfehler auslösen."):
            sub(None, 1)

    def test_mul_exists(self):
        """
        Prüft, ob die Funktion 'mul' existiert.
        """
        self.assertTrue(callable(mul), "'mul' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_mul_typical_inputs(self):
        """
        Prüft, ob 'mul' typische Werte korrekt verarbeitet.
        """
        self.assertEqual(mul(2, 3), 6, "'mul' soll zwei positive Ganzzahlen korrekt multiplizieren.")
        self.assertEqual(mul(-2, -3), 6, "'mul' soll zwei negative Ganzzahlen korrekt multiplizieren.")
        self.assertEqual(mul(2, -3), -6, "'mul' soll eine positive und eine negative Zahl korrekt multiplizieren.")

    def test_mul_edge_cases(self):
        """
        Prüft, ob 'mul' Randfälle korrekt behandelt.
        """
        self.assertEqual(mul(0, 100), 0, "'mul' soll '0' korrekt behandeln.")
        self.assertEqual(mul(1.5, 2), 3.0, "'mul' soll mit Kommazahlen korrekt multiplizieren.")

    def test_mul_type_errors(self):
        """
        Prüft, ob 'mul' Typfehler korrekt auslöst.
        """
        with self.assertRaises(TypeError, msg="'mul' soll bei String-Eingaben einen Typfehler auslösen."):
            mul("a", 1)
        with self.assertRaises(TypeError, msg="'mul' soll bei 'None'-Eingaben einen Typfehler auslösen."):
            mul(None, 1)

    def test_div_exists(self):
        """
        Prüft, ob die Funktion 'div' existiert.
        """
        self.assertTrue(callable(div), "'div' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_div_typical_inputs(self):
        """
        Prüft, ob 'div' typische Werte korrekt verarbeitet.
        """
        self.assertEqual(div(6, 3), 2.0, "'div' soll zwei positive Ganzzahlen korrekt dividieren.")
        self.assertEqual(div(-6, -3), 2.0, "'div' soll zwei negative Ganzzahlen korrekt dividieren.")
        self.assertEqual(div(6, -3), -2.0, "'div' soll eine positive und eine negative Zahl korrekt dividieren.")

    def test_div_edge_cases(self):
        """
        Prüft, ob 'div' Randfälle korrekt behandelt.
        """
        self.assertEqual(div(0, 1), 0.0, "'div' soll 0 korrekt behandeln, wenn es durch eine Zahl dividiert wird.")
        with self.assertRaises(ZeroDivisionError, msg="'div' soll bei Division durch 0 einen Fehler auslösen."):
            div(1, 0)

    def test_div_type_errors(self):
        """
        Prüft, ob 'div' Typfehler korrekt auslöst.
        """
        with self.assertRaises(TypeError, msg="'div' soll bei String-Eingaben einen Typfehler auslösen."):
            div("a", 1)
        with self.assertRaises(TypeError, msg="'div' soll bei 'None'-Eingaben einen Typfehler auslösen."):
            div(None, 1)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "mul" Funkton existiert ✅
2. Multipliziert zwei positive Ganzzahlen ✅
3. Multipliziert zwei negative Ganzzahlen ✅
4. Multipliziert eine positive und eine negative Ganzzahlen ✅
5. Multipliziert zwei Gleitkommazahlen ✅
6. Multipliziert eine Gleitkommazahl und eine Ganzzahl ❌
7. Multipliziert eine Ganzzahl mit 0 ✅
8. Multipliziert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "div" Funkton existiert ✅
2. Dividiert zwei positive Ganzzahlen ✅
3. Dividiert zwei negative Ganzzahlen ✅
4. Dividiert eine positive und eine negative Ganzzahlen ✅
5. Dividiert zwei Gleitkommazahlen ✅
6. Dividiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Wirft einen Error für Division mit 0 ✅
8. Dividiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 24/30
'''

2. ###
import unittest

class TestSubFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_sub_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5, 3), 2, "'sub' soll zwei positive Ganzzahlen korrekt subtrahieren. Überprüfe die Berechnung.")

    def test_sub_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-5, -3), -2, "'sub' soll zwei negative Ganzzahlen korrekt subtrahieren. Achte auf die Behandlung der Vorzeichen.")

    def test_sub_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5, -3), 8, "'sub' soll eine positive und eine negative Zahl korrekt subtrahieren. Überprüfe die Addition bei negativen Zahlen.")

    def test_sub_large_number(self):
        """
        Prüft, ob 'sub' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(sub(float('inf'), 1), float('inf'), "'sub' soll auch mit großen Zahlen umgehen können. Überprüfe, ob keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Verifiziere die Eingabevalidierung."):
            sub("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'sub' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe die Eingabevalidierung."):
            sub(1, None)

class TestMulFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'mul' existiert.
        """
        self.assertTrue(callable(mul), "'mul' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_mul_two_positive_integers(self):
        """
        Prüft, ob 'mul' zwei positive Ganzzahlen korrekt multipliziert.
        """
        self.assertEqual(mul(2, 3), 6, "'mul' soll zwei positive Ganzzahlen multiplizieren. Überprüfe die Berechnung.")

    def test_mul_negative_and_positive_integer(self):
        """
        Prüft, ob 'mul' eine negative und eine positive Zahl korrekt multipliziert.
        """
        self.assertEqual(mul(-2, 3), -6, "'mul' soll eine negative und eine positive Zahl multiplizieren können. Achte auf die Vorzeichen.")

    def test_mul_with_zero(self):
        """
        Prüft, ob 'mul' mit der Zahl '0' korrekt multipliziert.
        """
        self.assertEqual(mul(0, 5), 0, "'mul' soll '0' korrekt behandeln. Überprüfe, ob der Rückgabewert korrekt ist.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'mul' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'mul' soll für String-Eingaben einen Typfehler werfen. Verifiziere die Eingabevalidierung."):
            mul("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'mul' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'mul' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe die Eingabevalidierung."):
            mul(1, None)

class TestDivFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'div' existiert.
        """
        self.assertTrue(callable(div), "'div' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_div_two_positive_integers(self):
        """
        Prüft, ob 'div' zwei positive Ganzzahlen korrekt dividiert.
        """
        self.assertEqual(div(6, 3), 2, "'div' soll zwei positive Ganzzahlen korrekt dividieren. Überprüfe die Berechnung.")

    def test_div_by_zero(self):
        """
        Prüft, ob 'div' eine Division durch Null korrekt behandelt.
        """
        with self.assertRaises(ZeroDivisionError, msg="'div' soll bei Division durch Null einen Fehler werfen. Überprüfe die Ausnahmebehandlung."):
            div(5, 0)

    def test_invalid_type_string(self):
        """
        Prüft, ob 'div' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'div' soll für String-Eingaben einen Typfehler werfen. Verifiziere die Eingabevalidierung."):
            div("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'div' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'div' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe die Eingabevalidierung."):
            div(1, None)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ❌
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ❌
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Subtrahiert eine Ganzzahl mit 0 ❌
8. Subtrahiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "mul" Funkton existiert ✅
2. Multipliziert zwei positive Ganzzahlen ✅
3. Multipliziert zwei negative Ganzzahlen ✅
4. Multipliziert eine positive und eine negative Ganzzahlen ✅
5. Multipliziert zwei Gleitkommazahlen ❌
6. Multipliziert eine Gleitkommazahl und eine Ganzzahl ❌
7. Multipliziert eine Ganzzahl mit 0 ✅
8. Multipliziert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "div" Funkton existiert ✅
2. Dividiert zwei positive Ganzzahlen ✅
3. Dividiert zwei negative Ganzzahlen ❌
4. Dividiert eine positive und eine negative Ganzzahlen ❌
5. Dividiert zwei Gleitkommazahlen ❌
6. Dividiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Wirft einen Error für Division mit 0 ✅
8. Dividiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 18/30
'''

3. ###
import unittest

class TestSubFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'sub' existiert.
        """
        self.assertTrue(callable(sub), "'sub' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_subtract_two_positive_integers(self):
        """
        Prüft, ob 'sub' zwei positive Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(5, 3), 2, "'sub' soll zwei positive Ganzzahlen subtrahieren können. Überprüfe die Berechnung.")

    def test_subtract_two_negative_integers(self):
        """
        Prüft, ob 'sub' zwei negative Ganzzahlen korrekt subtrahiert.
        """
        self.assertEqual(sub(-5, -3), -2, "'sub' soll zwei negative Ganzzahlen subtrahieren können. Vergewissere dich, dass Vorzeichen korrekt behandelt werden.")

    def test_subtract_positive_and_negative_integer(self):
        """
        Prüft, ob 'sub' eine positive und eine negative Zahl korrekt subtrahiert.
        """
        self.assertEqual(sub(5, -3), 8, "'sub' soll eine positive und eine negative Zahl subtrahieren können. Achte auf korrekte Vorzeichenbehandlung.")

    def test_subtract_two_floats(self):
        """
        Prüft, ob 'sub' zwei Kommazahlen korrekt subtrahiert.
        """
        self.assertAlmostEqual(sub(5.5, 2.5), 3.0, places=2, msg="'sub' soll mit Kommazahlen umgehen können. Überprüfe die Fließkommaarithmetik.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'sub' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'sub' soll für String-Eingaben einen Typfehler werfen. Überprüfe die Eingabevalidierung."):
            sub("a", 1)

class TestMulFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'mul' existiert.
        """
        self.assertTrue(callable(mul), "'mul' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_multiply_two_positive_integers(self):
        """
        Prüft, ob 'mul' zwei positive Ganzzahlen korrekt multipliziert.
        """
        self.assertEqual(mul(3, 4), 12, "'mul' soll zwei positive Ganzzahlen multiplizieren können. Überprüfe die Berechnung.")

    def test_multiply_two_negative_integers(self):
        """
        Prüft, ob 'mul' zwei negative Ganzzahlen korrekt multipliziert.
        """
        self.assertEqual(mul(-3, -4), 12, "'mul' soll zwei negative Ganzzahlen multiplizieren können. Achte auf korrektes Vorzeichenhandling.")

    def test_multiply_positive_and_negative_integer(self):
        """
        Prüft, ob 'mul' eine positive und eine negative Zahl korrekt multipliziert.
        """
        self.assertEqual(mul(3, -4), -12, "'mul' soll eine positive und eine negative Zahl multiplizieren können. Überprüfe die Vorzeichen.")

    def test_multiply_with_zero(self):
        """
        Prüft, ob 'mul' mit der Zahl '0' korrekt umgeht.
        """
        self.assertEqual(mul(0, 5), 0, "'mul' soll mit '0' multiplizieren können. Überprüfe die Nullbehandlung.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'mul' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'mul' soll für String-Eingaben einen Typfehler werfen. Überprüfe die Eingabevalidierung."):
            mul("a", 1)

class TestDivFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'div' existiert.
        """
        self.assertTrue(callable(div), "'div' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_divide_two_positive_integers(self):
        """
        Prüft, ob 'div' zwei positive Ganzzahlen korrekt dividiert.
        """
        self.assertEqual(div(8, 4), 2, "'div' soll zwei positive Ganzzahlen dividieren können. Überprüfe die Berechnung.")

    def test_divide_two_negative_integers(self):
        """
        Prüft, ob 'div' zwei negative Ganzzahlen korrekt dividiert.
        """
        self.assertEqual(div(-8, -4), 2, "'div' soll zwei negative Ganzzahlen dividieren können. Achte auf korrektes Vorzeichenhandling.")

    def test_divide_positive_and_negative
###
'''
1. "sub" Funkton existiert ✅
2. Subtrahiert zwei positive Ganzzahlen ✅
3. Subtrahiert zwei negative Ganzzahlen ✅
4. Subtrahiert eine positive und eine negative Ganzzahlen ✅
5. Subtrahiert zwei Gleitkommazahlen ✅
6. Subtrahiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Subtrahiert eine Ganzzahl mit 0 ✅
8. Subtrahiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "mul" Funkton existiert ✅
2. Multipliziert zwei positive Ganzzahlen ✅
3. Multipliziert zwei negative Ganzzahlen ✅
4. Multipliziert eine positive und eine negative Ganzzahlen ✅
5. Multipliziert zwei Gleitkommazahlen ❌
6. Multipliziert eine Gleitkommazahl und eine Ganzzahl ❌
7. Multipliziert eine Ganzzahl mit 0 ✅
8. Multipliziert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

1. "div" Funkton existiert ✅
2. Dividiert zwei positive Ganzzahlen ✅
3. Dividiert zwei negative Ganzzahlen ✅
4. Dividiert eine positive und eine negative Ganzzahlen ❌
5. Dividiert zwei Gleitkommazahlen ❌
6. Dividiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Wirft einen Error für Division mit 0 ❌
8. Dividiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 24/30

Total: 66/90
'''


Test 3:
1. ###
import unittest
import math

class TestMathOperations(unittest.TestCase):

    def test_class_exists(self):
        """
        Prüft, ob die Klasse 'MathOperations' existiert.
        """
        self.assertTrue('MathOperations' in globals(), "'MathOperations' soll existieren. Vergewissere dich, dass die Klasse definiert ist.")

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'square_root' existiert.
        """
        self.assertTrue(hasattr(MathOperations, 'square_root') and callable(getattr(MathOperations, 'square_root')),
                        "'square_root' soll existieren. Vergewissere dich, dass die Funktion in der Klasse 'MathOperations' definiert ist.")

    def test_square_root_positive_integer(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel einer positiven Ganzzahl korrekt berechnet.
        """
        self.assertEqual(MathOperations.square_root(4), 2, 
                         "'square_root' soll die Quadratwurzel einer positiven Ganzzahl berechnen. Überprüfe den Algorithmus.")

    def test_square_root_positive_float(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel einer positiven Kommazahl korrekt berechnet.
        """
        self.assertEqual(MathOperations.square_root(2.25), 1.5, 
                         "'square_root' soll die Quadratwurzel einer positiven Kommazahl berechnen. Vergewissere dich, dass Fließkommazahlen korrekt verarbeitet werden.")

    def test_square_root_zero(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel von 0 korrekt berechnet.
        """
        self.assertEqual(MathOperations.square_root(0), 0, 
                         "'square_root' soll die Quadratwurzel von 0 berechnen. Stelle sicher, dass der Code für diesen Randfall funktioniert.")

    def test_square_root_negative_number(self):
        """
        Prüft, ob 'square_root' bei negativen Zahlen einen Fehler auslöst.
        """
        with self.assertRaises(ValueError, msg="'square_root' soll bei negativen Zahlen einen Fehler werfen. Überprüfe die Eingabevalidierung."):
            MathOperations.square_root(-1)

    def test_square_root_large_number(self):
        """
        Prüft, ob 'square_root' mit sehr großen Zahlen umgehen kann.
        """
        self.assertAlmostEqual(MathOperations.square_root(1e10), 1e5, 
                               "'square_root' soll auch mit sehr großen Zahlen umgehen können. Überprüfe die Genauigkeit für große Eingabewerte.")

    def test_square_root_non_numeric_input(self):
        """
        Prüft, ob 'square_root' bei nicht-numerischen Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'square_root' soll für nicht-numerische Eingaben einen Typfehler werfen. Stelle sicher, dass die Eingaben geprüft werden."):
            MathOperations.square_root("abc")

    def test_square_root_none_input(self):
        """
        Prüft, ob 'square_root' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'square_root' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe die Eingabevalidierung."):
            MathOperations.square_root(None)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "MathOperations" Klasse existiert ✅
2. "squere_root" Funkton existiert ✅
3. Berechnet die Qadratwurzel einer positiven Ganzzahl ✅
4. Wirft einen ValueError für eine negativen Ganzzahl ✅
5. Berechnet die Quadarwurzel von einer Gleitkommazahl ✅
6. Berechnet die Qadratwurzel von 0 ✅
7. Berechnet die Qadratwurzel von einer sehr großen Zahl ✅
8. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
9. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 9/9
'''

2. ###
import unittest
from math_operations import MathOperations

class TestMathOperations(unittest.TestCase):

    def test_class_exists(self):
        """
        Prüft, ob die Klasse 'MathOperations' existiert.
        """
        self.assertTrue(hasattr(MathOperations, 'square_root'), 
                        "'MathOperations' soll die Methode 'square_root' enthalten. Überprüfe die Definition.")

    def test_square_root_exists(self):
        """
        Prüft, ob die Methode 'square_root' existiert.
        """
        self.assertTrue(callable(getattr(MathOperations, 'square_root', None)), 
                        "'square_root' soll als Methode existieren. Stelle sicher, dass die Methode definiert ist.")

    def test_square_root_positive_number(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel einer positiven Zahl korrekt berechnet.
        """
        self.assertEqual(MathOperations.square_root(4), 2.0, 
                         "'square_root' soll die Quadratwurzel einer positiven Zahl berechnen. Überprüfe, ob die Berechnung korrekt ist.")

    def test_square_root_zero(self):
        """
        Prüft, ob 'square_root' für die Eingabe '0' korrekt funktioniert.
        """
        self.assertEqual(MathOperations.square_root(0), 0.0, 
                         "'square_root' soll die Quadratwurzel von '0' als '0.0' zurückgeben. Stelle sicher, dass diese Eingabe behandelt wird.")

    def test_square_root_large_number(self):
        """
        Prüft, ob 'square_root' mit großen Zahlen korrekt funktioniert.
        """
        self.assertEqual(MathOperations.square_root(1e6), 1000.0, 
                         "'square_root' soll mit großen Zahlen korrekt umgehen können. Überprüfe die Berechnung für solche Eingaben.")

    def test_square_root_negative_number(self):
        """
        Prüft, ob 'square_root' bei einer negativen Eingabe einen Wertfehler auslöst.
        """
        with self.assertRaises(ValueError, 
                               msg="'square_root' soll bei negativen Eingaben einen Wertfehler auslösen. Stelle sicher, dass negative Zahlen korrekt behandelt werden."):
            MathOperations.square_root(-4)

    def test_square_root_float_input(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel einer Kommazahl korrekt berechnet.
        """
        self.assertAlmostEqual(MathOperations.square_root(2.25), 1.5, 
                               "'square_root' soll die Quadratwurzel einer Kommazahl korrekt berechnen. Überprüfe die Genauigkeit bei solchen Eingaben.")

    def test_square_root_invalid_type_string(self):
        """
        Prüft, ob 'square_root' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, 
                               msg="'square_root' soll für String-Eingaben einen Typfehler werfen. Überprüfe die Typvalidierung."):
            MathOperations.square_root("a")

    def test_square_root_invalid_type_none(self):
        """
        Prüft, ob 'square_root' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, 
                               msg="'square_root' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe die Typvalidierung."):
            MathOperations.square_root(None)

    def test_square_root_invalid_type_list(self):
        """
        Prüft, ob 'square_root' bei Listen-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, 
                               msg="'square_root' soll für Listen-Eingaben einen Typfehler werfen. Überprüfe die Typvalidierung."):
            MathOperations.square_root([4])

if __name__ == "__main__":
    unittest.main()
###
'''
1. "MathOperations" Klasse existiert ✅
2. "squere_root" Funkton existiert ✅
3. Berechnet die Qadratwurzel einer positiven Ganzzahl ✅
4. Wirft einen ValueError für eine negativen Ganzzahl ✅
5. Berechnet die Quadarwurzel von einer Gleitkommazahl ✅
6. Berechnet die Qadratwurzel von 0 ✅
7. Berechnet die Qadratwurzel von einer sehr großen Zahl ✅
8. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
9. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 9/9
'''

3. ###
import unittest
import math

class TestMathOperations(unittest.TestCase):

    def test_class_exists(self):
        """
        Prüft, ob die Klasse 'MathOperations' existiert.
        """
        self.assertTrue('MathOperations' in globals(), "'MathOperations' soll existieren. Vergewissere dich, dass die Klasse definiert ist.")

    def test_square_root_function_exists(self):
        """
        Prüft, ob die Funktion 'square_root' existiert.
        """
        self.assertTrue(hasattr(MathOperations, 'square_root') and callable(getattr(MathOperations, 'square_root')), 
                        "'square_root' soll in der Klasse 'MathOperations' existieren. Vergewissere dich, dass die Methode definiert ist.")

    def test_square_root_positive_integer(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel einer positiven Ganzzahl korrekt berechnet.
        """
        self.assertEqual(MathOperations.square_root(16), 4.0, 
                         "'square_root' soll die Quadratwurzel einer positiven Ganzzahl berechnen. Überprüfe, ob der Algorithmus korrekt ist.")

    def test_square_root_positive_float(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel einer positiven Fließkommazahl korrekt berechnet.
        """
        self.assertAlmostEqual(MathOperations.square_root(2.25), 1.5, 
                               "'square_root' soll die Quadratwurzel einer positiven Fließkommazahl berechnen. Stelle sicher, dass Fließkommazahlen korrekt behandelt werden.")

    def test_square_root_zero(self):
        """
        Prüft, ob 'square_root' die Quadratwurzel von 0 korrekt berechnet.
        """
        self.assertEqual(MathOperations.square_root(0), 0.0, 
                         "'square_root' soll die Quadratwurzel von 0 korrekt berechnen. Vergewissere dich, dass der Sonderfall '0' richtig behandelt wird.")

    def test_square_root_negative_input(self):
        """
        Prüft, ob 'square_root' bei einer negativen Eingabe einen Wertfehler auslöst.
        """
        with self.assertRaises(ValueError, msg="'square_root' soll bei einer negativen Eingabe einen 'ValueError' werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            MathOperations.square_root(-4)

    def test_square_root_large_number(self):
        """
        Prüft, ob 'square_root' mit sehr großen Zahlen korrekt umgeht.
        """
        self.assertAlmostEqual(MathOperations.square_root(1e10), 1e5, 
                               "'square_root' soll mit sehr großen Zahlen korrekt arbeiten. Überprüfe die Berechnung bei extremen Eingabewerten.")

    def test_square_root_invalid_type_string(self):
        """
        Prüft, ob 'square_root' bei einer String-Eingabe einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'square_root' soll bei einer String-Eingabe einen Typfehler werfen. Vergewissere dich, dass der Eingabetyp überprüft wird."):
            MathOperations.square_root("16")

    def test_square_root_invalid_type_none(self):
        """
        Prüft, ob 'square_root' bei einer 'None'-Eingabe einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'square_root' soll bei einer 'None'-Eingabe einen Typfehler werfen. Überprüfe, ob der Eingabetyp überprüft wird."):
            MathOperations.square_root(None)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "MathOperations" Klasse existiert ✅
2. "squere_root" Funkton existiert ✅
3. Berechnet die Qadratwurzel einer positiven Ganzzahl ✅
4. Wirft einen ValueError für eine negativen Ganzzahl ✅
5. Berechnet die Quadarwurzel von einer Gleitkommazahl ✅
6. Berechnet die Qadratwurzel von 0 ✅
7. Berechnet die Qadratwurzel von einer sehr großen Zahl ✅
8. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
9. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 9/9

Total: 27/27
'''

Test 4:
1. ###
import unittest

class TestCalculateMean(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_mean_of_integers(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt einer Liste von Ganzzahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0, "'calculate_mean' soll den Durchschnitt von Ganzzahlen korrekt berechnen.")

    def test_mean_of_floats(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt einer Liste von Kommazahlen korrekt berechnet.
        """
        self.assertAlmostEqual(calculate_mean([1.2, 3.4, 5.6]), 3.4, "'calculate_mean' soll den Durchschnitt von Kommazahlen korrekt berechnen.")

    def test_mean_of_mixed_types(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt einer Liste von Ganzzahlen und Kommazahlen korrekt berechnet.
        """
        self.assertAlmostEqual(calculate_mean([1, 2.5, 3]), 2.1666666666666665, "'calculate_mean' soll den Durchschnitt von gemischten Typen korrekt berechnen.")

    def test_empty_list(self):
        """
        Prüft, ob 'calculate_mean' bei einer leeren Liste 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([]), "'calculate_mean' soll bei einer leeren Liste 'None' zurückgeben.")

    def test_list_with_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei einer Liste mit einem String 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([1, "a", 3]), "'calculate_mean' soll 'None' zurückgeben, wenn die Liste nicht-numerische Werte enthält.")

    def test_list_with_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei einer Liste mit 'None' 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([1, None, 3]), "'calculate_mean' soll 'None' zurückgeben, wenn die Liste nicht-numerische Werte enthält.")

    def test_single_integer(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt für eine Liste mit nur einer Ganzzahl korrekt berechnet.
        """
        self.assertEqual(calculate_mean([5]), 5.0, "'calculate_mean' soll den Durchschnitt für eine Liste mit einem Element korrekt berechnen.")

    def test_single_float(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt für eine Liste mit nur einer Kommazahl korrekt berechnet.
        """
        self.assertEqual(calculate_mean([2.5]), 2.5, "'calculate_mean' soll den Durchschnitt für eine Liste mit einem Element korrekt berechnen.")

    def test_large_numbers(self):
        """
        Prüft, ob 'calculate_mean' mit sehr großen Zahlen umgehen kann.
        """
        self.assertAlmostEqual(calculate_mean([1e10, 1e10, 1e10]), 1e10, "'calculate_mean' soll mit sehr großen Zahlen korrekt umgehen.")

    def test_invalid_input_not_list(self):
        """
        Prüft, ob 'calculate_mean' bei nicht-listenförmigen Eingaben 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean(123), "'calculate_mean' soll 'None' zurückgeben, wenn die Eingabe kein Listentyp ist.")
        self.assertIsNone(calculate_mean("123"), "'calculate_mean' soll 'None' zurückgeben, wenn die Eingabe kein Listentyp ist.")

if __name__ == "__main__":
    unittest.main()
###
```
###
'''
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ✅
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 7/10
'''

2. ###
import unittest

class TestCalculateMean(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_mean_of_integers(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt einer Liste von Ganzzahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2, 3]), 2, "'calculate_mean' soll den Durchschnitt einer Liste von Ganzzahlen korrekt berechnen.")

    def test_mean_of_floats(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt einer Liste von Kommazahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5, "'calculate_mean' soll den Durchschnitt einer Liste von Kommazahlen korrekt berechnen.")

    def test_mean_of_mixed_numbers(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt einer Liste von Ganzzahlen und Kommazahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2.5, 3]), 2.1666666666666665, "'calculate_mean' soll den Durchschnitt einer gemischten Liste aus Ganzzahlen und Kommazahlen korrekt berechnen.")

    def test_empty_list(self):
        """
        Prüft, ob 'calculate_mean' bei einer leeren Liste 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([]), "'calculate_mean' soll bei einer leeren Liste 'None' zurückgeben. Überprüfe, ob die Länge der Liste geprüft wird.")

    def test_invalid_type_in_list_string(self):
        """
        Prüft, ob 'calculate_mean' bei einer Liste mit Strings 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([1, "a", 3]), "'calculate_mean' soll bei einer Liste mit Strings 'None' zurückgeben. Überprüfe, ob alle Elemente auf Zahlen geprüft werden.")

    def test_invalid_type_in_list_none(self):
        """
        Prüft, ob 'calculate_mean' bei einer Liste mit 'None' 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([1, None, 3]), "'calculate_mean' soll bei einer Liste mit 'None' 'None' zurückgeben. Stelle sicher, dass ungültige Typen korrekt behandelt werden.")

    def test_mean_with_large_numbers(self):
        """
        Prüft, ob 'calculate_mean' mit sehr großen Zahlen umgehen kann.
        """
        self.assertEqual(calculate_mean([1e10, 2e10, 3e10]), 2e10, "'calculate_mean' soll mit sehr großen Zahlen umgehen können.")

    def test_mean_with_negative_numbers(self):
        """
        Prüft, ob 'calculate_mean' mit negativen Zahlen korrekt umgeht.
        """
        self.assertEqual(calculate_mean([-1, -2, -3]), -2, "'calculate_mean' soll mit negativen Zahlen korrekt umgehen.")

    def test_mean_with_zero(self):
        """
        Prüft, ob 'calculate_mean' den Durchschnitt korrekt berechnet, wenn '0' in der Liste enthalten ist.
        """
        self.assertEqual(calculate_mean([0, 2, 4]), 2, "'calculate_mean' soll den Durchschnitt korrekt berechnen, wenn '0' in der Liste enthalten ist.")

if __name__ == "__main__":
    unittest.main()
###
'''
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ✅
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 8/10
'''

3. ###
import unittest

class TestCalculateMeanFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), 
                        "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_mean_of_integers(self):
        """
        Prüft, ob 'calculate_mean' den Mittelwert einer Liste von Ganzzahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2, 3, 4]), 2.5, 
                         "'calculate_mean' soll den Mittelwert einer Liste von Ganzzahlen korrekt berechnen.")

    def test_mean_of_floats(self):
        """
        Prüft, ob 'calculate_mean' den Mittelwert einer Liste von Kommazahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1.1, 2.2, 3.3, 4.4]), 2.75, 
                         "'calculate_mean' soll den Mittelwert einer Liste von Kommazahlen korrekt berechnen.")

    def test_mean_of_mixed_numbers(self):
        """
        Prüft, ob 'calculate_mean' den Mittelwert einer Liste mit Ganzzahlen und Kommazahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2.2, 3, 4.4]), 2.65, 
                         "'calculate_mean' soll den Mittelwert einer Liste mit Ganzzahlen und Kommazahlen korrekt berechnen.")

    def test_mean_of_empty_list(self):
        """
        Prüft, ob 'calculate_mean' bei einer leeren Liste 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([]), 
                          "'calculate_mean' soll bei einer leeren Liste 'None' zurückgeben.")

    def test_mean_with_invalid_element_string(self):
        """
        Prüft, ob 'calculate_mean' bei einem String in der Liste 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([1, "a", 3]), 
                          "'calculate_mean' soll bei ungültigen Elementen wie Strings in der Liste 'None' zurückgeben.")

    def test_mean_with_invalid_element_none(self):
        """
        Prüft, ob 'calculate_mean' bei einem 'None'-Element in der Liste 'None' zurückgibt.
        """
        self.assertIsNone(calculate_mean([1, None, 3]), 
                          "'calculate_mean' soll bei ungültigen Elementen wie 'None' in der Liste 'None' zurückgeben.")

    def test_mean_with_large_numbers(self):
        """
        Prüft, ob 'calculate_mean' mit sehr großen Zahlen korrekt umgeht.
        """
        self.assertEqual(calculate_mean([1e10, 2e10, 3e10]), 2e10, 
                         "'calculate_mean' soll mit sehr großen Zahlen korrekt umgehen.")

    def test_mean_with_single_element(self):
        """
        Prüft, ob 'calculate_mean' den Mittelwert einer Liste mit einem Element korrekt berechnet.
        """
        self.assertEqual(calculate_mean([5]), 5, 
                         "'calculate_mean' soll den Mittelwert einer Liste mit einem Element korrekt berechnen.")

    def test_mean_with_negative_numbers(self):
        """
        Prüft, ob 'calculate_mean' den Mittelwert einer Liste mit negativen Zahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([-1, -2, -3, -4]), -2.5, 
                         "'calculate_mean' soll den Mittelwert einer Liste mit negativen Zahlen korrekt berechnen.")

    def test_mean_with_all_zeros(self):
        """
        Prüft, ob 'calculate_mean' den Mittelwert einer Liste mit Nullen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([0, 0, 0]), 0, 
                         "'calculate_mean' soll den Mittelwert einer Liste mit Nullen korrekt berechnen.")

if __name__ == "__main__":
    unittest.main()
###
'''
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ✅
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle:

Bemerkungen:

Punkte: 8/10

Total: 23/30
'''


Test 5:
1. ###
import unittest

class TestIsLeapYearFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'is_leap_year' existiert.
        """
        self.assertTrue(callable(is_leap_year), "'is_leap_year' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_typical_leap_year(self):
        """
        Prüft, ob ein typisches Schaltjahr korrekt erkannt wird.
        """
        self.assertTrue(is_leap_year(2024), "'is_leap_year' soll erkennen, dass 2024 ein Schaltjahr ist. Überprüfe die Bedingung für durch 4 teilbare Jahre.")

    def test_typical_non_leap_year(self):
        """
        Prüft, ob ein typisches Nicht-Schaltjahr korrekt erkannt wird.
        """
        self.assertFalse(is_leap_year(2023), "'is_leap_year' soll erkennen, dass 2023 kein Schaltjahr ist. Überprüfe die Bedingung für nicht durch 4 teilbare Jahre.")

    def test_century_non_leap_year(self):
        """
        Prüft, ob ein Jahrhundertjahr, das kein Schaltjahr ist, korrekt erkannt wird.
        """
        self.assertFalse(is_leap_year(1900), "'is_leap_year' soll erkennen, dass 1900 kein Schaltjahr ist. Stelle sicher, dass die Bedingung für durch 100 teilbare Jahre ohne durch 400 teilbar erfüllt ist.")

    def test_century_leap_year(self):
        """
        Prüft, ob ein Jahrhundertjahr, das ein Schaltjahr ist, korrekt erkannt wird.
        """
        self.assertTrue(is_leap_year(2000), "'is_leap_year' soll erkennen, dass 2000 ein Schaltjahr ist. Überprüfe die Bedingung für durch 400 teilbare Jahre.")

    def test_edge_case_year_0(self):
        """
        Prüft, ob das Jahr 0 korrekt als Schaltjahr erkannt wird.
        """
        self.assertTrue(is_leap_year(0), "'is_leap_year' soll erkennen, dass das Jahr 0 ein Schaltjahr ist. Überprüfe, ob die Funktion für sehr kleine Zahlen korrekt funktioniert.")

    def test_negative_leap_year(self):
        """
        Prüft, ob ein negatives Jahr korrekt als Schaltjahr erkannt wird.
        """
        self.assertTrue(is_leap_year(-4), "'is_leap_year' soll erkennen, dass -4 ein Schaltjahr ist. Vergewissere dich, dass negative Eingaben korrekt verarbeitet werden.")

    def test_negative_non_leap_year(self):
        """
        Prüft, ob ein negatives Jahr korrekt als Nicht-Schaltjahr erkannt wird.
        """
        self.assertFalse(is_leap_year(-1), "'is_leap_year' soll erkennen, dass -1 kein Schaltjahr ist. Überprüfe die Logik für negative Zahlen.")

    def test_invalid_type_string(self):
        """
        Prüft, ob bei String-Eingaben ein Typfehler ausgelöst wird.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year("2024")

    def test_invalid_type_none(self):
        """
        Prüft, ob bei 'None'-Eingaben ein Typfehler ausgelöst wird.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year(None)

    def test_invalid_type_float(self):
        """
        Prüft, ob bei Fließkomma-Eingaben ein Typfehler ausgelöst wird.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für Fließkomma-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year(2024.0)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "is_leap_year" Funkton existiert ✅
2. Mehrere Schaltjahre werden richtig als Schaltjahr erkannt ✅
3. Mehrere nicht Schaltjahre richtig als nicht Schaltjahre erkannt ✅
4. Ein Jahre das durch 100 aber nicht durch 400 teilbar ist wird richtig als nicht Schaltjahr erkannt ✅
5. Wirft einen Typfehler für nicht integer Eingaben (z.B. Gleitkommazahlen oder Strings) ✅
6. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle: 

Bemerkungen:

Punkte: 6/6
'''

2. ###
import unittest

class TestIsLeapYearFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'is_leap_year' existiert.
        """
        self.assertTrue(callable(is_leap_year), "'is_leap_year' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_typical_leap_year(self):
        """
        Prüft, ob typische Schaltjahre korrekt erkannt werden.
        """
        self.assertTrue(is_leap_year(2024), "'is_leap_year' soll erkennen, dass 2024 ein Schaltjahr ist.")

    def test_typical_non_leap_year(self):
        """
        Prüft, ob typische Nicht-Schaltjahre korrekt erkannt werden.
        """
        self.assertFalse(is_leap_year(2023), "'is_leap_year' soll erkennen, dass 2023 kein Schaltjahr ist.")

    def test_century_non_leap_year(self):
        """
        Prüft, ob Jahrhunderte, die keine Schaltjahre sind, korrekt erkannt werden.
        """
        self.assertFalse(is_leap_year(1900), "'is_leap_year' soll erkennen, dass 1900 kein Schaltjahr ist.")

    def test_century_leap_year(self):
        """
        Prüft, ob Jahrhunderte, die Schaltjahre sind, korrekt erkannt werden.
        """
        self.assertTrue(is_leap_year(2000), "'is_leap_year' soll erkennen, dass 2000 ein Schaltjahr ist.")

    def test_edge_case_min_year(self):
        """
        Prüft, ob der kleinste mögliche Jahreswert korrekt behandelt wird.
        """
        self.assertFalse(is_leap_year(1), "'is_leap_year' soll erkennen, dass 1 kein Schaltjahr ist.")

    def test_edge_case_zero_year(self):
        """
        Prüft, ob das Jahr 0 korrekt als Schaltjahr behandelt wird.
        """
        self.assertTrue(is_leap_year(0), "'is_leap_year' soll erkennen, dass 0 ein Schaltjahr ist.")

    def test_edge_case_large_year(self):
        """
        Prüft, ob sehr große Jahreswerte korrekt verarbeitet werden.
        """
        self.assertTrue(is_leap_year(4000000), "'is_leap_year' soll erkennen, dass 4000000 ein Schaltjahr ist.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'is_leap_year' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year("2024")

    def test_invalid_type_float(self):
        """
        Prüft, ob 'is_leap_year' bei Fließkommazahlen einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für Fließkommazahlen einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year(2024.0)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'is_leap_year' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year(None)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "is_leap_year" Funkton existiert ✅
2. Mehrere Schaltjahre werden richtig als Schaltjahr erkannt ✅
3. Mehrere nicht Schaltjahre richtig als nicht Schaltjahre erkannt ✅
4. Ein Jahre das durch 100 aber nicht durch 400 teilbar ist wird richtig als nicht Schaltjahr erkannt ✅
5. Wirft einen Typfehler für nicht integer Eingaben (z.B. Gleitkommazahlen oder Strings) ✅
6. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle: 

Bemerkungen:

Punkte: 6/6
'''

3. ###
import unittest

class TestIsLeapYearFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'is_leap_year' existiert.
        """
        self.assertTrue(callable(is_leap_year), "'is_leap_year' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_typical_leap_year(self):
        """
        Prüft, ob 'is_leap_year' ein typisches Schaltjahr korrekt identifiziert.
        """
        self.assertTrue(is_leap_year(2024), "'is_leap_year' soll 2024 als Schaltjahr identifizieren. Überprüfe die Logik für Jahre, die durch 4 teilbar sind.")

    def test_typical_non_leap_year(self):
        """
        Prüft, ob 'is_leap_year' ein typisches Nicht-Schaltjahr korrekt identifiziert.
        """
        self.assertFalse(is_leap_year(2023), "'is_leap_year' soll 2023 als Nicht-Schaltjahr identifizieren. Überprüfe die Logik für Jahre, die nicht durch 4 teilbar sind.")

    def test_century_non_leap_year(self):
        """
        Prüft, ob 'is_leap_year' ein Jahrhundertjahr, das kein Schaltjahr ist, korrekt erkennt.
        """
        self.assertFalse(is_leap_year(1900), "'is_leap_year' soll 1900 als Nicht-Schaltjahr identifizieren. Überprüfe die Logik für Jahre, die durch 100, aber nicht durch 400 teilbar sind.")

    def test_century_leap_year(self):
        """
        Prüft, ob 'is_leap_year' ein Jahrhundertjahr, das ein Schaltjahr ist, korrekt erkennt.
        """
        self.assertTrue(is_leap_year(2000), "'is_leap_year' soll 2000 als Schaltjahr identifizieren. Überprüfe die Logik für Jahre, die durch 400 teilbar sind.")

    def test_negative_year(self):
        """
        Prüft, ob 'is_leap_year' für ein negatives Jahr korrekt funktioniert.
        """
        self.assertFalse(is_leap_year(-1), "'is_leap_year' soll für das Jahr -1 korrekt arbeiten. Überprüfe die Handhabung negativer Eingaben.")

    def test_year_zero(self):
        """
        Prüft, ob 'is_leap_year' für das Jahr 0 korrekt funktioniert.
        """
        self.assertTrue(is_leap_year(0), "'is_leap_year' soll das Jahr 0 als Schaltjahr identifizieren. Überprüfe die Logik für spezielle Fälle.")

    def test_large_leap_year(self):
        """
        Prüft, ob 'is_leap_year' für eine große Schaltjahr-Zahl korrekt funktioniert.
        """
        self.assertTrue(is_leap_year(2400), "'is_leap_year' soll 2400 als Schaltjahr identifizieren. Überprüfe die Logik für große Zahlen.")

    def test_large_non_leap_year(self):
        """
        Prüft, ob 'is_leap_year' für eine große Nicht-Schaltjahr-Zahl korrekt funktioniert.
        """
        self.assertFalse(is_leap_year(2300), "'is_leap_year' soll 2300 als Nicht-Schaltjahr identifizieren. Überprüfe die Logik für große Zahlen.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'is_leap_year' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year("2024")

    def test_invalid_type_none(self):
        """
        Prüft, ob 'is_leap_year' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year(None)

    def test_invalid_type_float(self):
        """
        Prüft, ob 'is_leap_year' bei Fließkommazahlen einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'is_leap_year' soll für Fließkommazahlen einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."):
            is_leap_year(2024.5)

if __name__ == "__main__":
    unittest.main()
###
'''
1. "is_leap_year" Funkton existiert ✅
2. Mehrere Schaltjahre werden richtig als Schaltjahr erkannt ✅
3. Mehrere nicht Schaltjahre richtig als nicht Schaltjahre erkannt ✅
4. Ein Jahre das durch 100 aber nicht durch 400 teilbar ist wird richtig als nicht Schaltjahr erkannt ✅
5. Wirft einen Typfehler für nicht integer Eingaben (z.B. Gleitkommazahlen oder Strings) ✅
6. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Fehlerhafte Testfälle: 

Bemerkungen:

Punkte: 6/6

Total: 18/18
'''