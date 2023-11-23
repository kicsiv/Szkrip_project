# main.py

import tkinter as tk
from gui import CalculatorGUI
from utils import square, cube, power


def custom_function(x):
    return x + 10


print("5-nek a négyzete: ", square(5))
print("3-nak a köbe: ", cube(3))
print("2 a harmadikon: ", power(2, 3))


root = tk.Tk()
app = CalculatorGUI(root)
root.mainloop()

