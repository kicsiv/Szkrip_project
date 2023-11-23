# Szkrip_project
# Egyszerű Számológép Program

Ez a program egy egyszerű számológépet valósít meg Python nyelven. A számológép három fő modult tartalmaz: `calculator`, `gui`, és `utils`. Az alábbiakban röviden ismertetem, hogy melyik modul mit csinál.

## Modulok és Függvények:

### `calculator` modul:

A `calculator` modul a számológép matematikai műveleteit kezeli.

- **Calculator osztály:**
  - `add(x, y)`: Összeadja a két bemenő számot.
  - `subtract(x, y)`: Kivonja az egyik számot a másikból.
  - `multiply(x, y)`: Szorozza a két bemenő számot.
  - `divide(x, y)`: Osztja az egyik számot a másikkal. Figyel a nullával történő osztásra.

### `gui` modul:

A `gui` modul a grafikus felhasználói felületet kezeli.

- **CalculatorGUI osztály:**
  - Létrehozza a főablakot és vezérlőket (entry mező, gombok).
  - Kezeli a gombokra kattintás eseményeket, és frissíti az eredményt az entry mezőben.

### `utils` modul:

A `utils` modul segédfüggvényeket tartalmaz.

- `square(x)`: Szám négyzetre emelése.
- `cube(x)`: Szám köbre emelése.
- `power(x, y)`: x számot emeli y hatványra.

## Saját Függvények:

- `custom_function(x)`: Egy egyszerű saját függvény, ami a bemenő számhoz hozzáad 10-et.

## Fő Program:

A `main.py` fájl a fő program, amely importálja és használja a fenti modulokat.

```python
import tkinter as tk
from gui import CalculatorGUI
from utils import square, cube, power

# Saját függvény példa
print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("Power of 2 to the 3rd:", power(2, 3))

# A bemutatásra szánt modul használata
root = tk.Tk()
app = CalculatorGUI(root)
root.mainloop()
