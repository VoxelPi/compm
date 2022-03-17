def split(input):
    return [{a} for a in input]

print(f"split({1, 2, 3}): {split({1, 2, 3})}")

# Create list a.
a = [set(range(n+1, 101)) for n in range(100)]
def diff(k):
    assert(0 <= k <= 99)
    if k == 99:
        return a[99]

    return a[k] - diff(k + 1)

for i in range(0, 100):
    print(f"diff({i}) = {diff(i)}")