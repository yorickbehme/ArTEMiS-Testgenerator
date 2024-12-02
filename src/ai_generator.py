import subprocess
import threading
from validator import CodeValidator


class TestGeneratorModel:
    def __init__(self, root):
        self.root = root
        self.generation_is_running = False
        self.validator = CodeValidator()
        self.lock = threading.Lock()

    def generate_test(self, prompt, code, model_name, syntax_check=True, structure_check=True, callback=None):
        """
        Startet die Generierung des Testcodes basierend auf der eingegebenen Musterlösung.
        """
        output = None  # Variable für Fehlerausgabe

        with self.lock:
            if self.generation_is_running:
                if callback:
                    callback("generation_running")
                return
            self.generation_is_running = True

        try:
            # Fehlerprüfung vor dem Start des Workers
            if not code.strip():
                output = "empty_code"
            elif syntax_check and not self.validator.is_syntax_valid(code):
                output = "syntax_error"
            elif structure_check and not self.validator.has_testable_structures(code):
                output = "structure_error"

            if output:
                # Fehler gefunden, zurücksetzen und Ergebnis übergeben
                with self.lock:
                    self.generation_is_running = False
                if callback:
                    callback(output)
                return

            def worker():
                """
                Arbeiterfunktion, die den Testcode generiert und das Ergebnis
                über den Callback zurückgibt.
                """
                nonlocal output  # Variable für Fehlerausgabe
                try:
                    # Erstellen des Prompts für das Modell
                    total_prompt = prompt + "\n" + code
                    result = subprocess.run(
                        ["ollama", "run", model_name, total_prompt],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        output = result.stdout.strip()
                        output_parts = output.split("```", 2)
                        if len(output_parts) > 2:
                            output = output_parts[1].strip()
                            if not self.validator.is_syntax_valid(output):
                                output = "Der generierte Testcode enthält Syntaxfehler, bitte überprüfen Sie die Ausgabe des Modells manuell." + "\n\n" + output
                        else:
                            output = "Ein Fehler bei der Erstellung ist aufgetreten, bitte versuchen Sie es erneut."
                    else:
                        output = "Fehler beim Abrufen der Antwort vom Modell."
                except subprocess.SubprocessError as e:
                    output = f"Fehler bei der Verbindung mit dem Modell: {e}"
                finally:
                    # Zurücksetzen des Flags und Callback-Aufruf
                    with self.lock:
                        self.generation_is_running = False
                    if callback and output is not None:
                        callback(output)

            # Starten des Worker-Threads
            thread = threading.Thread(target=worker, daemon=True)
            thread.start()

        except Exception as e:
            # Sicherstellen, dass `generation_is_running` korrekt zurückgesetzt wird
            with self.lock:
                self.generation_is_running = False
            print(f"Unbekannter Fehler: {e}")
            if callback:
                callback(f"unexpected_error: {e}")
