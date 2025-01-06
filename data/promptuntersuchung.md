# **Promptuntersuchung**

In dieser Analyse werden verschiedene **Prompting-Techniken** systematisch untersucht. Zu jeder Technik wurde ein spezifischer Prompt entwickelt und optimiert, um ein Testskript für den unten stehenden **Code** zu generieren. Jeder Prompt wurde dreimal mit **Llama3** ausgeführt, und die Ergebnisse flossen in die Untersuchung ein.

Die Ausgaben wurden mit einer vordefinierten Liste von **Standard-Testfällen** abgeglichen, bewertet und in ein Punktesystem überführt. Abschließend sind die Ergebnisse in einer **Auswertungstabelle** zusammengefasst, die der Übersichtlichkeit halber am Anfang des Dokuments platziert wurde.

---

## **Auswertungstabelle**

| **Technik**           | **Iteration 1** | **Iteration 2** | **Iteration 3** | **Total** | **Prozent** |
|-----------------------|------------|------------|------------|-----------|-------------|
| **Instruction-Prompting** | 5/10       | 6/10       | 7/10       | 18/30     | 60,00%      |
| **Zero-Shot-Prompting**   | 2/10       | 2/10       | 5/10       | 9/30      | 30,00%      |
| **One-Shot-Prompting**    | 7/10       | 7/10       | 7/10       | 21/30     | 70,00%      |
| **Few-Shot-Prompting**    | 7/10       | 7/10       | 6/10       | 20/30     | 66,67%      |
| **Chain-of-Thought-Prompting** | 4/10       | 5/10       | 3/10       | 11/30     | 36,67%      |
| **Multitask-Prompting**   | 4/10       | 5/10       | 6/10       | 12/30     | 40,00%      |
| **Instruction + One-Shot Prompting** | 8/10       | 9/10       | 6/10       | 23/30     | 76,67%      |

---

## **Code**

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

## **Prompting-Techniken**
1. Instruction-Prompting
2. Zero-Shot-Prompting
3. One-Shot-Prompting
4. Few-Shot-Prompting
5. Chain of Thought Prompting
6. Multitask-Prompting
7. Inscruction-Prompting + One-Shot Prompting

---

## **Instruction-Prompting**

```
You are a Python test generation tool. **Generate a comprehensive Python test suite for the provided code.** Follow these requirements:

- Include test cases to verify the existence of all classes and functions, expected behavior for typical inputs, edge cases for unusual inputs, and handling of type errors.
- Provide clear feedback in German for each failed test, specifying what functionality is required to pass.
- Output only the complete Python test suite without any additional explanations or comments.

### Code to Test ###
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
class TestCalculateMean(unittest.TestCase):

    def test_calculate_mean_empty_list(self):
        self.assertIsNone(calculate_mean([]))

    def test_calculate_mean_single_element(self):
        self.assertEqual(calculate_mean([5]), 5)

    def test_calculate_mean_multiple_elements(self):
        self.assertAlmostEqual(calculate_mean([1,2,3,4,5]), 3)

    def test_calculate_mean_mixed_type_input(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b', 1, 2])

    def test_calculate_mean_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_mean([1, 2, 'a'])

    def test_calculate_mean_string_input(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b'])

    def test_calculate_mean_zero_length_list(self):
        self.assertIsNone(calculate_mean([]))

    def test_calculate_mean_negative_numbers(self):
        self.assertAlmostEqual(calculate_mean([-1, 0, 1]), 0)

    def test_calculate_mean_float_input(self):
        self.assertAlmostEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

---

```
import unittest
from your_module import calculate_mean

