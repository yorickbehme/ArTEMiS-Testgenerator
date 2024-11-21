# **Modelluntersuchung**

In dieser Analyse werden verschiedene **KI-Modelle** systematisch auf ihre Leistungsfähigkeit bei der Testgenerierung untersucht. Hierzu wurde jedes Modell dreimal mit einem einheitlichen **Standardprompt** getestet.

Die generierten Ergebnisse wurden mit einer vordefinierten Liste von **Standard-Testfällen** abgeglichen, bewertet und in ein Punktesystem überführt. Die abschließende Gegenüberstellung der Ergebnisse erfolgt in einer **Auswertungstabelle**, die zur besseren Übersicht am Anfang des Dokuments platziert ist.

---

## **Auswertungstabellen**->Überarbeiten

| **Modell**           | **Iteration 1** | **Iteration 2** | **Iteration 3** | **Total** | **Prozent** |
|-----------------------|------------|------------|------------|-----------|-------------|
| **Mistral**          | 5/10       | 6/10       | 6/10       | 17/30     | 56,67%      |
| **Llama3**           | 6/10       | 6/10       | 6/10       | 18/30     | 60,00%      |
| **CodeLlama**        | 5/10       | 4/10       | 4/10       | 13/30     | 43,33%      |
| **StarCoder2**       | 0/10       | 0/10       | 0/10       | 0/30      | 0,00%       |
| **Gemma2**           | 4/10       | 4/10       | 4/10       | 12/30     | 40,00%      |
| **CodeGemma**        | 5/10       | 5/10       | 5/10       | 15/30     | 50,00%      |
| **Gemini 1.5 Flash** | 6/10       | 6/10       | 7/10       | 19/30     | 63,33%      |
| **GPT-4o**           | 7/10       | 7/10       | 8/10       | 22/30     | 73,33%      |

---

## **Standardprompt**

```
You are a Python test generation tool. Generate a comprehensive test suite for the provided code. Ensure that you:
- Include test cases for syntax validation, class and function existence, overall behavior, and edge cases.
- Output only the Python test suite without explanations or additional comments.
Code: 
def add(a, b):
    return a+b
```

---

## **KI-Modelle**
1. mistral:7b
2. llama3:8b
3. codellama:7b
4. starcoder2:7b
5. gemma2:9b
6. codegemma:7b
7. Gemini 1.5 flash
8. ChatGPT 4o

## **Mistral**

---

```python
import unittest
from your_module import add

class TestAddFunction(unittest.TestCase):
    def test_syntax_validation(self):
        self.assertIsInstance(add, type)

    def test_class_and_function_existence(self):
        self.assertTrue(hasattr(your_module, 'add'))

    def test_basic_behavior(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(add(sys.maxsize, 1), sys.maxsize + 1)
        self.assertEqual(add(-sys.maxsize - 1, -1), -sys.maxsize - 2)
        self.assertEqual(add(-sys.maxsize, sys.maxsize), 0)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

---

```python
import unittest
from your_module import add  # replace 'your_module' with the appropriate 
module name

