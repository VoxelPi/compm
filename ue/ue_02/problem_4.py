import math

def dec(ev, fun):
    def inner():
        return fun(ev)
    return inner

print(f"dec(pi/2, sin) = {dec(math.pi/2, math.sin)()}")
print(f"dec(1, exp) = {dec(1, math.exp)()}")

def comp(l):
    def inner(a):
        output = a
        for f in reversed(l):
            output = f(output)
        return output
    return inner

print(f"comp([math.asin, math.sin])(math.pi * 4) = {comp([math.sin, math.log, math.exp])(-math.pi/2)}")