import tkinter as tk
import json
import os
from tkinter import messagebox

class Prompt_Manager:
    def __init__(self, json_file="prompts.json"):
        """
        Initialisiert den PromptsManager und lädt die Prompts aus einer JSON-Datei.
        """
        self.json_file = json_file
        self.prompts = self.load_prompts()
        self.selected_prompt = tk.StringVar(value="Einfache Funktionen")
        
    def successful_save_prompt_to_json(self, title, content):
        """
        Speichert den erstellten Prompt.
        """

        # Validierung der Eingaben
        if not title:
            messagebox.showerror("Fehler", "Der Titel darf nicht leer sein.")
            return False
        if not content:
            messagebox.showerror("Fehler", "Der Prompt-Inhalt darf nicht leer sein.")
            return False

        try:
            # Prüfen, ob der Titel bereits existiert
            if title in self.prompts:
                overwrite = messagebox.askyesno(
                    "Titel überschreiben?",
                    f"Der Titel '{title}' existiert bereits. Möchtest du ihn überschreiben?"
                )
                if overwrite:
                    self.update_prompt(title, content)
                    self.selected_prompt.set(title)
                    return True
                else:
                    return False
            else:
                # Neuen Prompt hinzufügen
                self.add_prompt(title, content)
                self.selected_prompt.set(title)
                return True

        except ValueError as e:
            messagebox.showerror("Fehler", str(e))
            return False
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")
            return False

    def load_prompts(self):
        """
        Lädt die Prompts aus einer JSON-Datei.
        """
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            # Standard-Prompt, falls keine Datei existiert
            return {
                "Einfache Funktionen": {
                    "content": "You are a Python test generation tool. **Generate a detailed and comprehensive Python test suite for the provided code.** Make sure the test suite satisfies all specified requirements:\n\n### Requirements ###\n* Include test cases to verify the existence of all classes and functions, expected behavior for typical inputs, edge cases for unusual inputs, and handling of type errors.\n* Provide clear feedback in German for each failed test, specifying what functionality is required to pass.\n* Output only the complete Python test suite without any additional explanations or comments.\n\n### Here comes the code to be tested ###"
                }
            }

    def save_prompts(self):
        """
        Speichert die Prompts in einer JSON-Datei.
        """
        with open(self.json_file, "w", encoding="utf-8") as f:
            json.dump(self.prompts, f, indent=4, ensure_ascii=False)

    def get_all_prompts(self):
        """Liefert alle Prompts."""
        return self.prompts

    def add_prompt(self, title, content):
        """
        Fügt ein neues Prompt hinzu und speichert es.
        """
        if not title.strip():
            raise ValueError("Der Titel darf nicht leer sein.")
        if not content.strip():
            raise ValueError("Der Inhalt darf nicht leer sein.")
        if title in self.prompts:
            raise ValueError("Ein Prompt mit diesem Titel existiert bereits.")

        self.prompts[title] = {"content": content}
        self.save_prompts()

    def delete_prompt(self, title):
        """
        Löscht ein vorhandenes Prompt und speichert die Änderungen.
        """
        if title not in self.prompts:
            raise ValueError("Ein Prompt mit diesem Titel existiert nicht.")

        del self.prompts[title]
        self.save_prompts()
        self.selected_prompt.set("")

    def update_prompt(self, title, content):
        """
        Aktualisiert den Inhalt eines vorhandenen Prompts und speichert die Änderungen.
        """
        if title not in self.prompts:
            raise ValueError("Ein Prompt mit diesem Titel existiert nicht.")

        self.prompts[title]["content"] = content
        self.save_prompts()
