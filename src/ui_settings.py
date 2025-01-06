import tkinter as tk
from tkinter import ttk, scrolledtext


class UISettings(tk.Frame):
    def __init__(self, main_app, switch_frame_callback, prompt_manager, validator_manager):
        super().__init__(main_app.root, bg="#E0E0E0")
        self.main_app = main_app
        self.prompt_manager = prompt_manager
        self.validator_manager = validator_manager

        self.switch_frame_callback = switch_frame_callback
        self.initial_prompt = (
            "You are a Python test generation tool. **Generate a detailed and comprehensive "
            "Python test suite for the provided code.** Make sure the test suite aligns with the "
            "given examples and satisfies all specified requirements:\n\n### Requirements ###\n"
            "* Include test cases to verify the existence of all classes and functions, "
            "expected behavior for typical inputs, edge cases for unusual inputs, and handling "
            "of type errors.\n* Provide clear feedback in German for each failed test, specifying "
            "what functionality is required to pass.\n* Output only the complete Python test suite "
            "without any additional explanations or comments.\n\n### Example ###\n```\n\n```\n"
            "### Here comes the code to be tested ###"
        )

        self.create_widgets()

    def create_widgets(self):
        """
        Erstellt die Widgets für die Einstellungsansicht.
        """
        # Hauptinhaltsbereich
        content_frame = tk.Frame(self, bg="#E0E0E0", padx=15, pady=15)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Einstellungen und Prompt-Erstellung in zwei Spalten aufteilen
        settings_frame = tk.Frame(content_frame, bg="#FFFFFF", bd=1, relief="solid", padx=10, pady=10)
        settings_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        prompt_frame = tk.Frame(content_frame, bg="#FFFFFF", bd=1, relief="solid", padx=10, pady=10)
        prompt_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Rahmen für die Buttons
        button_frame = tk.Frame(content_frame, bg="#E0E0E0")
        button_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0))

        # --- Einstellungen-Bereich ---
        tk.Label(
            settings_frame,
            text="Einstellungen",
            font=("Arial", 16, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 30))

        tk.Label(
            settings_frame,
            text="Prompt auswählen:",
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 5))
        
        self.prompt_selector = ttk.Combobox(
            settings_frame,
            textvariable=self.prompt_manager.selected_prompt,
            values=list(self.prompt_manager.prompts.keys()),
            state="readonly",
        )
        self.prompt_selector.pack(fill=tk.X, pady=40)

        tk.Label(
            settings_frame,
            text="Syntaxprüfung:",
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 5))

        syntax_check_option = tk.Checkbutton(
            settings_frame,
            text="aktivieren",
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#333333",
            variable=self.validator_manager.syntax_check_option,
        )
        syntax_check_option.pack(anchor="w", pady=40)

        tk.Label(
            settings_frame,
            text="Strukturprüfung:",
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 5))

        structure_check_option = tk.Checkbutton(
            settings_frame,
            text="aktivieren",
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#333333",
            variable=self.validator_manager.structure_check_option,
        )
        structure_check_option.pack(anchor="w", pady=40)

        tk.Label(
            settings_frame,
            text="Ausgewählten Prompt löschen:",
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 5))

        delete_prompt_button = tk.Button(
            settings_frame,
            text="Löschen",
            command=lambda: self.delete(),
            font=("Arial", 12, "bold"),
            bg="#FF6B6B",
            fg="#333333",
            highlightbackground="#FFFFFF",
        )
        delete_prompt_button.pack(fill=tk.X, pady=40)

        # --- Prompt-Erstellungs-Bereich ---
        tk.Label(
            prompt_frame,
            text="Prompt erstellen",
            font=("Arial", 16, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=(0, 10))

        tk.Label(
            prompt_frame,
            text="Titel:",
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=5)

        self.prompt_titel_text = tk.Entry(
            prompt_frame,
            font=("Arial", 12),
            bg="#F9F9F9",
            fg="#333333",
            highlightbackground="#FFFFFF",
        )
        self.prompt_titel_text.pack(fill=tk.X, pady=5)

        tk.Label(
            prompt_frame,
            text="Prompt-Text:",
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
        ).pack(anchor="w", pady=5)

        self.prompt_text = scrolledtext.ScrolledText(
            prompt_frame,
            wrap=tk.WORD,
            font=("Courier New", 12),
            bg="#F9F9F9",
            fg="#333333",
        )
        self.prompt_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.prompt_text.insert("1.0", self.initial_prompt)

        # --- Buttons ---
        save_prompt_button = tk.Button(
            button_frame,
            text="Prompt speichern",
            command=lambda: self.save_prompt(),
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
            highlightcolor="#999999",
            highlightbackground="#E0E0E0",
            width=18,
            height=2,
        )
        save_prompt_button.grid(row=0, column=0, padx=5, pady=5)

        back_button = tk.Button(
            button_frame,
            text="Zurück",
            command=lambda: self.switch_frame_callback(self.main_app.main_frame),
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg="#333333",
            highlightcolor="#999999",
            highlightbackground="#E0E0E0",
            width=18,
            height=2,
        )
        back_button.grid(row=0, column=1, padx=5, pady=5)

        # Layout-Management
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)

    def update_prompt_selection(self):
        """
        Aktualisiert die Auswahlmöglichkeiten für die Prompts.
        """
        self.prompt_selector["values"] = list(self.prompt_manager.prompts.keys())

    def save_prompt(self):
        """
        Speichert den erstellten Prompt.
        """
        title = self.prompt_titel_text.get()
        content = self.prompt_text.get("1.0", tk.END).strip()
        # Update Promptvorlage, für erfolgreihe Erstellung
        is_successful = self.prompt_manager.successful_save_prompt_to_json(title, content)
        if is_successful:
            self.prompt_titel_text.delete(0, tk.END)
            self.prompt_text.insert("1.0", self.initial_prompt)
        self.update_prompt_selection()

    def delete(self):
        """
        Löscht den aktuell ausgewählten Prompt.
        """
        self.prompt_manager.delete_prompt(self.prompt_selector.get())
        self.update_prompt_selection()
