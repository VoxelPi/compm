from ast import arg
import math

def count(fun):
    n = 0
    def inner(*args, **kwargs):
        nonlocal n # use variable n of outer function.
        n += 1
        return (n, fun(*args, **kwargs))
    return inner

f = count(math.sin)

print(f"f(pi/2*0) = {f(math.pi/2*0)}")
print(f"f(pi/2*1) = {f(math.pi/2*1)}")
print(f"f(pi/2*2) = {f(math.pi/2*2)}")
print(f"f(pi/2*3) = {f(math.pi/2*3)}")
print(f"f(pi/2*4) = {f(math.pi/2*4)}")