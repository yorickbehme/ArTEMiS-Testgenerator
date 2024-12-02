## **Prompt Beispiel optimierungs Untersuchung**

Es wird getestet ob ein spezialisiertes Beispiel im oneshot Prompt die Qualität der Ergebnisse verbessert. 

In der folgenden Analyse wird der Einfluss eines speziellen Beispiels in der Prompteingabe hinsichtlich ihres Einflusses auf die Leistungsfähigkeit bei der Testgenerierung untersucht. Jeder Test durchlauf besteht aus drei Iterationen des gleichen Basisprompts einmal mit einem allgemeinen und einmal mit einem speziellen Beispiel.

Die Ergebnisse der Modellausgabe werden anschließend mit einer vordefinierten Liste von **Standard-Testfällen** abgeglichen, bewertet und in ein Punktesystem überführt. Abschließend werden die Ergebnisse in **Auswertungstabellen** zusammengefasst und gegenübergestellt. Diese befinden sich der Übersichtlichkeit halber am Anfang des Dokuments.

---

## **Auswertungstabelle**

| **Prompt-Art**                        | **Iteration 1** | **Iteration 2** | **Iteration 3** | **Total** | **Prozent** |
|---------------------------------------|-----------------|-----------------|-----------------|-----------|-------------|
| **Allgemeines Beispiel**              | 6/10            | 7/10            | 7/10            | 20/30     | 66,67%      |
| **Spezialisiertes Beispiel**          | 8/10            | 8/10            | 8/10            | 24/30     | 80,00%      |

---

## **Allgemeines Beispiel**

### **Prompt**

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
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b 
    return b
```

---

```
import unittest

class TestFibonacciFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'fibonacci' existiert.
        """
        self.assertTrue(callable(fibonacci), "'fibonacci' soll existieren. 
Vergewissere dich, dass die Funktion definiert ist.")

    def test_fibonacci_zero(self):
        """
        Prüft, ob 'fibonacci' für n=0 korrekt ausgerichtet wird.
        """
        self.assertEqual(fibonacci(0), 0, "'fibonacci' soll für n=0 den 
Wert '0' zurückgeben. Überprüfe die Ausgabe bei einfacher Eingabe.")

    def test_fibonacci_one(self):
        """
        Prüft, ob 'fibonacci' für n=1 korrekt ausgerichtet wird.
        """
        self.assertEqual(fibonacci(1), 1, "'fibonacci' soll für n=1 den 
Wert '1' zurückgeben. Überprüfe die Ausgabe bei einfacher Eingabe.")

    def test_fibonacci_small_positive_integer(self):
        """
        Prüft, ob 'fibonacci' eine positive Ganzzahl korrekt berechnet.
        """
        self.assertEqual(fibonacci(5), 5, "'fibonacci' soll eine positive 
Ganzzahl korrekt berechnen. Überprüfe die Ausgabe bei kleinen Eingaben.")

    def test_fibonacci_large_positive_integer(self):
        """
        Prüft, ob 'fibonacci' eine positive Ganzzahl korrekt berechnet.
        """
        self.assertEqual(fibonacci(10), 55, "'fibonacci' soll eine 
positive Ganzzahl korrekt berechnen. Überprüfe die Ausgabe bei größeren 
Eingaben.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'fibonacci' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'fibonacci' soll für 
String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingangen 
korrekt validiert werden."): fibonacci("a")

    def test_invalid_type_none(self):
        """
        Prüft, ob 'fibonacci' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'fibonacci' soll für 
'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingangen 
korrekt validiert werden."): fibonacci(None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "fibonacci" Funkton existiert ✅
2. Gibt für eine '0' Eingabe das Ergebnis: 0 aus ✅
3. Gibt für die '1' Eingabe das Ergebnis: 1 aus ✅
4. Berechnet die n'te Stelle der Fibonacci Reihe korrekt ✅
5. Berechnet die n'te Stelle für große Zahlen korrekt ❌
6. Prüft ob die Implementierung iterativ umgesetzt wurde ❌
7. Wirft einen Typfehler für Eingaben die nicht integer Zahlen sind ✅
8. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 6/8**

