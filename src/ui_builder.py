import tkinter as tk
from tkinter import messagebox, scrolledtext
from ai_generator import TestGeneratorModel
from validator import CodeValidator
from ui_elements import RoundedButton

class TestGeneratorUI:
    def __init__(self, root):
        """
        Initialisiert die Hauptkomponenten der Benutzeroberfläche.
        """
        self.ai_gen = TestGeneratorModel()
        self.validator = CodeValidator()
        self.syntax_check_var = tk.BooleanVar(value=True)
        self.generation_is_running = False

        self.root = root
        self.root.title("ArTEMiS-Testgenerator")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#232323")
        self.create_interface()

    def create_interface(self):
        """
        Erstellt die Benutzeroberfläche mit allen notwendigen Widgets.
        """
        # Label für den Eingabebereich
        code_label = tk.Label(
            self.root, text="Musterlösung", font=("Arial", 20, "bold"),
            bg="#232323", fg="#f0f0f0"
        )
        code_label.grid(row=0, column=0, padx=20, pady=0, sticky="w")

        # Label für den Ausgabebereich
        testcode_label = tk.Label(
            self.root, text="Testcode", font=("Arial", 20, "bold"),
            bg="#232323", fg="#f0f0f0"
        )
        testcode_label.grid(row=0, column=1, padx=20, pady=0, sticky="w")

        # Rahmen für Eingabe und Einstellungen
        sub_frame = tk.Frame(self.root, bg="#373737", bd=1, relief="flat")
        sub_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Eingabebereich für den Quellcode
        code_frame = tk.Frame(sub_frame, bg="#373737", bd=1, relief="flat")
        code_frame.grid(row=0, column=0, sticky="nsew")
        self.code_text = tk.Text(
            code_frame, wrap=tk.WORD, font=("Arial", 14),
            bg="#232323", fg="#f0f0f0", insertbackground="#f0f0f0"
        )
        self.code_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Rahmen für Einstellungen und Buttons
        settings_frame = tk.Frame(sub_frame, bg="#373737")
        settings_frame.grid(row=1, column=0, pady=10, sticky="ew")

        # Button zur Starten der Testgenerierung
        RoundedButton(
            parent=settings_frame,
            text="Testgenerierung starten",
            radius=14,
            bg="#2D2D2D",
            fg="white",
            font=("Arial", 14, "bold"),
            command=self.start_generation,
            width=200,
            height=50
        )

        # Checkbox für die Syntax- und Strukturprüfung
        syntax_check_option = tk.Checkbutton(
            settings_frame, text="Syntax und Struktur Prüfung",
            font=("Arial", 10), bg="#373737", fg="#f0f0f0",
            relief="raised", variable=self.syntax_check_var
        )
        syntax_check_option.grid(row=1, column=2, padx=10, pady=5)

        # Ausgabebereich für den generierten Testcode
        testcode_frame = tk.Frame(self.root, bg="#373737", bd=2, relief="flat")
        testcode_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")
        self.output_text = scrolledtext.ScrolledText(
            testcode_frame, wrap=tk.WORD, font=("Arial", 14),
            bg="#232323", fg="#f0f0f0"
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.output_text.config(state=tk.DISABLED)

        # Layout-Konfiguration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        sub_frame.grid_columnconfigure(0, weight=1)
        sub_frame.grid_rowconfigure(0, weight=1)

        settings_frame.grid_columnconfigure(0, weight=1)
        settings_frame.grid_columnconfigure(1, weight=1)
        settings_frame.grid_columnconfigure(2, weight=1)

    def start_generation(self):
        """
        Startet die Generierung des Testcodes basierend auf der eingegebenen Musterlösung.
        """
        if self.generation_is_running:
            return
        self.generation_is_running = True
        print("Testgenerierung wird gestartet...")
        code = self.code_text.get("1.0", tk.END).strip()

        if self.syntax_check_var.get():
            print("Syntax und Struktur Prüfung wird durchgeführt...")
            if not self.validator.is_syntax_valid(code):
                messagebox.showerror(
                    "Fehler",
                    "Der Code enthält einen Syntaxfehler. Soll die Testgenerierung dennoch gestartet werden, deaktivieren Sie die 'Syntax und Struktur Prüfung'."
                )
                self.generation_is_running = False
                return
            if not self.validator.has_testable_structures(code):
                messagebox.showerror(
                    "Fehler",
                    "Der Code enthält keine testbaren Strukturen. Soll die Testgenerierung dennoch gestartet werden, deaktivieren Sie die 'Syntax und Struktur Prüfung'."
                )
                self.generation_is_running = False
                return
            print("Syntax und Struktur Prüfung abgeschlossen.")

        # Aktualisierung des UI-Status
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Testgenerierung läuft, bitte warten...")
        self.output_text.config(state=tk.DISABLED)

        # Start der Testcode-Generierung
        self.ai_gen.generate_test_code_with_llama(
            code,
            "llama3:latest",
            callback=self.update_output
        )

    def update_output(self, result):
        """
        Aktualisiert den Ausgabebereich mit dem generierten Testcode.
        """
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state=tk.DISABLED)
        self.generation_is_running = False
        print("Testgenerierung abgeschlossen.")
