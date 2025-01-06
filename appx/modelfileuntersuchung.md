# **Modelfileuntersuchung**

In der folgenden Analyse wird der Einfluss eines System Prompts sowie verschiedener Laufzeit Parameter hinsichtlich ihres Einflusses auf die Leistungsfähigkeit bei der Testgenerierung untersucht. Jeder Test durchlauf besteht aus drei Iterationen der gleichen Prompteingabe.

Die Ergebnisse der Modellausgabe werden anschließend mit einer vordefinierten Liste von **Standard-Testfällen** abgeglichen, bewertet und in ein Punktesystem überführt. Abschließend werden die Ergebnisse in **Auswertungstabellen** zusammengefasst und gegenübergestellt. Diese befinden sich der Übersichtlichkeit halber am Anfang des Dokuments.

---

## **Auswertungstabelle**

| **Modellparameter**                            | **Iteration 1** | **Iteration 2** | **Iteration 3** | **Total** | **Prozent** |
|---------------------------------------|-----------------|-----------------|-----------------|-----------|-------------|
| **Standard-Parameter**                   | 8/10            | 9/10            | 6/10            | 23/30     | 76,67%      |
| **System-Prompt mit Standard-Parametern** | 5/10            | 5/10            | 5/10            | 15/30     | 50,00%      |
| **Konservative-Parameter**               | 1/10            | 1/10            | 5/10            | 7/30     | 23,33%      |
| **Kreative-Parameter**                   | 7/10            | 8/10            | 6/10            | 21/30     | 70,00%      |
| **Sehr Kreative-Parameter**                   | 5/10            | 1/10            | 1/10            | 7/30     | 23,33%      |

---

### **Standard-Prompt ohne Modelfileanpassungen**

---

You are a Python test generation tool. **Generate a detailed and comprehensive Python test suite for the provided code.** Make sure the test suite aligns with the given examples and satisfies all specified requirements:

### Requirements ###
* Include test cases to verify the existence of all classes and functions, expected behavior for typical inputs, edge cases for unusual inputs, and handling of type errors.
* Provide clear feedback in German for each failed test, specifying what functionality is required to pass.
* Output only the complete Python test suite without any additional explanations or comments.

### Example ###
```
import unittest

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
### Code ###
```
def calculate_mean(number_list: list):
    length = len(number_list)
    if length == 0:
        return None
    for l in number_list:
        if type(l) != int:
            if type(l) != float:
                return None
    summe = sum(number_list)
    average = summe / length
    return average
```
---

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

---

### **Auswertung**
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

**Punkte: 8/10**

---

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

### **Auswertung**
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

**Punkte: 9/10**

---

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

---

### **Auswertung**
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

**Punkte: 6/10**

***Total: 23/30***

---

## **Mit System Prompt**

**System Prompt**

---

You are a Python test generation tool. **Your primary task is to generate a detailed and comprehensive Python test suite for the provided code.** Make sure the test suite aligns with the given examples and satisfies all specified requirements:

* Include test cases to verify the existence of all classes and functions, expected behavior for typical inputs, edge cases for unusual inputs, and handling of type errors.
* Provide clear feedback in German for each failed test, specifying what functionality is required to pass.
* Output only the complete Python test suite without any additional explanations or comments.

---

**User Prompt**

---

Generate a comprehensive Python test suite for the provided code, ensuring it aligns with the structure and style of the example code. 

### Example ###
```
import unittest

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
### Code ###
```
def calculate_mean(number_list: list):
    length = len(number_list)
    if length == 0:
        return None
    for l in number_list:
        if type(l) != int:
            if type(l) != float:
                return None
    summe = sum(number_list)
    average = summe / length
    return average
```

