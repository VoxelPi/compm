class new_list(list):
    def __getitem__(self, index):
        return super().__getitem__(index - 1)

    def __setitem__(self, index, value):
        return super().__setitem__(index - 1, value)

    def __delitem__(self, index):
        return super().__delitem__(index - 1)

# Test __getitem__
l = new_list(['A', 'B', 'C', 'D'])

# Test __setitem__
print(l[2])
l[1] = 'Z'
print(l[1])

# Test __delitem__
del l[1]
print(l[1])

class strange_float(float):
    def __add__(self, other):
        return super().__sub__(other)

    def __sub__(self, other):
        return super().__add__(other)

    def __mul__(self, other):
        assert(other != 0)
        return super().__truediv__(other)
    
    def __truediv__(self, other):
        return super().__mul__(other)

a = strange_float(1)
b = strange_float(2)

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")