class TestAddFunction(unittest.TestCase):
    def test_syntax_validation(self):
        self.assertRaises(TypeError, add)
        self.assertRaises(TypeError, add, 1, "not a number")
        self.assertRaises(TypeError, add, None, 2)
        self.assertIsInstance(add(1, 2), int)

    def test_class_and_function_existence(self):
        self.assertIsNotNone(add)
        self.assertTrue(callable(add))

    def test_behavior(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(99999, 1), 100000)
        self.assertEqual(add(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(add(-100000, 1), -99999)
        self.assertEqual(add(sys.maxsize, 1), sys.maxsize + 1)
        self.assertEqual(add(sys.maxsize, -1), sys.maxsize - 1)
        self.assertEqual(add(-sys.maxsize, -1), -sys.maxsize + 1)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ❌
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

---

```python
import unittest
from your_module import add

class TestAddFunction(unittest.TestCase):
    def test_syntax_validation(self):
        self.assertIsInstance(add, type)

    def test_function_existence(self):
        self.assertTrue(callable(add))

    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 4), 14)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, -4), -14)

    def test_zero(self):
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(4, 0), 4)

    def test_float_numbers(self):
        self.assertAlmostEqual(add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(add(-2.5, -3.7), -6.2)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            add('str', 4)
        with self.assertRaises(TypeError):
            add(4, 'str')

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

***Total: 17/30**

---

Llama3:8b

---

```
import unittest
class TestAddFunction(unittest.TestCase):
    def test_syntax(self):
        self.assertIsNotNone(add)

    def test_class_existence(self):
        self.assertIs(type(add), type((lambda x: None)))

    def test_function_type(self):
        self.assertIsInstance(add, type(abs))

    def test_valid_input(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_invalid_input_type_integer(self):
        with self.assertRaises(TypeError):
            add('a', 2)
        with self.assertRaises(TypeError):
            add(1, 'b')

    def test_invalid_input_type_non_numeric(self):
        with self.assertRaises(TypeError):
            add(None, None)
        with self.assertRaises(TypeError):
            add([], [])
        with self.assertRaises(TypeError):
            add({}, {})

    def test_edge_case_negative_numbers(self):
        self.assertEqual(add(-10, 2), -8)
        self.assertEqual(add(0, -1), -1)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

---

```
import unittest
class TestAddFunction(unittest.TestCase):

    def test_syntax(self):
        pass

    def test_class_and_function_existence(self):
        self.assertIsNotNone(add)
        self.assertTrue(callable(add))

    def test_addition(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(0, 0), 0)

    def test_edge_cases(self):
        self.assertRaises(TypeError, add, 'a', 2)
        self.assertRaises(TypeError, add, 2, 'b')
        self.assertEqual(add(None, None), None)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

---

```
import unittest
class TestAddFunction(unittest.TestCase):

    def test_syntax(self):
        self.assertEqual(add("hello", 5), None)

    def test_function_exists(self):
        self.assertIsNotNone(add)
    
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)

    def test_edge_case_zero(self):
        self.assertEqual(add(-1,0),-1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(add(-5,-7), -12)

    def test_edge_case_large_integers(self):
        self.assertEqual(add(100000,200000), 300000)

    def test_edge_case_floating_point(self):
        self.assertAlmostEqual(add(0.1, 2.3), 2.4)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

***Total: 18/30***

---

## **codellama**

---

import unittest

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4)

    def test_add_mixed(self):
        self.assertEqual(add(1, 2.0), 3.0)

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add('a', 'b')

    def test_add_value_error(self):
        with self.assertRaises(ValueError):
            add('a', 1)

if __name__ == '__main__':
    unittest.main()

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Addiert eine Ganzzahl mit 0 ❌
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

---

import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_float_numbers(self):
        self.assertEqual(add(1.5, 2.5), 4)

    def test_add_string(self):
        with self.assertRaises(TypeError):
            add("hello", "world")

    def test_add_none(self):
        with self.assertRaises(TypeError):
            add(None, None)

if __name__ == '__main__':
    unittest.main()

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ❌
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 4/10**

---

```
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6, places=1)

    def test_add_with_strings(self):
        with self.assertRaises(TypeError):
            add("hello", "world")

class TestAddClass(unittest.TestCase):
    def setUp(self):
        self.adder = add

    def test_add_two_numbers(self):
        self.assertEqual(self.adder(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.adder(-2, -3), -5)

    def test_add_floats(self):
        self.assertAlmostEqual(self.adder(2.5, 3.5), 6, places=1)

    def test_add_with_strings(self):
        with self.assertRaises(TypeError):
            self.adder("hello", "world")

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ❌
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 4/10**

***Total: 13/30***

---

## **StarCoder2**

---

def is_even(x):
    return x % 2 == 0
###Punkte: 0

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ❌
3. Addiert zwei negative Ganzzahlen ❌
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ❌
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 0/10**

---

Test:
add(1, 2) == 3
add(256, 257) == 513
add('a', 'b') == 'ab'


Example
Input: 
def add(a, b):
    return a+b

Output:
add(1, 2) == 3
add(256, 257) == 513
add('a', 'b') == 'ab'
###Punkte: 0

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ❌
3. Addiert zwei negative Ganzzahlen ❌
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ❌
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 0/10**

---

Testing criteria (10 points):
- Validate that a function is syntactically correct (use `exec` and 
`compile`)
- Validate that a function exists
- Validate the output of a function (e.g., a+b=3)
- Validate a range of inputs for the function, e.g., 0 + 1 = 1
- Output the test case as you see fit. E.g., `add(1,2)` or `add(a=1, 
b=2)`.

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ❌
3. Addiert zwei negative Ganzzahlen ❌
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ❌
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 0/10**

***Total: 0/30***

---

## **gemme2**

---

```python
import unittest

class TestAdd(unittest.TestCase):
    def test_syntax(self):
        assert "def add(a, b):" in globals()

    def test_function_exists(self):
        assert callable(globals()['add'])

    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_float_numbers(self):
        self.assertEqual(add(2.5, 3.7), 6.2)

if __name__ == '__main__':
    unittest.main()  
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 4/10**

---

2. ###
```python
import unittest

class TestAdd(unittest.TestCase):

    def test_syntax(self):
        pass

    def test_add_existence(self):
        self.assertTrue(hasattr(globals(), 'add'))

    def test_add_function(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_add_edge_cases(self):
        self.assertEqual(add(float('inf'), 1), float('inf'))
        self.assertEqual(add(-float('inf'), -1), -float('inf'))



if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ❌
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 4/10**

---

```python
import unittest

class TestAdd(unittest.TestCase):

    def test_syntax(self):
        exec("def add(a, b): return a + b")

    def test_function_existence(self):
        with self.assertRaises(NameError):
            globals().pop('add', None)
        
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_float_numbers(self):
        self.assertEqual(add(2.5, 3.7), 6.2)


if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 4/10**

***Total: 12/30***

---

## **codegemma**

---

```python
import unittest

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_float(self):
        self.assertEqual(add(2.5, 3.5), 6)

    def test_add_non_numeric_types(self):
        with self.assertRaises(TypeError):
            add("a", "b")

    def test_add_missing_arguments(self):
        with self.assertRaises(TypeError):
            add(2)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

---

```python
import unittest

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_non_numeric_values(self):
        with self.assertRaises(TypeError):
            add('a', 'b')

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

---

```python
import unittest

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_none(self):
        self.assertRaises(TypeError, add, None, 3)

    def test_add_empty_string(self):
        self.assertRaises(TypeError, add, "", 3)

    def test_add_list(self):
        self.assertRaises(TypeError, add, [1, 2], 3)

    def test_add_dictionary(self):
        self.assertRaises(TypeError, add, {1: 2}, 3)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ❌
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ❌
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 5/10**

***Total: 15/30***

---

## **gemini 1.5 Flash**

---

import unittest

class TestAddFunction(unittest.TestCase):

    def test_add_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_integers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_signs(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 999999), 1999999)

    def test_add_floating_point_numbers(self):
        self.assertAlmostEqual(add(1.23, 4.56), 5.79, places=2)

if __name__ == '__main__':
    unittest.main()

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

---

import unittest

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_signs(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_float_numbers(self):
        self.assertEqual(add(2.5, 3.7), 6.2)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 999999), 1999999)

if __name__ == '__main__':
    unittest.main()

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ❌
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 6/10**

---

import unittest

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_signs(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_float_numbers(self):
        self.assertEqual(add(2.5, 3.7), 6.2)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_string_input(self):
        with self.assertRaises(TypeError):
            add("hello", "world")

if __name__ == '__main__':
    unittest.main()

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 7/10**

***Total: 19/30***

---

## **GPT-4o**

---

```python
import unittest

class TestAddFunction(unittest.TestCase):
    
    def test_function_exists(self):
        self.assertTrue(callable(add), "Function 'add' does not exist")
    
    def test_syntax_validation(self):
        try:
            compile("def add(a, b): return a+b", '<string>', 'exec')
        except SyntaxError:
            self.fail("Syntax error in function 'add'")

    def test_addition(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(-1.5, 1.5), 0.0)
    
    def test_edge_cases(self):
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(float('inf'), 1), float('inf'))
        self.assertEqual(add(1, float('inf')), float('inf'))
        self.assertTrue(add(float('inf'), float('-inf')), "Expected NaN or undefined")

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            add("a", "b")
        with self.assertRaises(TypeError):
            add(None, 1)
        with self.assertRaises(TypeError):
            add(1, None)
        with self.assertRaises(TypeError):
            add([1, 2], [3, 4])

if __name__ == "__main__":
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 7/10**

---

import unittest

class TestAddFunction(unittest.TestCase):

    def test_add_exists(self):
        # Check if the function `add` exists
        self.assertTrue(callable(add))

    def test_add_basic(self):
        # Basic test cases
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

    def test_add_floats(self):
        # Test with float values
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(-1.5, -2.5), -4.0)

    def test_add_strings(self):
        # Test with string inputs
        self.assertEqual(add("hello ", "world"), "hello world")
        self.assertEqual(add("foo", "bar"), "foobar")

    def test_add_lists(self):
        # Test with list inputs
        self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(add([], [1, 2]), [1, 2])

    def test_add_tuples(self):
        # Test with tuple inputs
        self.assertEqual(add((1, 2), (3, 4)), (1, 2, 3, 4))
        self.assertEqual(add((), (1, 2)), (1, 2))

    def test_add_edge_cases(self):
        # Test with edge cases
        self.assertEqual(add(float('inf'), 1), float('inf'))
        self.assertEqual(add(float('-inf'), -1), float('-inf'))
        self.assertTrue(isinstance(add(None, None), type(None)))

    def test_add_invalid_type(self):
        # Test with invalid types
        with self.assertRaises(TypeError):
            add(1, "a")
        with self.assertRaises(TypeError):
            add("a", 1)
        with self.assertRaises(TypeError):
            add([1, 2], 3)
        with self.assertRaises(TypeError):
            add(3, [1, 2])

