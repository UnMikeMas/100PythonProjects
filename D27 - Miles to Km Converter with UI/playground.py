def add(*args):
    total = 0
    for i in args:
        total += i
    print(total)


add(8, 9, 10, 67, 9000)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=5, multiply=10)

