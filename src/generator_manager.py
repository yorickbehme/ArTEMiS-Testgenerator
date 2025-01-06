import subprocess
import threading
from tkinter import messagebox

class Generator_Manager:
    def __init__(self, root):
        self.root = root
        self.lock = threading.Lock()
        self.model_name = "llama3.1:8b"
        self.is_running = False
        
    def start_generate(self, prompt, code, model_name, callback=None):
        """
        Startet die Generierung des Testskripts basierend auf der eingegebenen Musterlösung.
        """
        total_prompt = f"{prompt}\n{code}"
        thread = threading.Thread(target=self._run_subprocess_generation, args=(total_prompt, model_name, callback), daemon=True)
        thread.start()

    def _run_subprocess_generation(self, total_prompt, model_name, callback):
        """
        Führt den Subprozess aus, um das Testskript zu generieren.
        """
        output = None
        try:
            result = subprocess.run(
                ["ollama", "run", model_name],
                input=total_prompt,
                capture_output=True,
                text=True
            )
            if result.returncode == 0 and result.stdout:
                output_split = result.stdout.split("```", 2)
                if len(output_split) > 2:
                    output = output_split[1].strip()
                else:
                    messagebox.showinfo("Fehler", "Ein Fehler bei der Generierung ist aufgetreten, bitte versuchen Sie es erneut.")
            else:
                error_message = result.stderr.strip() if result.stderr else "Unbekannter Fehler."
                messagebox.showinfo("Fehler", f"Fehler bei der Verbindung mit dem Modell: {error_message}")
        except subprocess.SubprocessError as e:
            messagebox.showinfo("Fehler", f"Fehler bei der Verbindung mit dem Modell: {e}")
        finally:
            self.is_running = False
            if callback:
                callback(output) 
