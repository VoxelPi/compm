class quaternion:
    def __init__(self, a0, a1, a2, a3):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, other):
        return quaternion(self.a0 + other.a0, self.a1 + other.a1, self.a2 + other.a2, self.a3 + other.a3)
    
    def __mul__(self, other):
        a0 = self.a0 * other.a0 - self.a1 * other.a1 - self.a2 * other.a2 - self.a3 * other.a3
        a1 = self.a0 * other.a1 + self.a1 * other.a0 + self.a2 * other.a3 - self.a3 * other.a2
        a2 = self.a0 * other.a2 - self.a1 * other.a3 + self.a2 * other.a0 + self.a3 * other.a1
        a3 = self.a0 * other.a3 + self.a1 * other.a2 - self.a2 * other.a1 + self.a3 * other.a0
        return quaternion(a0, a1, a2, a3)
    
    def __str__(self) -> str:
        return f"({self.a0} + {self.a1}*i + {self.a2}*j + {self.a3}*k)"

z1 = quaternion(1, 1, 1, 1)
z2 = quaternion(2, 2, 2, 2)

print(f"z1 + z2 = {z1 + z2}")
print(f"z1 * z2 = {z1 * z2}")