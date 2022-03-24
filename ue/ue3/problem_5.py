from ast import arg


def sentence(*args):
    print(" ".join(args))

sentence('I', 'like', 'cake.')

def combine(*args):
    all_int = True
    all_float = True

    for entry in args:
        if type(entry) != int:
            all_int = False
        if type(entry) != float:
            all_float = False

    if all_int:
        return sum(args)

    elif all_float:
        result = 1
        for entry in args:
            result *= entry
        return result

    else:
        return "wrong input"

print(combine(1, 2, 5))
print(combine(1.0, 2.0, 5.0))
print(combine(1, 2.0, 5))