import subprocess
import threading


class TestGeneratorModel:
    def generate_test_code_with_llama(self, code, model_name, callback=None):
        """
        Startet die Generierung eines Testcodes für den bereitgestellten Python-Code
        unter Verwendung des angegebenen Modells.

        Args:
            code (str): Der Python-Code, für den Tests generiert werden sollen.
            model_name (str): Der Name des zu verwendenden Modells.
            callback (function, optional): Eine Funktion, die mit dem generierten
                Testcode aufgerufen wird. Standard ist None.
        """
        def worker():
            """
            Arbeiterfunktion, die den Testcode generiert und das Ergebnis
            über den Callback zurückgibt.
            """
            # Erstellen des Prompts für das Modell
            prompt = f'''You are a Python test generation tool. **Generate a detailed and comprehensive Python test suite for the provided code.** Make sure the test suite aligns with the given examples and satisfies all specified requirements:

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
{code}'''
            try:
                result = subprocess.run(
                    ["ollama", "run", model_name, prompt],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    output = result.stdout.strip()
                    # Extrahieren des relevanten Teils der Ausgabe
                    output = output.split("```", 2) 
                    if len(output) > 2:
                        output = output[1].strip()  
                    else:
                        output = "Ein Fehler bei der Erstellung ist Aufgetretten, bitte versuchen Sie es erneut."
                else:
                    output = "Fehler beim Abrufen der Antwort vom Modell."
            except subprocess.SubprocessError as e:
                output = f"Fehler bei der Verbindung mit dem Llama-Modell: {e}"
            
            # Callback aufrufen, falls vorhanden
            if callback:
                callback(output)
        # Starten des Worker-Threads
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
    