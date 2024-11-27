import numpy
import pytensor.tensor as pt
from pytensor import function
x = pt.dscalar('x')
y = pt.dscalar('y')
z = x + y
print(z)
f = function([x,y],z)
print(f(2,3))