---

```
import unittest

class TestFibonacciFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'fibonacci' existiert.
        """
        self.assertTrue(callable(fibonacci), "'fibonacci' soll existieren. 
Vergewissere dich, dass die Funktion definiert ist.")

    def test_fibonacci_zero(self):
        """
        Prüft, ob 'fibonacci' den Wert 0 bei Eingabe von 0 korrekt 
zurückgibt.
        """
        self.assertEqual(fibonacci(0), 0, "'fibonacci' soll den Wert 0 bei 
Eingabe von 0 zurückgeben. Überprüfe, ob die Implementierung für den 
Nullfall korrekt ist.")

    def test_fibonacci_one(self):
        """
        Prüft, ob 'fibonacci' den Wert 1 bei Eingabe von 1 korrekt 
zurückgibt.
        """
        self.assertEqual(fibonacci(1), 1, "'fibonacci' soll den Wert 1 bei 
Eingabe von 1 zurückgeben. Überprüfe, ob die Implementierung für den 
Einheitsfall korrekt ist.")

    def test_fibonacci_positive_integer(self):
        """
        Prüft, ob 'fibonacci' positive Ganzzahlen korrekt berechnet.
        """
        self.assertEqual(fibonacci(5), 5, "'fibonacci' soll positive 
Ganzzahlen korrekt berechnen. Überprüfe, ob die Implementierung für 
einfache Fälle korrekt ist.")

    def test_fibonacci_negative_integer(self):
        """
        Prüft, ob 'fibonacci' negative Ganzzahlen korrekt berechnet.
        """
        self.assertEqual(fibonacci(-5), 3, "'fibonacci' soll negative 
Ganzzahlen korrekt berechnen. Vergewissere dich, dass Vorzeichen richtig 
behandelt werden.")

    def test_fibonacci_large_positive_integer(self):
        """
        Prüft, ob 'fibonacci' sehr große positive Zahlen korrekt 
berechnet.
        """
        self.assertEqual(fibonacci(100), 354224848179261915075, 
"'fibonacci' soll sehr große positive Zahlen korrekt berechnen. Überprüfe, 
ob die Implementierung für großes Ausmaß korrekt ist.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'fibonacci' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'fibonacci' soll für 
String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt 
validiert werden."): fibonacci("a")

    def test_invalid_type_none(self):
        """
        Prüft, ob 'fibonacci' bei 'None'-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'fibonacci' soll für 
'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt 
validiert werden."): fibonacci(None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "fibonacci" Funkton existiert ✅
2. Gibt für eine '0' Eingabe das Ergebnis: 0 aus ✅
3. Gibt für die '1' Eingabe das Ergebnis: 1 aus ✅
4. Berechnet die n'te Stelle der Fibonacci Reihe korrekt ✅
5. Berechnet die n'te Stelle für große Zahlen korrekt ✅
6. Prüft ob die Implementierung iterativ umgesetzt wurde ❌
7. Wirft einen Typfehler für Eingaben die nicht integer Zahlen sind ✅
8. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Bemerkung: 
- Fehlerhafte Rechnung für Negative-Integer

**Punkte: 7/8**

---

Here is the Python test suite:

```
import unittest
import math

class TestFibonacciFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'fibonacci' existiert.
        """
        self.assertTrue(callable(fibonacci), "'fibonacci' soll existieren. 
Vergewissere dich, dass die Funktion definiert ist.")

    def test_fibonacci_zero(self):
        """
        Prüft, ob 'fibonacci' bei Eingabe 0 den korrekten Wert zurückgibt.
        """
        self.assertEqual(fibonacci(0), 0, "'fibonacci' soll für Eingabe 0 
den korrekten Wert zurückgeben. Überprüfe, ob die Basistruppen richtig 
berechnet werden.")

    def test_fibonacci_one(self):
        """
        Prüft, ob 'fibonacci' bei Eingabe 1 den korrekten Wert zurückgibt.
        """
        self.assertEqual(fibonacci(1), 1, "'fibonacci' soll für Eingabe 1 
den korrekten Wert zurückgeben. Vergewissere dich, dass die Rekursion 
korrekt abgeschlossen wird.")

    def test_fibonacci_small_number(self):
        """
        Prüft, ob 'fibonacci' bei kleineren Zahlen den korrekten Wert 
zurückgibt.
        """
        for i in range(1, 10):
            self.assertEqual(fibonacci(i), math.fib(i), "'fibonacci' soll 
für kleinere Zahlen den korrekten Wert zurückgeben. Überprüfe die 
Fibonacci-Folge.")

    def test_fibonacci_large_number(self):
        """
        Prüft, ob 'fibonacci' bei größeren Zahlen den korrekten Wert 
zurückgibt.
        """
        for i in range(10, 20):
            self.assertEqual(fibonacci(i), math.fib(i), "'fibonacci' soll 
für größere Zahlen den korrekten Wert zurückgeben. Überprüfe die 
Fibonacci-Folge.")

    def test_invalid_type_string(self):
        """
        Prüft, ob 'fibonacci' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'fibonacci' soll für 
