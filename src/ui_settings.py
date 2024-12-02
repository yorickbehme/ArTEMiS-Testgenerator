import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from ui_elements import RoundedButton


class SettingsFrame(tk.Frame):
    def __init__(self, main_app, switch_frame_callback, prompt_manager):
        super().__init__(main_app.root, bg="#232323")
        self.main_app = main_app
        self.prompt_manager = prompt_manager
        
        self.switch_frame_callback = switch_frame_callback
        self.syntax_check_var = tk.BooleanVar(value=True)
        self.structure_check_var = tk.BooleanVar(value=True)
        self.selected_prompt_var = tk.StringVar(value="Einfache Funktionen")
        self.selected_model_var = tk.StringVar(value="llama3")

        # Stil setzen
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TCombobox", fieldbackground="white", background="white", foreground="black")

        self.create_widgets()

    def create_widgets(self):
        # Titel
        title_label = tk.Label(
            self, text="Einstellungen", font=("Arial", 20, "bold"),
            bg="#232323", fg="#f0f0f0"
        )
        title_label.grid(row=0, column=0, padx=20, pady=10)

        # Einstellungs Frame
        settings_frame = tk.Frame(self, bg="#373737", bd=1, relief="flat")
        settings_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Syntax-Check Option
        syntax_check_option = tk.Checkbutton(
            settings_frame, text="Syntax Prüfung aktivieren",
            font=("Arial", 14), bg="#373737", fg="#f0f0f0",
            variable=self.syntax_check_var
        )
        syntax_check_option.grid(row=0, column=0, columnspan=2, sticky="w", pady=5, padx=20)

        # Structure-Check Option
        structure_check_option = tk.Checkbutton(
            settings_frame, text="Struktur Prüfung aktivieren",
            font=("Arial", 14), bg="#373737", fg="#f0f0f0",
            variable=self.structure_check_var
        )
        structure_check_option.grid(row=1, column=0, columnspan=2, sticky="w", pady=5, padx=20)

        # Prompt-Auswahl
        prompt_label = tk.Label(
            settings_frame, text="Prompt Auswahl:", font=("Arial", 14),
            bg="#373737", fg="#f0f0f0"
        )
        prompt_label.grid(row=2, column=0, sticky="w", padx=20)

        self.prompt_selector = ttk.Combobox(
            settings_frame,
            textvariable=self.selected_prompt_var,
            values=list(self.prompt_manager.prompts.keys()),
            state="readonly"
        )
        self.prompt_selector.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

        # Erzwinge Sichtbarkeit
        self.update_idletasks()

        # Zurück-Button
        back_button = RoundedButton(
            parent=settings_frame,
            text="Zurück",
            radius=14,
            bg="#2D2D2D",
            fg="white",
            font=("Arial", 14, "bold"),
            command=lambda: self.switch_frame_callback(self.main_app.testgenerator_frame),
            width=250,
            height=50
        )
        back_button.canvas.grid(row=4, column=0, columnspan=3, pady=10)

        # Prompt Erstellung
        prompt_label = tk.Label(
            self, text="Neuer Prompt", font=("Arial", 20, "bold"),
            bg="#232323", fg="#f0f0f0"
        )
        prompt_label.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        prompt_frame = tk.Frame(self, bg="#373737", bd=1, relief="flat")
        prompt_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        # Prompt Titel
        prompt_label = tk.Label(
            prompt_frame, text="Titel:", font=("Arial", 14, "bold"),
            bg="#373737", fg="#f0f0f0"
        )
        prompt_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.prompt_titel_text = tk.Entry(
            prompt_frame, font=("Arial", 14),
            bg="#232323", fg="#f0f0f0", insertbackground="#f0f0f0", 
            width=50
        )
        self.prompt_titel_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Prompt Text
        prompt_text_label = tk.Label(
            prompt_frame, text="Prompt:", font=("Arial", 14, "bold"),
            bg="#373737", fg="#f0f0f0"
        )
        prompt_text_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.prompt_text = scrolledtext.ScrolledText(
            prompt_frame, wrap=tk.WORD, font=("Arial", 14),
            bg="#232323", fg="#f0f0f0", insertbackground="#f0f0f0", 
            width=50, height=18
        )
        self.prompt_text.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
        self.prompt_text.insert("1.0", "You are a Python test generation tool. **Generate a detailed and comprehensive Python test suite for the provided code.** Make sure the test suite aligns with the given examples and satisfies all specified requirements:\n\n### Requirements ###\n* Include test cases to verify the existence of all classes and functions, expected behavior for typical inputs, edge cases for unusual inputs, and handling of type errors.\n* Provide clear feedback in German for each failed test, specifying what functionality is required to pass.\n* Output only the complete Python test suite without any additional explanations or comments.\n\n### Example ###\n```\n\n```\n### Here comes the code to be tested ###")

        # Prompt Speichern Button
        back_button = RoundedButton(
            parent=prompt_frame,
            text="Prompt speichern",
            radius=14,
            bg="#2D2D2D",
            fg="white",
            font=("Arial", 14, "bold"),
            command=lambda: self.debounce(self.save_prompt),            
            width=250,
            height=50
        )
        back_button.canvas.grid(row=4, column=0, columnspan=3, pady=10)

        # Layout-Management

        settings_frame.grid_rowconfigure(0, weight=1)
        settings_frame.grid_columnconfigure(0, weight=1)
        settings_frame.grid_rowconfigure(1, weight=1)
        settings_frame.grid_rowconfigure(2, weight=1)
        settings_frame.grid_rowconfigure(3, weight=1)
        settings_frame.grid_rowconfigure(4, weight=1)

        prompt_frame.grid_rowconfigure(0, weight=1)
        prompt_frame.grid_columnconfigure(0, weight=1)
        prompt_frame.grid_rowconfigure(1, weight=1)
        prompt_frame.grid_rowconfigure(2, weight=1)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def save_prompt(self):
        # Eingaben aus der UI auslesen
        title = self.prompt_titel_text.get().strip()
        content = self.prompt_text.get("1.0", "end-1c").strip()

        # Validierung: Titel und Inhalt dürfen nicht leer sein
        if not title:
            messagebox.showerror("Fehler", "Der Titel darf nicht leer sein.")
            return
        if not content:
            messagebox.showerror("Fehler", "Der Prompt-Inhalt darf nicht leer sein.")
            return

        try:
            # Prüfen, ob der Titel bereits existiert
            if title in self.prompt_manager.prompts:
                # Überschreiben bestätigen
                overwrite = messagebox.askyesno(
                    "Titel überschreiben?",
                    f"Der Titel '{title}' existiert bereits. Möchtest du ihn überschreiben?"
                )
                if overwrite:
                    # Aktualisierung des Prompts
                    self.prompt_manager.update_prompt(title, content)
                    messagebox.showinfo("Erfolg", f"Der Prompt '{title}' wurde aktualisiert.")
                else:
                    return
            else:
                # Neuen Prompt hinzufügen
                self.prompt_manager.add_prompt(title, content)
                messagebox.showinfo("Erfolg", f"Der Prompt '{title}' wurde gespeichert.")

            # Dropdown-Liste aktualisieren
            self.prompt_selector["values"] = list(self.prompt_manager.prompts.keys())
            self.prompt_selector.set(title)

            # Eingabefelder zurücksetzen
            self.prompt_titel_text.delete(0, "end")
            self.prompt_text.delete("1.0", "end")

        except ValueError as e:
            # Fehler bei der Validierung abfangen
            messagebox.showerror("Fehler", str(e))
        except Exception as e:
            # Allgemeine Fehlerbehandlung
            messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")

    def debounce(self, func, delay=200):
        if hasattr(self, "_debounce_timer"):
            self.after_cancel(self._debounce_timer)
        self._debounce_timer = self.after(delay, func)