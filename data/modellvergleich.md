# **Modellvergleich**

Diese Analyse untersucht und vergleicht die Leistungsfähigkeit der Modelle **Mistral:7b** (lokal installiert mit Ollama) und **Llama:8b** (lokal installiert mit Ollama) bei der Testgenerierung für **komplexeren Code**. Beide Modelle werden jeweils dreimal mit einem einheitlichen **Standardprompt** getestet.

Die generierten Ergebnisse werden mit einer vordefinierten Liste von **Standard-Testfällen** abgeglichen, bewertet und in ein Punktesystem überführt. Abschließend erfolgt eine Gegenüberstellung der Ergebnisse in einer **Auswertungstabelle**, die zur besseren Übersicht am Anfang des Dokuments platziert wurde.

---

## **Auswertungstabellen**->Überarbeiten

| Test | Llama3         | GPT-4o          |
|------|----------------|-----------------|
| 1.   | 21/30 = 70%    | 30/30 = 100%    |
| 2.   | 63/90 = 70%    | 66/90 = 73,33%  |
| 3.   | 12/27 = 44,44% | 27/27 = 100%    |
| 4.   | 23/30 = 76,67% | 23/30 = 76,67%  |
| 5.   | 16/18 = 88,89% | 18/18 = 100%    |
| **Total:** | **ø 69,80%** | **ø 90%** |

---

## **Standardprompt**

```
You are a Python test generation tool. Generate a comprehensive test suite for the provided code. Ensure that you:
- Include test cases for syntax validation, class and function existence, overall behavior, type errors, and edge cases.
- Provide clear and understandable feedback in German for any failed tests.
- Output only the Python test suite without explanations or additional comments.
Code: 
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

--

## **Mistral:7b**

--- 

```python
import unittest
from typing import List, Union

class TestCalculateMeanFunction:
    def test_syntax_validation(self):
        with self.assertRaises(SyntaxError):
            exec("def calculate_mean(number_list: list:\n    length = len(number_list)\n    if length == 0:\n        return None\n    for l in number_list:\n        if type(l) != int: \n           if type(l) != float:\n               return None\n    summe = sum(number_list)\n    average = summe / length\n    return average")

    def test_class_and_function_existence(self):
        self.assertIsInstance(calculate_mean, type)
        self.assertTrue(callable(calculate_mean))

    def test_overall_behavior(self):
        self.assertEqual(calculate_mean([]), None)
        self.assertEqual(calculate_mean([1, 2, 3]), 2.0)
        self.assertEqual(calculate_mean([1.0, 2.0, 3.0]), 2.0)

    def test_type_errors(self):
        self.assertIsNone(calculate_means([]))
        with self.assertRaises(TypeError):
            calculate_mean("not a number")
        with self.assertRaises(TypeError):
            calculate_mean([1, "not a number", 3])

    def test_edge_cases(self):
        self.assertEqual(calculate_mean([0]), 0.0)
        self.assertEqual(calculate_mean([-1, 1]), 0.0)
        self.assertAlmostEqual(calculate_mean([5.0, 4.0, 3.0, 2.0, 1.0]), 3.0)

class TestDataTypes:
    def test_expected_data_types(self):
        self.assertEqual(type(calculate_mean([])), type(None))
        self.assertIsInstance(calculate_mean([1, 2, 3]), float)

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ✅
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ✅
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ✅
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ✅
8. Berechnet den Durchschnitt einer Liste mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌


**Punkte: 7/10**

---