if __name__ == "__main__":
    unittest.main()

---

### **Auswertung**
1. "add" Funkton existiert ✅
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ❌
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ❌
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 7/10**

---

```python
import unittest

class TestAddFunction(unittest.TestCase):

    def test_add_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_integers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_positive_and_negative_integers(self):
        self.assertEqual(add(5, -3), 2)

    def test_add_zero_and_integer(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)
        self.assertAlmostEqual(add(-2.5, -3.1), -5.6)

    def test_add_float_and_integer(self):
        self.assertAlmostEqual(add(3, 2.5), 5.5)
        self.assertAlmostEqual(add(2.5, 3), 5.5)

    def test_add_large_numbers(self):
        self.assertEqual(add(1_000_000, 2_000_000), 3_000_000)
        self.assertEqual(add(-1_000_000, -2_000_000), -3_000_000)

    def test_add_edge_cases(self):
        self.assertEqual(add(float('inf'), 1), float('inf'))
        self.assertEqual(add(-float('inf'), 1), -float('inf'))
        self.assertTrue(math.isnan(add(float('nan'), 1)))

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add("a", 1)
        with self.assertRaises(TypeError):
            add(1, "b")
        with self.assertRaises(TypeError):
            add(None, 1)
        with self.assertRaises(TypeError):
            add(1, None)

if __name__ == '__main__':
    unittest.main()
```

---

### **Auswertung**
1. "add" Funkton existiert ❌
2. Addiert zwei positive Ganzzahlen ✅
3. Addiert zwei negative Ganzzahlen ✅
4. Addiert eine positive und eine negative Ganzzahlen ✅
5. Addiert zwei Gleitkommazahlen ✅
6. Addiert eine Gleitkommazahl und eine Ganzzahl ✅
7. Addiert eine Ganzzahl mit 0 ✅
8. Addiert mit einer sehr großen Zahl ✅
9. Wirft einen Typfehler für nicht-numerische Eingaben (z.B. Zeichenkette oder Liste) ✅
10. Gibt Sinnvolles Feedback für nichterfüllte Testfälle ❌

**Punkte: 8/10**

***Total: 22/30***
