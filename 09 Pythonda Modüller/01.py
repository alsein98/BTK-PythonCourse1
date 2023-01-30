import math 

print(math.ceil(3.7))
print(dir(math))
"""
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
"""
print(help(math.isqrt))
print(math.isqrt(11)) # nearest sqrt base
print(math.factorial(4))
#----------------------------------------
import math as op
print(op.floor(113.7))
#----------------------------------------
from math import cos,sin
print(cos(0))
#----------------------------------------
#from math import *
def cos(x):
    return "YO-"

print(cos(0)) # return the last diff.