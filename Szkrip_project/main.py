# main.py

import tkinter as tk
from gui import CalculatorGUI
from utils import square, cube, power


def custom_function(x):
    return x + 10


print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("Power of 2 to the 3rd:", power(2, 3))


root = tk.Tk()
app = CalculatorGUI(root)
root.mainloop()

