import tkinter as tk
from tkinter import scrolledtext


class UIMain(tk.Frame):
    def __init__(self, main_app, switch_frame_callback, generator_manager, prompt_manager, validator_manager):
        super().__init__(main_app.root, bg="#E0E0E0")
        self.main_app = main_app

        self.switch_frame_callback = switch_frame_callback
        self.generator_manager = generator_manager
        self.prompt_manager = prompt_manager
        self.validator_manager = validator_manager

        self.create_widgets()

    def create_widgets(self):
        """
        Erstellen der Widgets für die Hauptansicht des Testgenerators.
        """
        # Hauptinhaltsbereich
        content_frame = tk.Frame(self, bg="#E0E0E0", padx=15, pady=15)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Eingabe- und Ausgabe-Bereich in zwei Spalten teilen
        input_frame = tk.Frame(content_frame, bg="#FFFFFF", bd=1, relief="solid", padx=10, pady=10)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        output_frame = tk.Frame(content_frame, bg="#FFFFFF", bd=1, relief="solid", padx=10, pady=10)
        output_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Rahmen für die Buttons
        button_frame = tk.Frame(content_frame, bg="#E0E0E0")
        button_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0))

        # --- Eingabe-Bereich ---
        tk.Label(
            input_frame,
            text="Musterlösung",
            font=("Arial", 16, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 10))

        self.code_text = scrolledtext.ScrolledText(
            input_frame,
            wrap=tk.WORD,
            font=("Courier New", 12),
            bg="#F9F9F9",
            fg="#333333",
            relief="flat",
            borderwidth=0,
        )
        self.code_text.pack(fill=tk.BOTH, expand=True)
        self.code_text.insert(
            tk.END, "Beispiel...\ndef example_function(x):\n    return x * 2"
        )

        # --- Ausgabe-Bereich ---
        tk.Label(
            output_frame,
            text="Testskript",
            font=("Arial", 16, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 10))

        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            wrap=tk.WORD,
            font=("Courier New", 12),
            bg="#F9F9F9",
            fg="#333333",
            state=tk.DISABLED,
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        self.output_text.insert(tk.END, "Hier erscheint der generierte Testcode.")

        # --- Buttons ---
        generate_button = tk.Button(
            button_frame,
            text="Test generieren",
            command=lambda: self.generate_testscript(),
            font=("Arial", 12, "bold"),
            bg="#FFFFFF", 
            fg="#333333",
            highlightcolor="#999999",
            highlightbackground="#E0E0E0",
            width=18,
            height=2,
        )
        generate_button.grid(row=0, column=0, padx=5, pady=5)

        settings_button = tk.Button(
            button_frame,
            text="Einstellungen",
            command=lambda: self.switch_frame_callback(self.main_app.settings_frame),
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
            highlightcolor="#999999",
            highlightbackground="#E0E0E0",
            width=18,
            height=2,
        )
        settings_button.grid(row=0, column=1, padx=5, pady=5)

        # Layout-Management
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)

    def update_output(self, result):
        """
        Aktualisiert den Ausgabebereich mit dem generierten Testcode.
        """
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state=tk.DISABLED)

    def generate_testscript(self):
        """
        Überprüft die Bedingungen und startet die Testskriptgenerierung.
        """
        # Variablen für die Generierung
        code = self.code_text.get("1.0", tk.END).strip()
        selected_prompt_title = self.prompt_manager.selected_prompt.get()
        prompt_content = self.prompt_manager.prompts[selected_prompt_title]["content"]
        model_name = self.generator_manager.model_name
        is_running = self.generator_manager.is_running
        syntax_check = self.validator_manager.syntax_check_option.get()
        structure_check = self.validator_manager.structure_check_option.get()

        # Bedingungen für die Generierung prüfen
        if not self.validator_manager.are_generation_conditions_met(
            code=code,
            model_name=model_name,
            is_running=is_running,
            syntax_check=syntax_check,
            structure_check=structure_check,
        ):
            return

        self.generator_manager.is_running = True

        self.update_output("Die Testskriptgenerierung wurde erfolgreich gestartet...")

        # Callback für die Ergebnisse
        def handle_result(result):
            self.update_output(result)
            self.generator_manager.is_running = False

        # Generierung starten
        self.generator_manager.start_generate(
            prompt=prompt_content,
            code=code,
            model_name=model_name,
            callback=handle_result,
        )
