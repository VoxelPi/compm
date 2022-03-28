# dictionary of all supported currencies and their relative value.
CURRENCIES = {
    "EUR": 1,
    "USD": 1.10,
    "CAD": 1.39,
    "JPY": 131.49
}

class ccy:
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __add__(self, other):
        return ccy(self.value + (other.value / CURRENCIES[other.currency]) * CURRENCIES[self.currency], self.currency)

    def __eq__(self, other):
        return self.value / CURRENCIES[self.currency] == other.value / CURRENCIES[other.currency]

    def __str__(self):
        return f"{self.value} {self.currency}"

a = ccy(1, "EUR")
b = ccy(1.1, "USD")
print(a + b)

print(ccy(2, "EUR") == a + b)
print(ccy(1, "USD") == a + b)