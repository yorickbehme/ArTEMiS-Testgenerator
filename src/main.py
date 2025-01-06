import tkinter as tk
from ui_main import UIMain
from ui_settings import UISettings
from generator_manager import Generator_Manager
from validator_manager import Validator_Manager
from prompt_manager import Prompt_Manager


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("ArTEMiS-Testskriptgenerator")
        self.root.geometry("1000x800")
        self.root.resizable(False, False)
        self.root.configure(bg="#232323")

        # Initialisiere das TestGeneratorModel
        self.generator_manager = Generator_Manager(self.root)
        self.prompt_manager = Prompt_Manager()
        self.validator_manager = Validator_Manager()

        # Frames initialisieren
        self.main_frame = UIMain(self, self.show_frame, self.generator_manager, self.prompt_manager, self.validator_manager)
        self.settings_frame = UISettings(self, self.show_frame, self.prompt_manager, self.validator_manager)

        # Frames ins Grid platzieren
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.settings_frame.grid(row=0, column=0, sticky="nsew")

        # Root-Layout konfigurieren
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Standardansicht anzeigen
        self.show_frame(self.main_frame)

    def show_frame(self, frame):
        """
        Blendet den angegebenen Frame ein und versteckt die anderen.
        """
        # Alle Frames verstecken
        self.main_frame.grid_remove()
        self.settings_frame.grid_remove()

        # Gewünschten Frame anzeigen
        frame.grid()
        self.root.update_idletasks()

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()