def test_fermats_last_problem(n, a, b, c):
    return a**n + b**n == c**n

print("Searching for solutions...")
for n in range(3, 100):
    for a in range(2, 40):
        for b in range(2, 40):
            for c in range(2, 40):
                if (test_fermats_last_problem(n, a, b, c)):
                    print(f"Found solution: n={n}, a={a}, b={b}, c={c}")

# series x.
def x(n):
    if n == 0:
        return 10 # x_0
    
    x_n_1 = x(n-1)

    return 2*(x_n_1**3)/(3*(x_n_1**2) - 1)

print("\nSeries x:")
for i in range(30):
    print(f"x_{i} = {x(i)}")


# series y.
def y(n):
    if n == 0:
        return 10 # y_0
    
    y_n_1 = y(n-1)

    return 1/2 * (y_n_1 + 1 / y_n_1)

print("\nSeries y:")
for i in range(30):
    print(f"y_{i} = {y(i)}")