---

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
        Prüft, ob 'calculate_mean' eine leere Liste korrekt behandelt.
        """
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll eine leere Liste auf 'None' setzen. Überprüfe, ob der Code für leere Listen funktioniert.")

    def test_calculate_mean_single_element(self):
        """
        Prüft, ob 'calculate_mean' eine Einzelausgabe korrekt behandelt.
        """
        self.assertEqual(calculate_mean([1]), 1, "'calculate_mean' soll eine Liste mit einem Element auf denselben Wert setzen. Überprüfe, ob der Code für einfache Listen funktioniert.")

    def test_calculate_mean_multiple_elements(self):
        """
        Prüft, ob 'calculate_mean' mehrere Ausgaben korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll eine Liste von Zahlen summiert und den Mittelwert berechnen. Überprüfe, ob der Code für Listen mit mehreren Elementen funktioniert.")

    def test_calculate_mean_mixed_types(self):
        """
        Prüft, ob 'calculate_mean' gemischte Datentypen korrekt behandelt.
        """
        self.assertEqual(calculate_mean([1, 2.5]), 1.75, "'calculate_mean' soll gemischte Datentypen wie Ganzzahlen und Kommazahlen korrekt addieren. Überprüfe, ob der Code für Listen mit verschiedenen Typen funktioniert.")

    def test_calculate_mean_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean("a")

    def test_calculate_mean_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean(None)

    def test_calculate_mean_invalid_type_list(self):
        """
        Prüft, ob 'calculate_mean' bei Listen-Eingaben mit falschen Elementen einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für Listen-Eingaben mit falschen Elementen einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, "a", 2])

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 5/10**

---

```
import unittest

class TestAddFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_calculate_mean_empty_list(self):
        """
        Prüft, ob 'calculate_mean' eine leere Liste korrekt behandelt.
        """
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll eine leere Liste als 'None' zurückgeben. Überprüfe, ob der Code für keine Eingaben funktioniert.")

    def test_calculate_mean_single_value(self):
        """
        Prüft, ob 'calculate_mean' bei einer einzigen Eingabe den Wert korrekt zurückgibt.
        """
        self.assertEqual(calculate_mean([1]), 1.0, "'calculate_mean' soll eine einzige Eingabe korrekt berechnen. Überprüfe, ob der Code einfache Zahlen korrekt behandelt.")

    def test_calculate_mean_multiple_values(self):
        """
        Prüft, ob 'calculate_mean' bei mehreren Eingaben den Wert korrekt zurückgibt.
        """
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll mehrere Werte korrekt berechnen. Überprüfe, ob der Code für einfache Listen korrekt funktioniert.")

    def test_calculate_mean_mixed_int_float(self):
        """
        Prüft, ob 'calculate_mean' bei einer Liste aus Mischung von ganzen und Fließkommazahlen den Wert korrekt zurückgibt.
        """
        self.assertEqual(calculate_mean([1, 2.5]), 1.75, "'calculate_mean' soll eine Mischung aus ganzen und Fließkommazahlen korrekt berechnen. Überprüfe, ob der Code für Listen mit verschiedenen Typen korrekt funktioniert.")

    def test_calculate_mean_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean("a")

    def test_calculate_mean_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean(None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 5/10**

---

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
        Prüft, ob 'calculate_mean' eine leere Liste korrekt behandles.
        """
        self.assertIsNone(calculate_mean([]), "'calculate_mean' soll für eine leere Liste None zurückgeben. Überprüfe, ob der Code für den Fall einer leeren Eingabe funktioniert.")

    def test_calculate_mean_single_element(self):
        """
        Prüft, ob 'calculate_mean' eine Einzelelement-Liste korrekt behandles.
        """
        self.assertEqual(calculate_mean([5]), 5.0, "'calculate_mean' soll die Element-Zahl als Durchschnitt zurückgeben. Überprüfe, ob der Code für einfache Listen funktioniert.")

    def test_calculate_mean_multiple_elements(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mehrerer Elemente korrekt behandles.
        """
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll die Durchschnittsberechnung für Listen mit mehreren Elementen durchführen.")

    def test_calculate_mean_mixed_float_int(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von Float und Integer korrekt behandles.
        """
        self.assertAlmostEqual(calculate_mean([1.5, 2.0, 3]), 2.1666666666666665, places=5, msg="'calculate_mean' soll Mixed-Float-Integer-Liste korrekt durchführen.")

    def test_calculate_mean_invalid_type(self):
        """
        Prüft, ob 'calculate_mean' bei nicht-ganzen Typen einen Fehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für unzulässige Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean("a")

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 5/10**

**Total: 15/30**

---

### **Konservative Parameter mit Standad-Prompt**

## **Modelfile**

```
FROM llama3

PARAMETER temperature 0.5
PARAMETER num_ctx 4096
PARAMETER repeat_penalty 1.3
PARAMETER num_predict -2
PARAMETER top_k 30
PARAMETER top_p 0.85
```

---

```
import unittest

class TestAddFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'add' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_add_two_positive_integers(self):
        """
        Prüft, ob 'calculate mean' zwei positive Ganzzahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2]), 1.5, "'add' soll zwei positive Ganzzahlen addieren können. Überprüfe, ob der Code für einfache Summen funktioniert.")

    def test_add_two_negative_integers(self):
        """
        Prüft, ob 'calculate mean' two negative integers korrekt addiert.
        """
        self.assertEqual(calculate_mean([-1, -2]), -1.5, "'add' soll zwei negative Ganzzahlen addieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

    def test_add_positive_and_negative_integer(self):
        """
        Prüft, ob 'calculate mean' eine positive und eine negative Zahl korrekt addiert.
        """
        self.assertEqual(calculate_mean([-2, 3]), 0.5, "'add' soll eine negative und eine positive Zahl addieren können. Achte darauf, dass Vorzeichen korrekt verarbeitet werden.")

    def test_add_two_floats(self):
        """
        Prüft, ob 'calculate mean' zwei Kommazahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 2.5]), 2.0, "'add' soll mit Kommazahlen umgehen können. Überprüfe, ob Fließkommazahlen korrekt summiert werden.")

    def test_add_float_and_integer(self):
        """
        Prüft, ob 'calculate mean' eine Kommazahl und eine Ganzzahl korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 2]), 1.75, "'add' soll mit einer Kommazahl und einer Ganzzahl umgehen können. Überprüfe die Typenkompatibilität.")

    def test_add_zero_and_integer(self):
        """
        Prüft, ob 'calculate mean' die Zahl '0' korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2]), 1.5, "'add' soll mit '0' addieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_add_large_number(self):
        """
        Prüft, ob 'calculate mean' sehr große Zahlen umgehen kann.
        """
        self.assertEqual(calculate_mean([float('inf'), 1]), float('nan'), "'add' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'calculate mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für String-Eingangen einen Typfehler werfen. Überprüfe, ob die Einggaben korrekt validiert werden."): calculate_mean(["a", 1])

    def test_invalid_type_none(self):
        """
        Prüft, ob 'calculate mean' bei None-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für None-Eingangen einen Typfehler werfen. Überprüfe, ob die Einggaben korrekt validiert werden."): calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ❌
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Bemerkung:
- Alle Tests fälschlicherweise auf 'add' (Beispiel Funktion) bezogen

