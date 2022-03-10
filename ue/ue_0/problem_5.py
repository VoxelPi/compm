import math

def eval_series(n):
    # calculate k.
    k = math.floor(-1/2 + math.sqrt(2*n + 9/4))
    assert(k**2 + k - 2 <= 2*n <= k**2 + 3*k - 2)

    # calculate a_n.
    return n + 1/k - (k**2 + k - 2) / 2

# print first 100 members of the sequence.
for i in range(100):
    print(f"a_{i} = {eval_series(i)}")