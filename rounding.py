def rounding(a, b):
    return round((12 * a + 25 * b) / (1 + a ** (2 ** b)), 2)


print(rounding(2, 2))