String-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt 
validiert werden."): fibonacci("a")

    def test_invalid_type_none(self):
        """
        Prüft, ob 'fibonacci' bei 'None'-Eingangen einen Typfehler 
auslöst.
        """
        with self.assertRaises(TypeError, msg="'fibonacci' soll für 
'None'-Eingaben einen Typfehler werfen. Überprüfe, ob die Eingaben korrekt 
validiert werden."): fibonacci(None)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "fibonacci" Funkton existiert ✅
2. Gibt für eine '0' Eingabe das Ergebnis: 0 aus ✅
3. Gibt für die '1' Eingabe das Ergebnis: 1 aus ✅
4. Berechnet die n'te Stelle der Fibonacci Reihe korrekt ✅
5. Berechnet die n'te Stelle für große Zahlen korrekt ✅
6. Prüft ob die Implementierung iterativ umgesetzt wurde ❌
7. Wirft einen Typfehler für Eingaben die nicht integer Zahlen sind ✅
8. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 7/8**

***Total: 20/24***

---

## **Spezielles Beispiel**

### **Prompt**

---

You are a Python test generation tool. **Generate a detailed and comprehensive Python test suite for the provided code.** Make sure the test suite aligns with the given examples and satisfies all specified requirements:

### Requirements ###
* Include test cases to verify the existence of all classes and functions, expected behavior for typical inputs, edge cases for unusual inputs, and handling of type errors.
* Provide clear feedback in German for each failed test, specifying what functionality is required to pass.
* Output only the complete Python test suite without any additional explanations or comments.

### Example ###

```
import unittest

class TestFactorialFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'factorial' existiert.
        """
        self.assertTrue(callable(factorial), "'factorial' soll existieren. Vergewissere dich, dass die Funktion definiert ist.")

    def test_factorial_of_zero(self):
        """
        Prüft, ob 'factorial' die Fakultät von 0 korrekt berechnet.
        """
        self.assertEqual(factorial(0), 1, "'factorial' soll für 0 den Wert 1 zurückgeben. Überprüfe die Basisfälle.")

    def test_factorial_of_one(self):
        """
        Prüft, ob 'factorial' die Fakultät von 1 korrekt berechnet.
        """
        self.assertEqual(factorial(1), 1, "'factorial' soll für 1 den Wert 1 zurückgeben. Überprüfe die Basisfälle.")

    def test_factorial_of_small_positive_integer(self):
        """
        Prüft, ob 'factorial' die Fakultät einer kleinen positiven Zahl korrekt berechnet.
        """
        self.assertEqual(factorial(5), 120, "'factorial' soll für 5 den Wert 120 zurückgeben. Überprüfe die Multiplikationslogik.")

    def test_factorial_of_large_positive_integer(self):
        """
        Prüft, ob 'factorial' die Fakultät einer großen positiven Zahl korrekt berechnet.
        """
        self.assertEqual(factorial(10), 3628800, "'factorial' soll für 10 den Wert 3628800 zurückgeben. Überprüfe die Skalierbarkeit.")

    def test_invalid_negative_integer(self):
        """
        Prüft, ob 'factorial' bei negativen Zahlen einen Fehler auslöst.
        """
        with self.assertRaises(ValueError, msg="'factorial' soll bei negativen Eingaben einen Fehler werfen. Überprüfe die Validierung."):
            factorial(-1)

    def test_invalid_type(self):
        """
        Prüft, ob 'factorial' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'factorial' soll für String-Eingaben einen Typfehler werfen. Überprüfe die Typenvalidierung."):
            factorial("5")

    def test_iterative_implementation(self):
        """
        Prüft, ob 'factorial' iterativ implementiert ist, indem die Anzahl der Aufrufe im Quellcode überprüft wird.
        """
        import inspect
        source_code = inspect.getsource(factorial)

        recursive_calls = source_code.count("factorial(") > 1

        self.assertFalse(
            recursive_calls,
            "'factorial' soll iterativ implementiert sein. Es wurden rekursive Aufrufe gefunden."
        )

if __name__ == "__main__":
    unittest.main()
```
### Code ###
```
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b 
    return b
```

---

Here is the Python test suite based on the provided code:

```
import unittest
import inspect

class TestFactorialFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'fibonacci' existiert.
        """
        self.assertTrue(callable(fibonacci), "'fibonacci' soll existieren. 
Vergewissere dich, dass die Funktion definiert ist.")

    def test_fibonacci_of_zero(self):
        """
        Prüft, ob 'fibonacci' die Fibonacci-Zahl von 0 korrekt berechnet.
        """
        self.assertEqual(fibonacci(0), 0, "'fibonacci' soll für 0 den Wert 
0 zurückgeben. Überprüfe die Basisfälle.")

    def test_fibonacci_of_one(self):
        """
        Prüft, ob 'fibonacci' die Fibonacci-Zahl von 1 korrekt berechnet.
        """
        self.assertEqual(fibonacci(1), 1, "'fibonacci' soll für 1 den Wert 
1 zurückgeben. Überprüfe die Basisfälle.")

    def test_fibonacci_of_small_positive_integer(self):
        """
        Prüft, ob 'fibonacci' die Fibonacci-Zahl einer kleinen positiven 
Zahl korrekt berechnet.
        """
        self.assertEqual(fibonacci(5), 5, "'fibonacci' soll für 5 den Wert 
5 zurückgeben. Überprüfe die rekursive Implementierung.")

    def test_fibonacci_of_large_positive_integer(self):
        """
        Prüft, ob 'fibonacci' die Fibonacci-Zahl einer großen positiven 
Zahl korrekt berechnet.
        """
        self.assertEqual(fibonacci(10), 55, "'fibonacci' soll für 10 den 
Wert 55 zurückgeben. Überprüfe die Skalierbarkeit.")

    def test_invalid_negative_integer(self):
        """
        Prüft, ob 'fibonacci' bei negativen Zahlen einen Fehler auslöst.
        """
        with self.assertRaises(ValueError, msg="'fibonacci' soll bei 
negativen Eingaben einen Fehler werfen. Überprüfe die Validierung."):
            fibonacci(-1)

    def test_invalid_type(self):
        """
        Prüft, ob 'fibonacci' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'fibonacci' soll für 
String-Eingaben einen Typfehler werfen. Überprüfe die Typenvalidierung."):
            fibonacci("5")

    def test_iterative_implementation(self):
        """
        Prüft, ob 'fibonacci' iterativ implementiert ist, indem die Anzahl 
der Aufrufe im Quellcode überprüft wird.
        """
        import inspect
        source_code = inspect.getsource(fibonacci)

        recursive_calls = source_code.count("fibonacci(") > 1

        self.assertFalse(
            recursive_calls,
            "'fibonacci' soll iterativ implementiert sein. Es wurden 
rekursive Aufrufe gefunden."
        )

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "fibonacci" Funkton existiert ✅
2. Gibt für eine '0' Eingabe das Ergebnis: 0 aus ✅
3. Gibt für die '1' Eingabe das Ergebnis: 1 aus ✅
4. Berechnet die n'te Stelle der Fibonacci Reihe korrekt ✅
5. Berechnet die n'te Stelle für große Zahlen korrekt ✅
6. Prüft ob die Implementierung iterativ umgesetzt wurde ✅
7. Wirft einen Typfehler für Eingaben die nicht integer Zahlen sind ✅
8. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 8/8**

---

```
import unittest

class TestFactorialFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'factorial' existiert.
        """
        self.assertTrue(callable(fibonacci), "'factorial' soll existieren. 
Vergewissere dich, dass die Funktion definiert ist.")

    def test_fibonacci_of_zero(self):
        """
        Prüft, ob 'factorial' die Fibonacci-Sequenz von 0 korrekt 
berechnet.
        """
        self.assertEqual(fibonacci(0), 0, "'factorial' soll für 0 den Wert 
0 zurückgeben. Überprüfe die Basisfälle.")

    def test_fibonacci_of_one(self):
        """
        Prüft, ob 'factorial' die Fibonacci-Sequenz von 1 korrekt 
berechnet.
        """
        self.assertEqual(fibonacci(1), 1, "'factorial' soll für 1 den Wert 
1 zurückgeben. Überprüfe die Basisfälle.")

    def test_fibonacci_of_small_positive_integer(self):
        """
        Prüft, ob 'factorial' die Fibonacci-Sequenz einer kleinen 
positiven Zahl korrekt berechnet.
        """
        self.assertEqual(fibonacci(5), 5, "'factorial' soll für 5 den Wert 
5 zurückgeben. Überprüfe die Rekursionslogik.")

    def test_fibonacci_of_large_positive_integer(self):
        """
        Prüft, ob 'factorial' die Fibonacci-Sequenz einer großen positiven 
Zahl korrekt berechnet.
        """
        self.assertEqual(fibonacci(10), 55, "'factorial' soll für 10 den 
Wert 55 zurückgeben. Überprüfe die Skalierbarkeit.")

    def test_invalid_negative_integer(self):
        """
        Prüft, ob 'factorial' bei negativen Zahlen einen Fehler auslöst.
        """
        with self.assertRaises(ValueError, msg="'factorial' soll bei 
negativen Eingaben einen Fehler werfen. Überprüfe die Validierung."):
            fibonacci(-1)

    def test_invalid_type(self):
        """
        Prüft, ob 'factorial' bei String-Eingaben einen Typfehler auslöst.
        """
        with self.assertRaises(TypeError, msg="'factorial' soll für 
String-Eingaben einen Typfehler werfen. Überprüfe die Typenvalidierung."):
            fibonacci("5")

    def test_iterative_implementation(self):
        """
        Prüft, ob 'factorial' iterativ implementiert ist, indem die Anzahl 
der Aufrufe im Quellcode überprüft wird.
        """
        import inspect
        source_code = inspect.getsource(fibonacci)

        recursive_calls = source_code.count("fibonacci(") > 1

        self.assertFalse(
            recursive_calls,
            "'factorial' soll iterativ implementiert sein. Es wurden 
rekursive Aufrufe gefunden."
        )

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "fibonacci" Funkton existiert ✅
2. Gibt für eine '0' Eingabe das Ergebnis: 0 aus ✅
3. Gibt für die '1' Eingabe das Ergebnis: 1 aus ✅
4. Berechnet die n'te Stelle der Fibonacci Reihe korrekt ✅
5. Berechnet die n'te Stelle für große Zahlen korrekt ✅
6. Prüft ob die Implementierung iterativ umgesetzt wurde ✅
7. Wirft einen Typfehler für Eingaben die nicht integer Zahlen sind ✅
8. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 8/8**

---

```
import unittest

class TestFactorialFunction(unittest.TestCase):

    def test_function_exists(self):
        """
        Prüft, ob die Funktion 'factorial' existiert.
        """
        self.assertTrue(callable(fibonacci), "'factorial' soll existieren. 
Vergewissere dich, dass die Funktion definiert ist.")

    def test_factorial_of_zero(self):
        """
        Prüft, ob 'factorial' die Fakultät von 0 korrekt berechnet.
        """
        self.assertEqual(fibonacci(0), 0, "'factorial' soll für 0 den Wert 
0 zurückgeben. Überprüfe die Basisfälle.")

    def test_factorial_of_one(self):
        """
        Prüft, ob 'factorial' die Fakultät von 1 korrekt berechnet.
        """
        self.assertEqual(fibonacci(1), 1, "'factorial' soll für 1 den Wert 
1 zurückgeben. Überprüfe die Basisfälle.")

    def test_factorial_of_small_positive_integer(self):
        """
        Prüft, ob 'factorial' die Fakultät einer kleinen positiven Zahl 
korrekt berechnet.
        """
        self.assertEqual(fibonacci(5), 5, "'factorial' soll für 5 den Wert 
5 zurückgeben. Überprüfe die Iteration.")

    def test_factorial_of_large_positive_integer(self):
        """
        Prüft, ob 'factorial' die Fakultät einer großen positiven Zahl 
korrekt berechnet.
        """
        self.assertEqual(fibonacci(10), 55, "'factorial' soll für 10 den 
Wert 55 zurückgeben. Überprüfe die Skalierbarkeit.")

    def test_invalid_negative_integer(self):
        """
        Prüft, ob 'factorial' bei negativen Zahlen einen Fehler auslöst.
        """
        with self.assertRaises(ValueError, msg="'factorial' soll bei 
negativen Eingaben einen Fehler werfen. Überprüfe die Validierung."):
            fibonacci(-1)

    def test_invalid_type(self):
        """
        Prüft, ob 'factorial' bei String-Eingangen einen Typfehler 
auslöst.
        """
        with self.assertRaises(TypeError, msg="'factorial' soll für 
String-Eingaben einen Typfehler werfen. Überprüfe die Typenvalidierung."):
            fibonacci("5")

    def test_iterative_implementation(self):
        """
        Prüft, ob 'factorial' iterativ implementiert ist, indem die Anzahl 
der Aufrufe im Quellcode überprüft wird.
        """
        import inspect
        source_code = inspect.getsource(fibonacci)

        recursive_calls = source_code.count("fibonacci(") > 1

        self.assertFalse(
            recursive_calls,
            "'factorial' soll iterativ implementiert sein. Es wurden 
rekursive Aufrufe gefunden."
        )

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "fibonacci" Funkton existiert ✅
2. Gibt für eine '0' Eingabe das Ergebnis: 0 aus ✅
3. Gibt für die '1' Eingabe das Ergebnis: 1 aus ✅
4. Berechnet die n'te Stelle der Fibonacci Reihe korrekt ✅
5. Berechnet die n'te Stelle für große Zahlen korrekt ✅
6. Prüft ob die Implementierung iterativ umgesetzt wurde ✅
7. Wirft einen Typfehler für Eingaben die nicht integer Zahlen sind ✅
8. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 8/8**

***Total: 24/24***

---