class TestCalculateMean(unittest.TestCase):

    def test_calculate_mean_empty_list(self):
        result = calculate_mean([])
        self.assertEqual(result, None)

    def test_calculate_mean_single_element(self):
        result = calculate_mean([5])
        self.assertAlmostEqual(result, 5.0)

    def test_calculate_mean_multiple_elements(self):
        result = calculate_mean([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 3.0)

    def test_calculate_mean_mixed_type(self):
        result = calculate_mean([1, "a", 3, None, 5])
        self.assertEqual(result, 3.0)

    def test_calculate_mean_non_numeric(self):
        with self.assertRaises(TypeError):
            calculate_mean([1, "a", 3, [4], 5])

    def test_calculate_mean_zero_length_list(self):
        result = calculate_mean([])
        self.assertEqual(result, None)

    def test_calculate_mean_negative_numbers(self):
        result = calculate_mean([-1, -2, -3])
        self.assertAlmostEqual(result, -2.0)

    def test_calculate_mean_decimal_numbers(self):
        result = calculate_mean([1.5, 2.75, 3.25])
        self.assertAlmostEqual(result, 2.5)

    def test_calculate_mean_negative_and_positive_numbers(self):
        result = calculate_mean([-1, -2, 0, 1, 2])
        self.assertAlmostEqual(result, 0.0)

    def test_calculate_mean_no_numeric_elements(self):
        with self.assertRaises(TypeError):
            calculate_mean(["a", "b", None])

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

---

3. ###
```
import unittest
from your_module import calculate_mean  # Replace with actual module name

class TestCalculateMean(unittest.TestCase):

    def test_calculate_mean_valid_input(self):
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0)

    def test_calculate_mean_empty_list(self):
        self.assertIsNone(calculate_mean([]))

    def test_calculate_mean_non_numeric_values(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b'])

    def test_calculate_mean_mixed_type_list(self):
        self.assertEqual(calculate_mean([1, 2.5, 3]), 2.1666666666666665)

    def test_calculate_mean_single_numeric_value(self):
        self.assertEqual(calculate_mean([4]), 4)

    def test_calculate_mean_multiple_numeric_values(self):
        self.assertEqual(calculate_mean([-1, -2, -3]), -2.0)

    def test_calculate_mean_negative_and_positive_values(self):
        self.assertAlmostEqual(calculate_mean([-5, 0, 5]), 0.0)

    def test_calculate_mean_non_integer_division(self):
        self.assertAlmostEqual(calculate_mean([1.0, 2.0, 3.0]), 2.0)

    def test_calculate_mean_float_input(self):
        self.assertAlmostEqual(calculate_mean([1.5, 2.5, 3.5]), 2.5)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 7/10**

***Total: 18/30***

---

## **Zero-Shot-Prompting**

```
You are a Python test generation tool. **Generate a Python test suite for the provided code** with German feedback for any failed tests. Use the following structure as a model.

### Code ###
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

Here is a Python test suite for the provided code, with German feedback 
for any failed tests:

```Python
import unittest
from your_module import calculate_mean  # Replace 'your_module' with the 
actual module name

class TestCalculateMean(unittest.TestCase):

    def test_empty_list(self):
        """
        Eine leere Liste sollte None zurückgeben.
        :return:
        """
        self.assertEqual(calculate_mean([]), None)

    def test_single_element_list(self):
        """
        Eine Liste mit einem Element sollte den Durchschnitt des Elements selbst zurückgeben.
        :return:
        """
        self.assertAlmostEqual(calculate_mean([5]), 5.0)

    def test_multiple_elements(self):
        """
        Eine Liste mit verschiedenen ganzen Zahlen sollte den Durchschnitt der Zahlen zurückgeben.
        :return:
        """
        self.assertAlmostEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)

    def test_mixed_types(self):
        """
        Eine Liste mit ganzen und floating-point-Zahlen sollte den Durchschnitt der Zahlen zurückgeben.
        :return:
        """
        self.assertAlmostEqual(calculate_mean([1, 2.0, 3, 4.5]), 2.75)

    def test_non_numeric_types(self):
        """
        Eine Liste mit nicht-numerischen Elementen sollte None zurückgeben.
        :return:
        """
        self.assertEqual(calculate_mean(["a", "b", "c"]), None)

if __name__ == '__main__':
    unittest.main()
```

This test suite covers the following scenarios:

- An empty list, which should return `None`.
- A single-element list, which should return the value of that element.
- A list with multiple elements, where all values are integers or floats, 
and the average is calculated correctly.
- A mixed list with both integers and floats, where the average is 
calculated correctly.
- A list with non-numeric elements, where `None` is returned.

The tests use `assertEqual` for exact equality and `assertAlmostEqual` for 
approximate floating-point comparisons. The German feedback comments are 
provided in docstrings for each test method.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 2/10**

---

Here is a test suite for the provided code with German feedback for any 
failed tests:

```
import unittest
from your_module import calculate_mean  # replace 'your_module' with the 
actual module name

class TestCalculateMean(unittest.TestCase):

    def test_empty_list(self):
        result = calculate_mean([])
        self.assertIsNone(result, "Fehler bei leeren Listen: Die Funktion sollte None zurückgeben")

    def test_single_element(self):
        result = calculate_mean([5])
        self.assertEqual(result, 5.0, "Fehler bei einer Einzelelement-Liste: Die Funktion sollte den Wert 5.0 zurückgeben")

    def test_multiple_elements(self):
        result = calculate_mean([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 3.0, places=10, msg="Fehler bei mehreren Elementen: Die Funktion sollte den Durchschnitt von 3.0 zurückgeben")

    def test_non_numeric_elements(self):
        result = calculate_mean(['a', 'b', 'c'])
        self.assertIsNone(result, "Fehler bei nicht-numericen Elementen: Die Funktion sollte None zurückgeben")

    def test_mixed_type_elements(self):
        result = calculate_mean([1, 2.0, 3, 4.5])
        self.assertAlmostEqual(result, 2.5, places=10, msg="Fehler bei gemischten Typ-Elementen: Die Funktion sollte den Durchschnitt von 2.5 zurückgeben")

    def test_division_by_zero(self):
        result = calculate_mean([1, 2, 3])
        self.assertIsNone(result, "Fehler bei Division durch Null: Die Funktion sollte None zurückgeben")

if __name__ == '__main__':
    unittest.main()
```

In this test suite, we're testing the following scenarios:

* An empty list
* A single element list
* A list with multiple numeric elements
* A list with non-numeric elements (e.g., strings)
* A list with mixed-type elements (e.g., integers and floats)
* A list where division by zero would occur

For each test, we're checking the expected output using assert methods 
provided by the unittest module. If a test fails, it will print an error 
message in German, indicating what went wrong.

Please replace `'your_module'` with the actual name of your Python module 
that contains the `calculate_mean` function.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 2/10**

---

Here is a Python test suite for the provided code:

```Python
import unittest
from calculate_mean import calculate_mean

class TestCalculateMean(unittest.TestCase):

    def test_calculate_mean_with_integers(self):
        # Positive integers
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)
        
        # Negative integers
        self.assertEqual(calculate_mean([-1, -2, -3, -4, -5]), -3.0)

    def test_calculate_mean_with_floats(self):
        # Positive floats
        self.assertAlmostEqual(calculate_mean([0.5, 1.25, 2.75, 3.5, 4.25]), 2.375)
        
        # Negative floats
        self.assertAlmostEqual(calculate_mean([-0.5, -1.25, -2.75, -3.5, -4.25]), -2.375)

    def test_calculate_mean_with_mixed_numbers(self):
        self.assertEqual(calculate_mean([1, 2.5, 3, 4.5, 5]), 3.0)
        
    def test_calculate_mean_empty_list(self):
        self.assertIsNone(calculate_mean([]))

    def test_calculate_mean_non_numeric_values(self):
        # Integers and floats
        with self.assertRaises(TypeError):
            calculate_mean([1, 2, 'a', 4, 5])

        # Non-numeric values only
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b', 'c'])

    def test_calculate_mean_with_single_value(self):
        self.assertEqual(calculate_mean([42]), 42.0)

if __name__ == '__main__':
    unittest.main()
```

These tests cover various scenarios, including:

1. Positive and negative integers
2. Positive and negative floats
3. Mixed numbers (integers and floats)
4. Empty list
5. Non-numeric values
6. Single value

Note: The `assertAlmostEqual` function is used to compare floating-point 
numbers with a small margin of error, as the actual result may not be 
exactly equal due to floating-point precision.

In case any test fails, you will receive German feedback like this:
```
Fehler in Test 'test_calculate_mean_with_integers': 
Stimme: 1
Erwartetes Ergebnis: <Expected>
Aktuelles Ergebnis: <Actual>

Fehlertext:

AssertionError: assertEqual expected: 3.0, actual: 2.5

In Zeile: 9 in TestCalculateMean
```
Translation:
"Error in test 'test_calculate_mean_with_integers': 
Value: 1
Expected result: <Expected>
Actual result: <Actual>

Error message:

AssertionError: assertEqual expected: 3.0, actual: 2.5

In line: 9 in TestCalculateMean"

This feedback helps you identify which test failed and what the expected 
and actual results were, making it easier to debug your code.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

***Total: 9/30***

---

## **One-Shot-Prompting**

```
You are a Python test generation tool. **Generate a Python test suite for the provided code** with German feedback for any failed tests. Use the following structure as a model.
### Example ###
import unittest

class TestAddFunction(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(add), "Erstelle eine Funktion mit dem namen 'add'.")

    def test_behavior(self):
        self.assertEqual(add(1, 2), 3, "'add' soll zwei positive Ganzzahlen addieren können.")
        self.assertEqual(add(-1, -2), -3, "'add' soll zwei negative Ganzzahlen addieren können.")
        self.assertEqual(add(-2, 3), 1, "'add' soll eine negative und eine positive Zahl addieren können.")
        self.assertEqual(add(1.5, 2.5), 4.0, "'add' soll mit Kommazaheln umgehen können.")
        self.assertEqual(add(1.5, 1), 2.5, "'add' soll mit einer ganzen und einer Kommazahl umgehen können.")
    
    def test_edge_cases(self):
        self.assertEqual(add(0, 1), 1, "'add' soll mit '0' addieren können.")
        self.assertEqual(add(float('inf'), 1), float('inf'), "'add' soll auch mit großen Zahlen umgehen können.")

    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'add' soll für String Eingaben einen Typfehler werfen."):
            add("a", 1)
        with self.assertRaises(TypeError, msg="'add' soll für 'None' Eingaben einen Typfehler werfen."):
            add(1, None)

if __name__ == "__main__":
    unittest.main()

### Code ###
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

Here's an example of how you can write tests using the provided structure:

```Python
import unittest
from your_module import calculate_mean  # Import the function to be tested

class TestCalculateMean(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(calculate_mean), "Die Funktion 'calculate_mean' existiert nicht.")

    def test_behavior(self):
        self.assertIsNone(calculate_mean([]), "'calculate_mean' sollte eine leere Liste auf None setzen.")
        self.assertEqual(calculate_mean([1]), 1, "'calculate_mean' sollte eine Liste mit einem Element auf das Element setzen.")
        self.assertEqual(calculate_mean([-2, 3, 5]), 2.0, "'calculate_mean' soll eine Mischung von positiven und negativen Zahlen verarbeiten können.")
        self.assertEqual(calculate_mean([1.5, 2.5]), 2.0, "'calculate_mean' soll mit Kommazahlen umgehen können.")
    
    def test_edge_cases(self):
        self.assertIsNone(calculate_mean([0]), None, "'calculate_mean' sollte eine Liste mit einem Null-Element auf None setzen.")
        self.assertEqual(calculate_mean([float('inf'), 1]), float('inf'), "'calculate_mean' soll auch mit großen Zahlen umgehen können.")

    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String Eingaben einen Typfehler werfen."):
            calculate_mean(["a", 1])
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None' Eingaben einen Typfehler werfen."):
            calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```

Please replace `'your_module'` with the name of your module where the 
`calculate_mean` function is located.

Remember to run these tests after fixing any bugs in your code to ensure 
that they are working as expected.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ✅
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 7/10**

---

Here is the test suite for the provided code:

```
### Test Suite for calculate_mean function ###

import unittest

class TestCalculateMean(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(calculate_mean), "Erstelle eine Funktion mit dem Namen 'calculate_mean'.")

    def test_behavior(self):
        self.assertEqual(calculate_mean([1, 2]), 1.5, "'calculate_mean' soll die Mittelwert berechnen.")
        self.assertIsNone(calculate_mean([]), msg="'calculate_mean' sollte für eine leere Liste None zurückgeben.")
        self.assertEqual(calculate_mean([-1, -2, 0, 1]), -1/2, "'calculate_mean' soll negative Zahlen addieren können.")
        self.assertAlmostEqual(calculate_mean([1.5, 2.5]), 2.0, places=1, msg="'calculate_mean' sollte mit Kommazahlen umgehen können.")
    
    def test_edge_cases(self):
        self.assertEqual(calculate_mean([0]), 0, "'calculate_mean' soll für eine Liste mit '0' den '0' als Mittelwert zurückgeben.")
        self.assertIsNone(calculate_mean([float('inf')]), msg="'calculate_mean' sollte auch mit großen Zahlen umgehen können.")
    
    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String Eingaben einen Typfehler werfen."):
            calculate_mean(["a", 1])
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None' Eingaben einen Typfehler werfen."):
            calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```

In this test suite, we have five tests:

- `test_function_exists`: This test checks if the function exists.
- `test_behavior`: This test checks if the function calculates the mean 
correctly for different types of input lists (e.g., with positive and 
negative numbers, with floating point numbers, etc.).
- `test_edge_cases`: This test checks if the function handles edge cases 
(e.g., an empty list, a list with only one element) correctly.
- `test_invalid_types`: This test checks if the function raises a 
TypeError when it encounters invalid types in the input list (e.g., 
strings or None).

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 7/10**

---

Here is the test suite for your code with German feedback:

```Python
import unittest
from your_module import calculate_mean  # replace 'your_module' with the 
actual name of your module/file

class TestCalculateMean(unittest.TestCase):

    def test_function_exists(self):
        self.assertTrue(callable(calculate_mean), "Erstelle eine Funktion mit dem Namen 'calculate_mean'.")

    def test_behavior(self):
        self.assertIsNone(calculate_mean([]), "Funktion sollte für leere Liste None zurückgeben.")
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll den Durchschnitt von ganzen Zahlen berechnen können.")
        self.assertEqual(calculate_mean([-1, -2, -3]), -2.0, "'calculate_mean' soll den Durchschnitt von negativen Zahlen berechnen können.")
        self.assertEqual(calculate_mean([1, 2, 3.5, 4, 5.5]), 3.2, "'calculate_mean' soll den Durchschnitt von ganzen und Kommazahlen berechnen können.")

    def test_edge_cases(self):
        self.assertIsNone(calculate_mean([0]), "Funktion sollte für eine Liste mit nur einem Element None zurückgeben.")
        self.assertEqual(calculate_mean([1.5, 2.5]), 2.0, "'calculate_mean' soll den Durchschnitt von Kommazahlen berechnen können.")

    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String Eingaben einen Typfehler werfen."):
            calculate_mean(["a", 1])
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None' Eingaben einen Typfehler werfen."):
            calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```

Replace `'your_module'` with the actual name of your module/file. The test 
suite includes tests for the existence of the function, its behavior on 
different types of inputs, edge cases and invalid types.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 7/10**

***Total: 21/30**

---

## **Few-Shot Prompting**

```
You are a Python test generation tool. **Generate a Python test suite for the provided code** with German feedback for any failed tests. Use the following structure as a model.
### Example 1 ###
import unittest

class TestAddFunction(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(add), "Erstelle eine Funktion mit dem namen 'add'.")

    def test_behavior(self):
        self.assertEqual(add(1, 2), 3, "'add' soll zwei positive Ganzzahlen addieren können.")
        self.assertEqual(add(-1, -2), -3, "'add' soll zwei negative Ganzzahlen addieren können.")
        self.assertEqual(add(-2, 3), 1, "'add' soll eine negative und eine positive Zahl addieren können.")
        self.assertEqual(add(1.5, 2.5), 4.0, "'add' soll mit Kommazaheln umgehen können.")
        self.assertEqual(add(1.5, 1), 2.5, "'add' soll mit einer ganzen und einer Kommazahl umgehen können.")
    
    def test_edge_cases(self):
        self.assertEqual(add(0, 1), 1, "'add' soll mit '0' addieren können.")
        self.assertEqual(add(float('inf'), 1), float('inf'), "'add' soll auch mit großen Zahlen umgehen können.")

    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'add' soll für String Eingaben einen Typfehler werfen."):
            add("a", 1)
        with self.assertRaises(TypeError, msg="'add' soll für 'None' Eingaben einen Typfehler werfen."):
            add(1, None)

if __name__ == "__main__":
    unittest.main()

### Example 2 ###
import unittest

class TestMultiplyFunction(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(multiply), "Erstelle eine Funktion mit dem Namen 'multiply'.")

    def test_behavior(self):
        self.assertEqual(multiply(2, 3), 6, "'multiply' soll zwei positive Ganzzahlen multiplizieren können.")
        self.assertEqual(multiply(-2, -3), 6, "'multiply' soll zwei negative Ganzzahlen multiplizieren können.")
        self.assertEqual(multiply(-2, 3), -6, "'multiply' soll eine negative und eine positive Zahl multiplizieren können.")
        self.assertEqual(multiply(2.5, 4), 10.0, "'multiply' soll mit Kommazahlen umgehen können.")
    
    def test_edge_cases(self):
        self.assertEqual(multiply(0, 5), 0, "'multiply' soll mit '0' multiplizieren können.")
        self.assertEqual(multiply(1e10, 2), 2e10, "'multiply' soll auch mit sehr großen Zahlen umgehen können.")

    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'multiply' soll für String Eingaben einen Typfehler werfen."):
            multiply("a", 1)
        with self.assertRaises(TypeError, msg="'multiply' soll für 'None' Eingaben einen Typfehler werfen."):
            multiply(1, None)

if __name__ == "__main__":
    unittest.main()

### Example 3 ###
import unittest

class TestDivideFunction(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(divide), "Erstelle eine Funktion mit dem Namen 'divide'.")

    def test_behavior(self):
        self.assertEqual(divide(6, 2), 3, "'divide' soll zwei positive Ganzzahlen korrekt dividieren können.")
        self.assertEqual(divide(-6, -2), 3, "'divide' soll zwei negative Ganzzahlen korrekt dividieren können.")
        self.assertEqual(divide(-6, 2), -3, "'divide' soll eine negative und eine positive Zahl korrekt dividieren können.")
        self.assertAlmostEqual(divide(5, 2), 2.5, "'divide' soll das Ergebnis als Gleitkommazahl zurückgeben, wenn nötig.")
    
    def test_edge_cases(self):
        self.assertEqual(divide(0, 1), 0, "'divide' soll bei einer Division von Null durch eine Zahl Null zurückgeben.")
        with self.assertRaises(ZeroDivisionError, msg="'divide' soll bei einer Division durch Null einen Fehler auslösen."):
            divide(1, 0)
    
    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'divide' soll für String-Eingaben einen TypeError auslösen."):
            divide("a", 2)
        with self.assertRaises(TypeError, msg="'divide' soll für 'None'-Eingaben einen TypeError auslösen."):
            divide(None, 2)
        with self.assertRaises(TypeError, msg="'divide' soll für nicht-numerische Eingaben einen TypeError auslösen."):
            divide(1, "b")

if __name__ == "__main__":
    unittest.main()

### Code ###
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

Here's a Python test suite using the unittest module:

```Python
import unittest
from statistics import mean  # Use the built-in mean function from the 
statistics module for comparison

class TestCalculateMeanFunction(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(calculate_mean), "Erstelle eine Funktion mit dem Namen 'calculate_mean'.")

    def test_behavior(self):
        self.assertAlmostEqual(calculate_mean([1, 2, 3]), mean([1, 2, 3]), msg="'calculate_mean' soll die durchschnittliche Zahl berechnen.")
        self.assertAlmostEqual(calculate_mean([-1, -2, -3]), mean([-1, -2, -3]), msg="'calculate_mean' soll auch negative Zahlen verarbeiten können.")
        self.assertAlmostEqual(calculate_mean([0.5, 1.5, 2.5]), mean([0.5, 1.5, 2.5]), msg="'calculate_mean' soll auch Kommazahlen verarbeiten können.")

    def test_edge_cases(self):
        self.assertIsNone(calculate_mean([]), msg="'calculate_mean' soll bei einer leeren Liste None zurückgeben.")
        self.assertAlmostEqual(calculate_mean([0]), mean([0]), msg="'calculate_mean' soll bei einer Liste mit nur einem Element den Wert dieses Elements zurückgeben.")
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String Eingaben einen TypeError auslösen."):
            calculate_mean(["a"])
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen TypeError auslösen."):
            calculate_mean([None])
        
if __name__ == "__main__":
    unittest.main()
```
This test suite covers the following scenarios:
- The function exists and can be called.
- The function calculates the mean correctly for different types of input 
(integer, negative, floating point).
- The function handles edge cases like an empty list or a single-element 
list correctly.
- The function raises TypeError when given invalid input (like strings or 
None).

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 7/10**

---

Here is the Python test suite for your `calculate_mean` function:

```
### Code ###
import unittest

class TestCalculateMeanFunction(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(calculate_mean), "Erstelle eine Funktion mit dem Namen 'calculate_mean'.")

    def test_behavior(self):
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll eine Liste von Zahlen korrekt mitteln können.")
        self.assertEqual(calculate_mean([-1, -2, -3]), -2.0, "'calculate_mean' soll eine Liste von negativen Zahlen mitteln können.")
        self.assertEqual(calculate_mean([1, 2, float('inf')]), 1.5, "'calculate_mean' soll auch mit sehr großen Zahlen umgehen können.")

    def test_edge_cases(self):
        self.assertIsNone(calculate_mean([]), "Die 'calculate_mean' Funktion sollte bei einer leeren Liste None zurückgeben.")
        self.assertEqual(calculate_mean([0]), 0.0, "'calculate_mean' soll bei einer Liste mit einem Element das element selbst zurückgeben.")
    
    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen TypeError auslösen."):
            calculate_mean(["a"])
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen TypeError auslösen."):
            calculate_mean([None])
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für nicht-numerische Eingaben einen TypeError auslösen."):
            calculate_mean([1, "b", 3])

if __name__ == "__main__":
    unittest.main()
```

This test suite checks the following:

*   The function `calculate_mean` exists and is callable.
*   It tests the basic functionality of calculating the mean with a list 
of numbers.
*   It tests edge cases such as an empty list, a list with a single 
element, or large numbers.
*   It tests invalid types by passing in strings, None values, and 
non-numeric values.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

Bemerkungen: 
- Beinhaltet Fehler

**Punkte: 7/10**

---

Here is the generated Python test suite with German feedback for any 
failed tests:
```
### Test Suite ###

import unittest

class TestCalculateMeanFunction(unittest.TestCase):

    def test_function_exists(self):
        self.assertTrue(callable(calculate_mean), "Erstelle eine Funktion mit dem Namen 'calculate_mean'.")

    def test_behavior(self):
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0, "'calculate_mean' soll die Durchschnittsberechnung korrekt durchführen.")
        self.assertEqual(calculate_mean([-1, -2, -3]), -2.0, "'calculate_mean' soll negative Zahlen korrekt berücksichtigen.")
        self.assertEqual(calculate_mean([1, 2, "a", 4]), None, "'calculate_mean' soll für nicht-numerische Eingaben 'None' zurückgeben.")
        self.assertAlmostEqual(calculate_mean([0.5, 0.8, 0.9]), 0.7333333333333333, "'calculate_mean' soll die Durchschnittsberechnung korrekt durchführen.")

    def test_edge_cases(self):
        self.assertEqual(calculate_mean([]), None, "'calculate_mean' soll bei einer leeren Liste 'None' zurückgeben.")
        self.assertEqual(calculate_mean([1]), 1.0, "'calculate_mean' soll bei einer Liste mit nur einem Element das Element selbst zurückgeben.")

    def test_invalid_types(self):
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für String-Eingaben einen TypeError auslösen."):
            calculate_mean(["a", "b"])
        with self.assertRaises(TypeError, msg="'calculate_mean' soll für 'None'-Eingaben einen TypeError auslösen."):
            calculate_mean([1, None])

if __name__ == "__main__":
    unittest.main()
```
This test suite checks the following:

* Whether the function `calculate_mean` exists
* The behavior of the function with different types of input (integer, 
float, negative numbers)
* Edge cases (empty list, single-element list)
* Invalid types (strings, None)

Note that I used the `assertAlmostEqual` method to check the 
floating-point calculation result. This is because floating-point 
calculations can sometimes produce slightly inaccurate results due to 
rounding errors.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ✅
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ✅

**Punkte: 6/10**

***Total: 20/30***

---

## **Chain of Thought Prompting**
```
You are a Python test generation tool. Follow each step carefully to **generate a comprehensive test suite for the provided code.**

1. **Verify Class and Function Existence**
    - Test that each function or class in the code is defined and callable.
    - Write specific tests to confirm the presence of all essential functions and classes.

2. **Test Expected Behavior**
    - Design test cases for typical inputs to check if each function performs as intended.
    - Use a variety of common input values to cover typical use cases.

3. **Include Edge Cases and Special Scenarios**
    - Add tests for unusual or extreme inputs to assess the function’s stability.
    - Verify that the function handles these cases correctly and returns the expected output.

4. **Handle Invalid Input Types**
    - Write test cases for incorrect or unsupported data types passed to the function.
    - Ensure that the function raises appropriate errors or gracefully handles these inputs.

**Output Requirements**
    - Provide clear feedback in German for each failed test, specifying what functionality is required to pass.
    - Output only the Python test suite with the defined test cases, without any additional comments or explanations beyond the test code itself.

### Code ###
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

Here is the generated test suite for the provided code:

```Python
import unittest
from your_module import calculate_mean  # Replace 'your_module' with the actual module name

class TestCalculateMean(unittest.TestCase):
    def test_function_exists(self):
        self.assertIsNotNone(calculate_mean)

    def test_empty_list(self):
        result = calculate_mean([])
        self.assertEqual(result, None)
        print("Fehler: Die Funktion sollte für eine leere Liste keinerlei Ausgabe erzeugen. Die Lösung ist die Rückgabe von 'None'.")

    def test_single_integer(self):
        result = calculate_mean([5])
        self.assertAlmostEqual(result, 5)
        print("Funktioniert: Eine einzelne Ganzzahl wird korrekt als Mittelwert zurückgegeben.")

    def test_multiple_integers(self):
        result = calculate_mean([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 3)
        print("Funktioniert: Mehrere Ganzzahlen werden korrekt als Mittelwert zurückgegeben.")

    def test_mixed_numbers(self):
        result = calculate_mean([1, 2.0, 3, 4, 5.0])
        self.assertAlmostEqual(result, 3)
        print("Funktioniert: Mischung aus Ganzzahlen und Dezimalzahlen wird korrekt als Mittelwert zurückgegeben.")

    def test_non_numeric_input(self):
        result = calculate_mean(['a', 'b', 'c'])
        self.assertEqual(result, None)
        print("Fehler: Die Funktion sollte für keine nicht-numericen Werte keinerlei Ausgabe erzeugen. Die Lösung ist die Rückgabe von 'None'.")

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            calculate_mean('not a list')
        print("Funktioniert: Die Funktion wirft einen TypeError, wenn ein nicht-Listeingabe gemacht wird.")

if __name__ == '__main__':
    unittest.main()
```

This test suite includes tests for the existence of the function, edge 
cases like an empty list or non-numeric inputs, and typical use cases with 
different types of input data.

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
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 4/10**

---

Here is the generated test suite:

```
import unittest
from your_module import calculate_mean  # Replace 'your_module' with the 
actual module name

class TestCalculateMean(unittest.TestCase):
    def test_class_and_function_presence(self):
        self.assertIsNotNone(calculate_mean)
        self.assertTrue(callable(calculate_mean))

    def test_typical_input(self):
        numbers = [1, 2, 3]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, 2.0)

    def test_empty_list(self):
        result = calculate_mean([])
        self.assertIsNone(result)

    def test_single_element(self):
        number = 5
        result = calculate_mean([number])
        self.assertAlmostEqual(result, number)

    def test_mixed_types(self):
        numbers = [1, 2.0, 3]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, 2.0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b'])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_mean({1: 2})

if __name__ == '__main__':
    unittest.main()
```

This test suite covers the expected behavior of the `calculate_mean` 
function, including typical inputs, edge cases, and invalid input types. 
The output will indicate whether each test passes or fails, with German 
feedback for failed tests specifying what functionality is required to 
pass.

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
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Bemerkungen: 
- Beinhaltet Fehler

**Punkte: 4/10**

---

Here is the comprehensive test suite for the provided code:

```
import unittest

class TestCalculateMean(unittest.TestCase):

    def test_class_definition(self):
        from calculator import calculate_mean  # assume calculator.py contains the function

    def test_function_callable(self):
        from calculator import calculate_mean
        calculate_mean([])

    def test_empty_list_return_none(self):
        from calculator import calculate_mean
        self.assertEqual(calculate_mean([]), None)

    def test_single_integer_element(self):
        from calculator import calculate_mean
        self.assertAlmostEqual(calculate_mean([42]), 42.0)

    def test_multiple_integer_elements(self):
        from calculator import calculate_mean
        self.assertAlmostEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)

    def test_mixed_type_list_invalid_input(self):
        from calculator import calculate_mean
        with self.assertRaises(TypeError):
            calculate_mean([42, 'hello'])

    def test_non_numeric_element_returns_none(self):
        from calculator import calculate_mean
        self.assertEqual(calculate_mean([1, 2, None]), None)

    def test_float_elements(self):
        from calculator import calculate_mean
        self.assertAlmostEqual(calculate_mean([1.0, 2.5, 3.25]), 2.25)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 3/10**

