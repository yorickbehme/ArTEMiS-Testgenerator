import tkinter as tk
import ast
import subprocess
from tkinter import messagebox

class Validator_Manager:
    def __init__(self):
        self.syntax_check_option = tk.BooleanVar(value=True)
        self.structure_check_option = tk.BooleanVar(value=True)

    def are_generation_conditions_met(self, code, model_name, is_running=True, syntax_check=True, structure_check=True):
        """
        Prüft ob die Bedingungen für die Generierung eines Testskripts erfüllt sind.
        """
        if is_running:
            messagebox.showinfo("Generierung läuft", "Testskriptgenerierung läuft bereits, bitte warten Sie.")
            return False
        
        if not self.is_model_available(model_name):
            return False

        if not code.strip():
            messagebox.showerror("Fehler", "Die Musterlösung darf nicht leer sein. Bitte geben Sie eine Musterlösung ein.")
            return False

        if syntax_check and not self.is_syntax_valid(code):
            messagebox.showerror("Fehler", "Der eingegebene Code enthält Syntaxfehler, bitte korrigieren Sie diese oder deaktivieren Sie die Syntaxprüfung.")
            return False

        if structure_check and not self.has_testable_structures(code):
            messagebox.showerror("Fehler", "Der eingegebene Code enthält keine klassisch testbaren Strukturen (Funktionen oder Klassen), wenn Sie die Generierung dennoch starten möchten, deaktivieren Sie die Strukturprüfung.")
            return False
        
        else:
            return True

    def is_syntax_valid(self, code):
        """
        Überprüft, ob der Code syntaktisch korrekt ist.
        """
        try:
            compile(code, "<string>", "exec")
            return True
        except SyntaxError:
            return False

    def has_testable_structures(self, code):
        """
        Überprüft, ob der Code Funktionen oder Klassen enthält.
        """
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    return True
            return False
        except SyntaxError:
            return False
        
    def is_model_available(self, model_name):
        """
        Prüft, ob das angegebene Modell mit Ollama installiert und verfügbar ist.
        """
        try:
            result = subprocess.run(
                ["ollama", "list"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )
            if model_name in result.stdout:
                return True
            else:
                messagebox.showerror("Fehler", "Ollama oder das Modell ("+ model_name +") ist nicht installiert oder nicht im PATH verfügbar. Bitte versichern Sie sich, dass sowohl Ollama als auch das Modell installiert sind.")
                return False
        except FileNotFoundError:
            messagebox.showerror("Fehler", "Ollama oder das Modell ("+ model_name +") ist nicht installiert oder nicht im PATH verfügbar. Bitte versichern Sie sich, dass sowohl Ollama als auch das Modell installiert sind.")
            return False
