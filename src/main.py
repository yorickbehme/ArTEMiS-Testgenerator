import tkinter as tk
from ui_builder import TestGeneratorUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TestGeneratorUI(root)
    root.mainloop()