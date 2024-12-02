import json
import os

class PromptsManager:
    def __init__(self, json_file="prompts.json"):
        """
        Initialisiert den PromptsManager und lädt die Prompts aus einer JSON-Datei.
        """
        self.json_file = json_file
        self.prompts = self.load_prompts()

    def load_prompts(self):
        """
        Lädt die Prompts aus einer JSON-Datei.
        """
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            # Standard-Prompts, falls keine Datei existiert
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
        print("Prompts erfolgreich gespeichert.")

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
        print(f"Prompt '{title}' erfolgreich hinzugefügt.")

    def delete_prompt(self, title):
        """
        Löscht ein vorhandenes Prompt und speichert die Änderungen.
        """
        if title not in self.prompts:
            raise ValueError("Ein Prompt mit diesem Titel existiert nicht.")

        del self.prompts[title]
        self.save_prompts()
        print(f"Prompt '{title}' erfolgreich gelöscht.")

    def update_prompt(self, title, content):
        """
        Aktualisiert den Inhalt eines vorhandenen Prompts und speichert die Änderungen.
        """
        if title not in self.prompts:
            raise ValueError("Ein Prompt mit diesem Titel existiert nicht.")

        self.prompts[title]["content"] = content
        self.save_prompts()
        print(f"Prompt '{title}' erfolgreich aktualisiert.")