```python
import unittest
from typing import List, Union

class TestCalculateMeanFunction:
    def test_syntax_validation(self):
        with self.assertRaises(SyntaxError):
            calculate_mean = "def calculate_mean("number_list: list):"

    def test_class_and_function_existence(self):
        with self.assertRaises(NameError):
            calculate_mean = None

    def test_empty_input(self):
        self.assertEqual(calculate_mean([]), None)

    def test_non_numeric_input(self):
        self.assertEqual(calculate_means([1, "a"]), None)

    def test_mixed_input(self):
        self.assertEqual(calculate_mean([1, 2.5, "3", 4]), None)

    def test_valid_numeric_input(self):
        self.assertAlmostEqual(calculate_means([1, 2, 3, 4]), 2.5)

    def test_single_value_input(self):
        self.assertEqual(calculate_mean([5]), 5)

    def test_multiple_same_values(self):
        self.assertAlmostEqual(calculate_means([1, 1, 1, 1]), 1)

    def test_large_input(self):
        self.assertAlmostEqual(calculate_means([1 for i in range(100)]), sum([i for i in range(1, 101)]) / 100)

class TestTypes:
    def test_list_type(self):
        self.assertIsInstance(calculate_mean([]), type(None))
        self.assertIsInstance(calculate_mean([1]), type(None))

    def test_int_or_float_elements(self):
        self.assertIsInstance(calculate_means([1, 2, 3, 4.5]), list)

class TestValues:
    def test_minimum_value(self):
        self.assertEqual(calculate_mean([-999999]), -999999)

    def test_maximum_value(self):
        self.assertEqual(calculate_mean([999999]), 999999)

if __name__ == '__main__':
    unittest.main()
```

This code provides a test suite for the `calculate_mean` function in 
Python, covering syntax validation, class and function existence, overall 
behavior, type errors, and edge cases. The tests are written using the 
built-in unittest module, and they provide clear and understandable 
feedback by raising appropriate exceptions or assertions when the provided 
function fails to meet the test conditions. All tests are written in 
English and output only the Python test suite without explanations or 
additional comments.

---

### **Auswertung**
1. "calculate_mean" Funkton existiert ❌
2. Berechnet den Durchschnitt einer Liste von positiven Ganzzahlen ✅
3. Berechnet den Durchschnitt einer Liste von negativen Ganzzahlen ❌
4. Berechnet den Durchschnitt einer Liste von positiven und negativen Ganzzahlen ❌
5. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen ❌
6. Berechnet den Durchschnitt einer Liste von Gleitkommazahlen und Ganzzahlen ❌
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Bemerkungen: 
- Viele fehlerhafte oder uneindeutige Testfälle

**Punkte: 2/10**

---

```python
import unittest
from typing import List, Union

class TestCalculateMeanFunction:
    def test_syntax_validation(self):
        self.assertRaises(SyntaxError, compile, 'calculate_mean')

    def test_class_existence(self):
        self.assertTrue(hasattr(__import__('module_name'), 'calculate_mean'))

    def test_function_existence(self):
        self.assertIsInstance(__import__('module_name').calculate_mean, type(lambda: None))

    def test_parameter_type(self):
        self.assertRaises(TypeError, calculate_mean, 1)

    def test_empty_list(self):
        self.assertEqual(calculate_mean([]), None)

    def test_integer_values(self):
        self.assertAlmostEqual(calculate_mean([1, 2, 3]), 2)

    def test_float_values(self):
        self.assertAlmostEqual(calculate_mean([1.0, 2.0, 3.0]), 2)

    def test_mixed_type_list(self):
        self.assertEqual(calculate_means([1, '2', 3]), None)

    def test_negative_values(self):
        self.assertAlmostEqual(calculate_mean([-1, -2, 3]), -0.5)

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
8. Berechnet den Durchschnitt einer Liste mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Bemerkungen: 
- Fehlerhafte Testfälle

**Punkte: 4/10**

***Total: 13/30***

---

## **Llama3:8b**

---

```
import unittest
class TestCalculateMean(unittest.TestCase):
    def test_syntax(self):
        pass  # Code compiles without syntax errors, so no tests needed

    def test_class_and_function_existence(self):
        self.assertIsNotNone(globals().get('calculate_mean'))
        self.assertIsInstance(calculate_mean, type)

    def test_positive_numbers(self):
        result = calculate_mean([1, 2, 3])
        self.assertEqual(result, 2.0)
    
    def test_zero_length_list(self):
        result = calculate_mean([])
        self.assertIsNone(result)
    
    def test_negative_numbers(self):
        result = calculate_mean([-1, -2, -3])
        self.assertEqual(result, -2.0)
    
    def test_mixed_numbers(self):
        result = calculate_mean([1, 2, -3, 4])
        self.assertEqual(result, 0.5)

    def test_floats(self):
        result = calculate_mean([1.0, 2.5, 3.75])
        self.assertAlmostEqual(result, 2.4166666666666665)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b', 'c'])
    
    def test_string_input(self):
        with self.assertRaises(TypeError):
            calculate_mean(['1', '2', '3'])

    def test_empty_string_input(self):
        result = calculate_mean(['', '', ''])
        self.assertIsNone(result)

    def test_mixed_types_input(self):
        result = calculate_mean([1, 2.0, 'a', None])
        self.assertIsNone(result)

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            calculate_mean(None)
    
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            calculate_mean('not a list')
    