**Punkte: 1/10**

---

```
import unittest
from your_module import add, calculate_mean  # Import the functions to be 
tested

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
        self.assertEqual(add(-1, -2), -3, "'add' soll zwei negative Ganzenalzahlen addieren können. Vergewissere dich, dass Vorzeichen richtig behandelt werden.")

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
        self.assertEqual(add(1.5, 1), 2.5, "'add' soll mit einer Kommazahl und einer Ganzenalzahlen umgehen können. Überprüfe die Typenkompatibilität.")

    def test_add_zero_and_integer(self):
        """
        Prüft, ob 'add' die Zahl '0' korrekt addiert.
        """
        self.assertEqual(add(0, 1), 1, "'add' soll mit '0' addieren können. Stelle sicher, dass der Code '0' korrekt behandelt.")

    def test_add_large_number(self):
        """
        Prüft, ob 'add' sehr große Zahlen umgehen kann.
        """
        self.assertEqual(add(float('inf'), 1), float('inf'), "'add' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'add' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für String-Eingangen einen Typfehler werfen. Überprüfe, ob die Eingänge korrekt validiert werden."): add("a", 1)

    def test_invalid_type_none(self):
        """
        Prüft, ob 'add' bei None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für None-Eingänge einen Typfehler werfen. Überprüfe, ob die Eingänge korrekt validiert werden."): add(1, None)

    def test_calculate_mean(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von Zahlen richtig berechnet.
        """
        self.assertEqual(calculate_mean([0]), 0.0)
        
if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ❌
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Bemerkung:
- Alle Tests fälschlicherweise auf 'add' (Beispiel Funktion) bezogen

**Punkte: 1/10**

---

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
        Prüft, ob 'calculate_mean' eine leere Liste korrekt behandelt.
        """
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll für leerer Listen den Wert `None` zurückgeben. Überprüfe die Korrektheit des Rückgabewerts.")

    def test_calculate_mean_single_integer(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit einem ganzen Zahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1]), 1.0, "'calculate_mean' soll Listen mit einer Zahl richtig berechnen.")

    def test_calculate_mean_single_float(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit einem Fließzahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1.5]), 1.5, "'calculate_mean' soll Listen mit einer Kommazahl richtig berechnen.")

    def test_calculate_mean_multiple_integers(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mehrerer ganzen Zahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2]), 1.5, "'calculate_mean' soll Listen mit mehreren Zahlen richtig berechnen.")

    def test_calculate_mean_multiple_floats(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mehrerer Kommazahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1.5, 2]), 1.75, "'calculate_mean' soll Listen mit mehreren Kommazahlen richtig berechnen.")

    def test_calculate_mean_mixed_integers_and_floats(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von ganzen Zahlen und Kommazahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1.5, 2]), 1.75, "'calculate_mean' soll Listen mit Mischung aus Ganzzahl und Kommazahl richtig berechnen.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingangen einen Typfehler werfen. Überprüfe die Eingabegültigkeit"): calculate_mean("a")

    def test_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für `None`-Eingangen einen Typfehler werfen. Überprüfe die Eingabegültigkeit"): calculate_mean(None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 5/10**

***Total: 7/30***

---

### **Kreative Parameter mit Standad-Prompt**

## **Modelfile**

```
FROM llama3

