class Complex:
    """
    A class that represents a complex number.
    Supports addition, multiplication and division.
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, z2):
        """
        Adds z2 to this complex number and returns the result.
        """
        return Complex(self.real + z2.real, self.imag + z2.imag)

    def multiply(self, z2):
        """
        Multiplies this complex number with z2 and returns the result.
        """
        return Complex(self.real * z2.real - self.imag * z2.imag, self.real * z2.imag + self.imag * z2.real)

    def divide(self, z2):
        """
        Divides this complex by z2 and returns the result.
        """
        return Complex((self.real * z2.real + self.imag * z2.imag) / (z2.real**2 + z2.imag**2), (self.imag * z2.real - self.real * z2.imag) / (z2.real**2 + z2.imag**2))

A = Complex(5, 3)
B = Complex(2, -1)

a = A.real + A.imag*1j
b = B.real + B.imag*1j

print("Add:")
C = A.add(B)
print(f"A + B = ({C.real}+{C.imag}j)")
print(f"a + b = {a + b}")

print("Multiply:")
C = A.multiply(B)
print(f"A * B = ({C.real}+{C.imag}j)")
print(f"a * b = {a * b}")

print("Divide:")
C = A.divide(B)
print(f"A / B = ({C.real}+{C.imag}j)")
print(f"a / b = {a / b}")