***Total: 11/30***

---

## **Multitask-Prompting**

```
You are a Python test generation tool. Your tasks are as follows to **create a comprehensive test suite for the provided code.** Complete each task independently, then combine all results into a single test suite.

# Task 1: Create a Complete List of Test Cases
**Goal**: Develop a list covering all necessary conditions to ensure the code functions as intended.
- Include checks for class and function existence, expected behavior for typical inputs, edge cases for unusual inputs, and error-handling tests for cases like type errors.

# Task 2: Write a Complete Test Script
**Goal**: Implement a test script that covers all test cases from Task 1.

**Output Requirements**
    - Provide clear feedback in German for each failed test, specifying what functionality is required to pass.
    - Output only the Python test suite with the defined test cases, without any additional comments or explanations beyond the test code itself.

### Code ###
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

**Task 1: Create a Complete List of Test Cases**

1. **Typical input test cases**
	* calculate_mean([1, 2, 3]): returns the correct mean (e.g., 2.0)
	* calculate_mean([10, 20, 30]): returns the correct mean (e.g., 20.0)
	* calculate_mean([-5, -10, 15]): returns the correct mean (e.g., 0.0)
2. **Edge cases**
	* calculate_mean([]): returns None
	* calculate_mean([1.5, 3.7]): returns the correct mean (e.g., 2.6)
	* calculate_mean(['a', 'b', 'c']): returns None
	* calculate_mean([None, None, None]): returns None
3. **Error-handling tests**
	* calculate_mean('not a list'): raises TypeError
	* calculate_mean({'not': 'a', 'list': 5}): raises TypeError

**Task 2: Write a Complete Test Script**

```python
import unittest