PARAMETER temperature 0.9
PARAMETER num_ctx 4096
PARAMETER repeat_penalty 1.1
PARAMETER num_predict -2
PARAMETER top_k 50
PARAMETER top_p 0.95
```

---

```
import unittest

class TestAddFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_calculate_mean_empty_list(self):
        """
        Prüft, ob 'calculate_mean' eine leere Liste korrekt behandelt.
        """
        self.assertIsNone(calculate_mean([]), "'calculate_mean' soll eine leere Liste als 'None' zurückgeben. Überprüfe, ob der Code für leere Listen funktioniert.")

    def test_calculate_mean_single_element_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit einem Element korrekt behandeldd.
        """
        self.assertEqual(calculate_mean([5]), 5, "'calculate_mean' soll eine Liste mit einem Element korrekt berechnen. Überprüfe, ob das Ergebnis stimmt.")

    def test_calculate_mean_multiple_elements_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit mehreren Elementen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll eine Liste mit mehreren Elementen korrekt berechnen. Überprüfe, ob das Ergebnis stimmt.")

    def test_calculate_mean_mixed_types_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit verschiedenen Typen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([1, 2, 3.5]), 2.1666666666666665, "'calculate_mean' soll eine Liste mit verschiedenen Typen korrekt berechnen. Überprüfe, ob das Ergebnis stimmt.")

    def test_calculate_mean_non_number_types_list(self):
        """
        Prüft, ob 'calculate_mean' bei nicht-numerischen Elementen einen Fehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für keine Liste von nicht-numerischen Elementen berechnen können. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, 'a', None])

    def test_calculate_mean_negative_numbers(self):
        """
        Prüft, ob 'calculate_mean' negative Zahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([-1, -2, -3]), -2.0, "'calculate_mean' soll negative Zahlen korrekt berechnen. Überprüfe, ob das Ergebnis stimmt.")

    def test_calculate_mean_large_numbers(self):
        """
        Prüft, ob 'calculate_mean' große Zahlen korrekt berechnet.
        """
        self.assertEqual(calculate_mean([10**1000, 10**999]), (10**999.5), "'calculate_mean' soll auch sehr große Zahlen berechnen können. Überprüfe, ob das Ergebnis stimmt.")

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

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ✅
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 7/10**

---

```
import unittest

class TestAddFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'calculate_mean' existiert.
        """
        self.assertTrue(callable(calculate_mean), "'calculate_mean' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_calculate_mean_empty_list(self):
        """
        Prüft, ob 'calculate_mean' einen leeren Liste korrekt behandelt.
        """
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll eine leere Liste als Null zurückgeben. Überprüfe, ob die Funktion ein passendes Ergebnis für leere Listen returniert.")

    def test_calculate_mean_single_element_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit einem Element korrekt behandelt.
        """
        self.assertEqual(calculate_mean([1]), 1.0, "'calculate_mean' soll die Durchschnittsberechnung für Listen mit einem Element durchführen.")

    def test_calculate_mean_positive_integer_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von positiven Ganzzahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2]), 1.5, "'calculate_mean' soll positive Ganzzahlen addieren können.")

    def test_calculate_mean_negative_integer_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von negativen Ganzzahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([-1, -2]), -1.5, "'calculate_mean' soll negative Ganzzahlen addieren können.")

    def test_calculate_mean_positive_and_negative_integer_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von positiven und negativen Ganzzahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([-1, 2]), 0.5, "'calculate_mean' soll positive und negative Ganzzahlen addieren können.")

    def test_calculate_mean_float_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von Kommazahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 2.0]), 1.75, "'calculate_mean' soll mit Kommazahlen umgehen können.")

    def test_calculate_mean_mixed_type_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von verschiedenen Typen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2.5]), 1.75, "'calculate_mean' soll verschiedene Typen wie Ganzzahlen und Kommazahlen addieren können.")

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

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 8/10**

---

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
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll eine leere Liste als Ergebnis von 'None' ergeben. Überprüfe, ob die Funktion für leere Listen korrekt reagiert.")

    def test_calculate_mean_list_with_integers(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit ganzen Zahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll die Summe einer Liste von Ganzzahlen ergeben. Überprüfe, ob die Funktion für einfache Summen funktioniert.")

    def test_calculate_mean_list_with_floats(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit Fließkommazahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 2.0, 3.0]), 2.1666666666666667, "'calculate_mean' soll die Summe einer Liste von Kommazahlen ergeben. Überprüfe, ob Fließkommazahlen korrekt summiert werden.")

    def test_calculate_mean_list_with_mixed_types(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit gemischt Typen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2.5, 3]), 2.0, "'calculate_mean' soll die Summe einer Liste von verschiedenen Typen ergeben. Überprüfe, ob die Funktion verschiedene Typen korrekt verarbeitet.")

    def test_calculate_mean_list_with_zero(self):
        """
        Prüft, ob 'calculate_mean' eine Liste mit dem Wert '0' korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 2.5, -3]), 0.33333333333333337, "'calculate_mean' soll die Summe einer Liste von Zahlen ergeben. Überprüfe, ob der Code für den Wert '0' korrekt reagiert.")

    def test_calculate_mean_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean(["a", 1])

    def test_calculate_mean_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingangen einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```
---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 6/10**

***Total: 21/39***

---

### ** Sehr kreative Parameter mit Standad-Prompt**

## **Modelfile**

```
FROM llama3

