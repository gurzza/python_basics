# find quadratic roots ax^2 + bx + c = 0
import math


def ask_value():
    print('Enter a, b, c: ', end='')
    a, b, c = [int(i) for i in input().split()]
    print('Your a, b, c: ', a, b, c)
    return a, b, c


def discr():
    d2 = (b * b) - (4 * a * c)

    if d2 == 0:
        x1 = x2 = -b / (2 * a)

    elif d2 > 0:
        x1 = (-b + math.sqrt(d2)) / (2 * a)
        x2 = (-b - math.sqrt(d2)) / (2 * a)

    else:
        x1 = complex(-b / (2 * a), math.sqrt(-d2) / (2 * a))
        x2 = complex(-b / (2 * a), - math.sqrt(-d2) / (2 * a))

    return x1, x2


a, b, c = ask_value()
x1, x2 = discr()
print('x1, x2: ', x1, x2)