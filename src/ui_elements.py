import tkinter as tk

class RoundedButton:
    def __init__(self, parent, text, radius, bg, fg, font, command, width, height):
        self.parent = parent
        self.text = text
        self.radius = radius
        self.bg = bg
        self.fg = fg
        self.font = font
        self.command = command
        self.width = width
        self.height = height
        self.create_button()

    def create_button(self):
        # Canvas erstellen
        self.canvas = tk.Canvas(
            self.parent,
            width=self.width,
            height=self.height,
            bg=self.parent.cget("bg"),
            highlightthickness=0
        )
        self.canvas.grid(row=0, column=0, padx=10, pady=5, columnspan=3)

        # Abgerundetes Rechteck
        self.canvas.create_arc(0, 0, self.radius * 2, self.radius * 2, start=90, extent=90, fill=self.bg, outline=self.bg)
        self.canvas.create_arc(self.width - self.radius * 2, 0, self.width, self.radius * 2, start=0, extent=90, fill=self.bg, outline=self.bg)
        self.canvas.create_arc(0, self.height - self.radius * 2, self.radius * 2, self.height, start=180, extent=90, fill=self.bg, outline=self.bg)
        self.canvas.create_arc(self.width - self.radius * 2, self.height - self.radius * 2, self.width, self.height, start=270, extent=90, fill=self.bg, outline=self.bg)
        self.canvas.create_rectangle(self.radius, 0, self.width - self.radius, self.height, fill=self.bg, outline=self.bg)
        self.canvas.create_rectangle(0, self.radius, self.width, self.height - self.radius, fill=self.bg, outline=self.bg)

        # Text in der Mitte
        self.text_id = self.canvas.create_text(self.width / 2, self.height / 2, text=self.text, fill=self.fg, font=self.font)

        # Klick-Event binden
        self.canvas.tag_bind(self.text_id, "<Button-1>", lambda event: self.command())
        self.canvas.tag_bind("all", "<Button-1>", lambda event: self.command())