PARAMETER temperature 1.1
PARAMETER num_ctx 4096
PARAMETER repeat_penalty 1.0
PARAMETER num_predict -2
PARAMETER top_k 60
PARAMETER top_p 0.96
```

---

Here is the Python test suite for the provided code:

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
        Prüft, ob 'calculate_mean' einen leeren Listen korrekt behandelt.
        """
        self.assertIs(calculate_mean([]), None, "'calculate_mean' soll für eine leere Liste None zurückgeben.")

    def test_calculate_mean_single_number(self):
        """
        Prüft, ob 'calculate_mean' eine einzige Zahl korrekt behanellt.
        """
        self.assertEqual(calculate_mean([5]), 5, "'calculate_mean' soll für eine einzige Zahl die Zahl zurückgeben.")

    def test_calculate_mean_integer_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von Ganzzahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2, 3, 4]), 2.5, "'calculate_mean' soll eine Liste von Ganzzahlen addieren können.")

    def test_calculate_mean_float_list(self):
        """
        Prüft, ob 'calculate_mean' eine Liste von Kommazahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1.5, 2.5, 3.5, 4.5]), 3.0, "'calculate_mean' soll mit Kommazahlen umgehen können.")

    def test_calculate_mean_mixed_integer_float_list(self):
        """
        Prüft, ob 'calculate_mean' eine Mischung von Ganzzahlen und Kommazahlen korrekt addiert.
        """
        self.assertEqual(calculate_mean([1, 2, 3, 4.5]), 2.5, "'calculate_mean' soll eine Mischung von Ganzzahlen und Kommazahlen addieren können.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'calculate_mean' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean(["a"])

    def test_invalid_type_none(self):
        """
        Prüft, ob 'calculate_mean' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```
---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 5/10**

---

```
import unittest

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
        self.assertEqual(add(1000000, 1), 1000001, "'add' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

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

    def test_invalid_type_none_again(self):
        """
        Prüft, ob 'add' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'add' soll für 'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt validiert werden."): add(None, 1)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ❌
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Bemerkung:
- Alle Tests fälschlicherweise auf 'add' (Beispiel Funktion) bezogen

**Punkte: 1/10**

---

```
import unittest

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
        self.assertEqual(add(10**100, 10**100), 10**100, "'add' soll auch mit großen Zahlen umgehen können. Achte darauf, dass keine Überläufe auftreten.")

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

    def test_add_too_few_arguments(self):
        """
        Prüft, ob 'add' zu wenig Argumente akzeptiert.
        """
        with self.assertRaises(TypeError, msg="'add' soll zu wenig Argumente akzeptieren. Überprüfe, ob die Funktion die richtigen Anzahl von Eingaben annimmt."): add()

    def test_add_too_many_arguments(self):
        """
        Prüft, ob 'add' zu viele Argumente akzeptiert.
        """
        with self.assertRaises(TypeError, msg="'add' soll zu viele Argumente akzeptieren. Überprüfe, ob die Funktion die richtigen Anzahl von Eingaben annimmt."): add(1, 2, 3)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ❌
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Bemerkung:
- Alle Tests fälschlicherweise auf 'add' (Beispiel Funktion) bezogen

**Punkte: 1/10**

***Total: 7/30***

---
