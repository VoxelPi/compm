def f(*args, **kwargs):
    for i in filter(lambda x: type(x) == int and x < len(kwargs), args):
        if i % 2 == 0:
            print(list(kwargs.keys())[i])
        else:
            print(list(kwargs.values())[i])

f(2, 7, 1, 'a', a=1, b=5, c=3)