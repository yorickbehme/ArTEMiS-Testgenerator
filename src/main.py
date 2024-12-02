import tkinter as tk
from ui_testgenerator import TestGeneratorFrame
from ui_settings import SettingsFrame
from ai_generator import TestGeneratorModel
from prompts import PromptsManager


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ArTEMiS-Testgenerator")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#232323")

        # Initialisiere das TestGeneratorModel
        self.test_generator_model = TestGeneratorModel(root)
        self.prompts_manager = PromptsManager()

        # Frames initialisieren
        self.testgenerator_frame = TestGeneratorFrame(self, self.show_frame, self.test_generator_model)
        self.settings_frame = SettingsFrame(self, self.show_frame, self.prompts_manager)

        # Frames ins Grid platzieren (aber initial verstecken)
        self.testgenerator_frame.grid(row=0, column=0, sticky="nsew")
        self.settings_frame.grid(row=0, column=0, sticky="nsew")

        # Root-Layout konfigurieren
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Standardansicht anzeigen
        self.show_frame(self.testgenerator_frame)

    def show_frame(self, frame):
        """
        Blendet den angegebenen Frame ein und versteckt die anderen.
        """
        # Alle Frames verstecken
        self.testgenerator_frame.grid_remove()
        self.settings_frame.grid_remove()

        # Gewünschten Frame anzeigen
        frame.grid()
        self.root.update_idletasks()

    def start_generate_test(self):
        """
        Ruft Daten aus den Frames ab und startet die Testgenerierung.
        """
        # Zu testenden Code aus ui_testgenerator holen
        code = self.testgenerator_frame.code_text.get("1.0", tk.END).strip()

        # Einstellungen und Prompt aus ui_settings holen
        selected_prompt_title = self.settings_frame.selected_prompt_var.get()
        prompt_content = self.prompts_manager.prompts[selected_prompt_title]["content"]
        syntax_check = self.settings_frame.syntax_check_var.get()
        structure_check = self.settings_frame.structure_check_var.get()
        model_name = self.settings_frame.selected_model_var.get()

        # Callback für die Ergebnisse
        def handle_result(result):
            self.testgenerator_frame.update_output(result)

        # Generierung starten
        self.test_generator_model.generate_test(
            prompt=prompt_content,
            code=code,
            model_name=model_name,
            syntax_check=syntax_check,
            structure_check=structure_check,
            callback=handle_result
        )

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()