if __name__ == '__main__':
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
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

---

```
import unittest

class TestCalculateMean(unittest.TestCase):
    def test_syntax_validation(self):
        self.assertIsNone(locals())

    def test_class_and_function_existence(self):
        from your_module import calculate_mean
        self.assertIsNotNone(calculate_mean)

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, 2.5)

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, -2.5)

    def test_mixed_positive_and_negative_numbers(self):
        numbers = [1, -2, 3, -4]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, -0.25)

    def test_empty_list(self):
        numbers = []
        result = calculate_mean(numbers)
        self.assertIsNone(result)

    def test_non_numeric_values(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            calculate_mean(numbers)

    def test_single_element(self):
        numbers = [5]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, 5)

    def test_two_elements(self):
        numbers = [1, 2]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, 1.5)

    def test_multiple_elements(self):
        numbers = [-10, -20, 0, 30]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, 5.0)

    def test_zero_length_list(self):
        numbers = [1] + [None] * (100 - 1)
        result = calculate_mean(numbers[:-1])
        self.assertIsNone(result)

    def test_string_value(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            calculate_mean(numbers)

    def test_float_values(self):
        numbers = [1.0, 2.5, 3.8]
        result = calculate_mean(numbers)
        self.assertAlmostEqual(result, 2.433333333333333)

if __name__ == '__main__':
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
7. Berechnet den Durchschnitt einer Liste mit 0 ❌
8. Berechnet den Durchschnitt einer Liste mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Bemerkungen: 
- Fehlerhafte Testfälle

**Punkte: 6/10**

---

```
import unittest
from calculator import calculate_mean

class TestCalculateMean(unittest.TestCase):

    def test_syntax(self):
        try:
            calculate_mean(1, 2, 3)
        except Exception as e:
            self.fail(f"Fehler bei der Syntax: {e}")

    def test_function_exists(self):
        self.assertIsNotNone(calculate_mean)

    def test_no_numbers(self):
        self.assertIsNone(calculate_mean([]))

    def test_one_number(self):
        self.assertEqual(calculate_mean([1]), 1)

    def test_multiple_numbers(self):
        self.assertAlmostEqual(calculate_mean([1, 2, 3]), 2.0)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 1, 2])

    def test_non_numeric_value(self):
        with self.assertRaises(ValueError):
            calculate_mean([1, 'b', 3])

    def test_zero_length(self):
        self.assertIsNone(calculate_mean([]))

    def test_all_strings(self):
        with self.assertRaises(TypeError):
            calculate_mean(['a', 'b', 'c'])

    def test_all_floats(self):
        self.assertAlmostEqual(calculate_mean([1.0, 2.5, 3.8]), 2.5)

    def test_mixed_types(self):
        with self.assertRaises(ValueError):
            calculate_mean([1, 'a', 2.0, 3])

if __name__ == '__main__':
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
8. Berechnet den Durchschnitt einer Liste mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für Eingaben die nicht-numerische Listen sind (z.B. Strings oder Integer) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

Bemerkungen: 
- Teilweise ungenaue Testfälle

**Punkte: 4/10**

***Total: 16/30***
