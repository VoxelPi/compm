from os import stat
import time

def a_slow(n):
    a0 = 1
    if (n == 0):
        return a0
    else:
        return 4 * a_slow(n-1) / (3 * a_slow(n-1) + 3)

def a_fast(n):
    a0 = 1
    if (n == 0):
        return a0
    else:
        a_n_1 = a_fast(n-1)
        return 4 * a_n_1 / (3 * a_n_1 + 3)


def b_slow(n):
    b0 = 5/4
    if (n == 0):
        return b0
    else:
        return b_slow(n-1)**2 - 2*b_slow(n-1) + 2

def b_fast(n):
    b0 = 5/4
    if (n == 0):
        return b0
    else:
        b_n_1 = b_fast(n-1)
        return b_n_1**2 - 2*b_n_1 + 2

def c_slow(n):
    c0 = 78/10
    if (n == 0):
        return c0
    else:
        return 1/2 * (c_slow(n-1) + 9 / c_slow(n-1))

def c_fast(n):
    c0 = 78/10
    if (n == 0):
        return c0
    else:
        c_n_1 = c_fast(n-1)
        return 1/2 * (c_n_1 + 9 / c_n_1)

def benchmark(fun, n):
    start = time.time()
    res = fun(n)
    return (f"{time.time() - start} sec", res)

N = 22
M = 500
print(f"a_{N} slow: {benchmark(a_slow, N)}")
print(f"a_{M} fast: {benchmark(a_fast, M)}")
print(f"b_{N} slow: {benchmark(b_slow, N)}")
print(f"b_{M} fast: {benchmark(b_fast, M)}")
print(f"c_{N} slow: {benchmark(c_slow, N)}")
print(f"c_{M} fast: {benchmark(c_fast, M)}")