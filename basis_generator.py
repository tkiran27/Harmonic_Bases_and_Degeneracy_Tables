import numpy as np
import sympy as sp
from sympy.combinatorics import CyclicGroup

x, y, z, t = sp.symbols("x y z t")
n = 3
p = 2
q = 1
m = 3

G = CyclicGroup(n)
