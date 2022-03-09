import math

def intbreak(n):
    digits = []
    while not n==0:
        digits.append(n - math.floor(n / 10)*10)
        n = math.floor(n / 10)

    return digits

def reorder(n):
    digits = intbreak(n)
    n = 0
    pow = 1 # 10^i_digit

    # Add even digits
    for d in digits:
        if (d % 2 == 0):
            n += d * pow
            pow *= 10

    # Add odd digits
    for d in digits:
        if (d % 2 == 1):
            n += d * pow
            pow *= 10
    return n
    
print(f"inbreak(364812): {intbreak(364812)}")
print(f"reorder(364812): {reorder(364812)}")
