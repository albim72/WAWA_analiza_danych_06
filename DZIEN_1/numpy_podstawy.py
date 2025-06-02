import os
import numpy as np
from moja_funkcja import obliczenie
from books import Book

print(os.environ)
g = np.array([1,2,3,11])
print(g)
print(type(g))
print(obliczenie(4,8,3))

b1 = Book("Wiedźmin", "Andrzej Sapkowski", 1986,56.3)
print(b1)
print(f"cena po rabacie: {b1.cena_po_rabacie(10):.2f} zł")
