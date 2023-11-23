# gui.py
import tkinter as tk
from tkinter import ttk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Egyszerú számológép")

        self.calculator = Calculator()

        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_entry = ttk.Entry(self.master, textvariable=self.result_var, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            ttk.Button(self.master, text=text, command=lambda t=text: self.button_click(t)).grid(row=row, column=col, sticky='nsew')

        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Hiba')
        else:
            current_text = self.result_var.get()
            new_text = current_text + value
            self.result_var.set(new_text)
