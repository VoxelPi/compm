def tuple_to_int(digits):
    pow = 1
    number = 0
    for digit in reversed(digits):
        number += digit * pow
        pow *= 10
    return number

def sum_tuples(tuples):
    results = []
    for tuple in tuples:
        sum = 0
        for number in tuple:
            sum += number
        results.append(sum)
    return results

def tuple_to_complex(tuple):
    even_digits = []
    odd_digits = []
    for digit in tuple:
        if digit % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)

    even_digits.sort()
    odd_digits.sort()
    odd_digits.reverse()

    return complex(tuple_to_int(even_digits), tuple_to_int(odd_digits))

print(f"tuple_to_int((1, 2, 3)): {tuple_to_int((1, 2, 3))}")
print(f"sum_tuples([(1, 2), (2, 3, 4), (3, 4)]): {sum_tuples([(1, 2), (2, 3, 4), (3, 4)])}")
print(f"tuple_to_complex((5, 2, 1, 3, 4)): {tuple_to_complex((5, 2, 1, 3, 4))}")