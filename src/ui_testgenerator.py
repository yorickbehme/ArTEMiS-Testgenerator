import tkinter as tk
from tkinter import scrolledtext, messagebox
from ui_elements import RoundedButton


class TestGeneratorFrame(tk.Frame):
    def __init__(self, main_app, switch_frame_callback, test_generator_model):
        super().__init__(main_app.root, bg="#232323")
        self.main_app = main_app
        self.switch_frame_callback = switch_frame_callback
        self.test_generator_model = test_generator_model
        self.last_error = None  
        self.last_code_state = "" 
        self.create_widgets()

    def create_widgets(self):
        # Eingabebereich
        code_label = tk.Label(
            self, text="Musterlösung", font=("Arial", 20, "bold"),
            bg="#232323", fg="#f0f0f0"
        )
        code_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        code_frame = tk.Frame(self, bg="#373737", bd=1, relief="flat")
        code_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.code_text = tk.Text(
            code_frame, wrap=tk.WORD, font=("Arial", 14),
            bg="#232323", fg="#f0f0f0", insertbackground="#f0f0f0"
        )
        self.code_text.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.code_text.insert(tk.END, "Beispiel...\ndef example_function(x):\n    return x * 2")

        # Buttons
        button_frame = tk.Frame(code_frame, bg="#373737")
        button_frame.grid(row=2, column=0, pady=10, sticky="ew")

        settings_button = RoundedButton(
            parent=button_frame,
            text="Einstellungen",
            radius=14,
            bg="#2D2D2D",
            fg="white",
            font=("Arial", 14, "bold"),
            command=lambda: self.switch_frame_callback(self.main_app.settings_frame),
            width=250,
            height=50
        )
        settings_button.canvas.grid(row=1, column=0, padx=5, pady=5)

        generate_button = RoundedButton(
            parent=button_frame,
            text="Testgenerierung starten",
            radius=14,
            bg="#2D2D2D",
            fg="white",
            font=("Arial", 14, "bold"),
            command=self.main_app.start_generate_test,
            width=250,
            height=50
        )
        generate_button.canvas.grid(row=0, column=0, padx=5, pady=5)

        # Ausgabebereich
        testcode_label = tk.Label(
            self, text="Testcode", font=("Arial", 20, "bold"),
            bg="#232323", fg="#f0f0f0"
        )
        testcode_label.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        testcode_frame = tk.Frame(self, bg="#373737", bd=2, relief="flat")
        testcode_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")
        self.output_text = scrolledtext.ScrolledText(
            testcode_frame, wrap=tk.WORD, font=("Arial", 14),
            bg="#232323", fg="#f0f0f0"
        )
        self.output_text.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.output_text.insert(tk.END, "Hier erscheint der generierte Testcode.")
        self.output_text.config(state=tk.DISABLED)

        # Layout-Management
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)

        code_frame.grid_rowconfigure(0, weight=1)
        code_frame.grid_columnconfigure(0, weight=1)

        testcode_frame.grid_rowconfigure(0, weight=1)
        testcode_frame.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def update_output(self, result):
        """
        Aktualisiert den Ausgabebereich mit dem generierten Testcode.
        Zeigt Fehler nur dann an, wenn sich der Fehler geändert hat oder
        wenn der Code geändert wurde.
        """

        # Aktuellen Codezustand holen
        current_code = self.code_text.get("1.0", tk.END).strip()

        # Prüfen, ob der Code sich geändert hat
        code_changed = current_code != self.last_code_state

        # Fehlerprüfung
        if result in ["generation_running", "empty_code", "syntax_error", "structure_error"]:
            # Verhindere doppelte Fehler, es sei denn, der Code hat sich geändert
            if result == self.last_error and not code_changed:
                return

            # Aktualisiere Fehlerzustand und Codezustand
            self.last_error = result
            self.last_code_state = current_code

            if result == "generation_running":
                # Nur eine Meldung anzeigen
                self.output_text.config(state=tk.NORMAL)
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, "Die Testgenerierung läuft, dies kann einen Moment dauern...")
                self.output_text.config(state=tk.DISABLED)
                return

            # Fehlermeldung anzeigen
            message_map = {
                "empty_code": "Die Musterlösung darf nicht leer sein. Bitte geben Sie eine Musterlösung ein.",
                "syntax_error": "Der Code enthält Syntaxfehler. Bitte korrigieren Sie diese oder deaktivieren Sie die Syntaxprüfung.",
                "structure_error": "Der Code enthält keine testbaren Strukturen. Bitte überprüfen Sie den Code oder deaktivieren Sie die Strukturprüfung.",
            }
            messagebox.showerror("Fehler", message_map[result])
            return

        # Rücksetzen bei erfolgreicher Ausgabe
        self.last_error = None
        self.last_code_state = current_code

        # Testcode aktualisieren
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state=tk.DISABLED)