class TestCalculateMean(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(calculate_mean([1, 2, 3]), 2.0)
        self.assertAlmostEqual(calculate_mean([10, 20, 30]), 20.0)
        self.assertAlmostEqual(calculate_mean([-5, -10, 15]), 0.0)

    def test_edge_cases(self):
        self.assertIsNone(calculate_mean([]))
        self.assertAlmostEqual(calculate_mean([1.5, 3.7]), 2.6)
        self.assertIsNone(calculate_mean(['a', 'b', 'c']))
        self.assertIsNone(calculate_mean([None, None, None]))

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            calculate_mean('not a list')
        with self.assertRaises(TypeError):
            calculate_mean({'not': 'a', 'list': 5})

if __name__ == '__main__':
    unittest.main()
```

**Output Requirements**

The output will be the Python test script above, without any additional 
comments or explanations beyond the test code itself.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 4/10**

---

Here are the results of completing each task independently, followed by 
combining them into a single test suite:

**Task 1: Create a Complete List of Test Cases**

1. Class existence: `calculate_mean` function exists
2. Typical inputs:
	* Empty list: `[]`
	* Single integer: `[42]`
	* Single float: `[3.14]`
	* Mixed integers and floats: `[1, 2, 3.5, 4, 5.7]`
3. Edge cases:
	* List with non-numeric elements: `['a', 'b', 3]`
	* List with mixed numeric and non-numeric elements: `[1, 'c', 2.5, None]`
	* List with negative numbers: `[-1, -2, -3.4]`
	* List with zero: `[0, 0, 0]`
4. Error-handling tests:
	* Type error (non-list input): `calculate_mean('not a list')`
	* Value error (invalid type in the list): `calculate_mean([1, 'two', 
3.5])`

**Task 2: Write a Complete Test Script**

```
import unittest
from your_module import calculate_mean

class TestCalculateMean(unittest.TestCase):

    def test_calculate_mean_empty_list(self):
        self.assertEqual(calculate_mean([]), None)

    def test_calculate_mean_single_integer(self):
        self.assertAlmostEqual(calculate_mean([42]), 42.0)

    def test_calculate_mean_single_float(self):
        self.assertAlmostEqual(ccalculate_mean([3.14]), 3.14)

    def test_calculate_mean_mixed_int_float(self):
        self.assertAlmostEqual(calculate_mean([1, 2, 3.5, 4, 5.7]), 3.1)

    def test_calculate_mean_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b', 3])

    def test_calculate_mean_mixed_types(self):
        with self.assertRaises(TypeError):
            calculate_mean([1, 'c', 2.5, None])

    def test_calculate_mean_negative_numbers(self):
        self.assertAlmostEqual(calculate_mean([-1, -2, -3.4]), -2.233333)

    def test_calculate_mean_zero(self):
        self.assertEqual(calculate_mean([0, 0, 0]), 0.0)

    def test_calculate_mean_type_error(self):
        with self.assertRaises(TypeError):
            calculate_mean('not a list')

if __name__ == '__main__':
    unittest.main()
```

**Output Requirements**

The test script will output the results of each test case in German:
- If a test fails, it will output `Fehler: Expected output X, but got Y.`
- If all tests pass, it will output nothing (i.e., no output).

Please note that the actual output may vary based on the Python version 
and environment you're using to run the tests.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ✅
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

---

Here are the results of Tasks 1 and 2:

**Task 1: Create a Complete List of Test Cases**

```
Test cases for calculate_mean function:
- Existence check:
    - class existence (calculate_mean exists as a function)
    - function existence (calculate_mean can be called)
- Typical inputs:
    - single integer value
    - multiple integer values
    - single float value
    - multiple float values
- Edge cases:
    - empty list (return None)
    - list with all integers
    - list with all floats
    - list containing both integers and floats
    - list with non-numerical values (strings, etc.)
- Error-handling tests:
    - type error (non-list input)
    - value error (input is not a number)
```

**Task 2: Write a Complete Test Script**

```Python
import unittest

class TestCalculateMean(unittest.TestCase):

    def test_calculate_mean(self):
        self.assertIsNotNone(calculate_mean([1, 2, 3, 4, 5]))
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)

        self.assertIsNotNone(calculate_mean([1.0, 2.0, 3.0, 4.0, 5.0]))
        self.assertEqual(calculate_mean([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)

        self.assertIsNone(calculate_mean([]))
        self.assertIsNone(calculate_mean([1, 'a', 2, 3]))

        with self.assertRaises(TypeError):
            calculate_mean('test')

        with self.assertRaises(ValueError):
            calculate_mean([1, 2, 3, 'a'])

    if __name__ == '__main__':
        unittest.main()
```

This test script includes all the test cases defined in Task 1. It covers 
existence checks, typical inputs, edge cases, and error-handling tests for 
the `calculate_mean` function.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste von sehr großen Zahlen ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Bemerkungen: 
- Beinhaltet Fehler

**Punkte: 3/10**

## **Total: 12/30**

---

## **Instruction + One-Shot Prompting**


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

---

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
