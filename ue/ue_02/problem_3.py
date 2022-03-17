class Vector:
    """
    A class for vector calculations in an n dimensional vector space.
    Supports addition and multiplying with a scalar.
    """
    def __init__(self, entries):
        self.entries = entries

    def add(self, z2):
        """
        Adds the vector z2 to this vector and returns the result.
        """
        assert(len(self.entries) == len(z2.entries))
        return Vector([self.entries[i] + z2.entries[i] for i in range(len(self.entries))])

    def scalar(self, a):
        """
        Scales this vector by a and returns the result.
        """
        return Vector([x*a for x in self.entries])

x = Vector([0, 2, -3, 5])
y = Vector([1, 2, 3, 4])

print("Vector:")
print(f"x = {x.entries}")
print(f"y = {y.entries}")
print(f"x + y = {x.add(y).entries}")
print(f"x * 3 = {x.scalar(3).entries}")

class VectorPlus(Vector): # Extend Vector class.
    """
    Extension of the Vector class that implements the inner and outer vector product.
    """

    def __init__(self, entries):
        super().__init__(entries) # Call parent constructor.

    def inner(self, z2):
        """
        Calculates the inner vector product.
        """
        assert(len(self.entries) == len(z2.entries))
        return VectorPlus([self.entries[i] * z2.entries[i] for i in range(len(self.entries))])
    
    def outer(self, z2):
        """
        Calculates the outer vector product.
        """
        return VectorPlus([[x * y for y in z2.entries] for x in self.entries])

a = VectorPlus([0, 2, -3, 5])
b = VectorPlus([1, 2, 3, 4])

print("\nVectorPlus:")
print(f"a = {a.entries}")
print(f"b = {b.entries}")
print(f"a inner b = {a.inner(b).entries}")
print(f"a outer b = {a.outer(b).entries}")