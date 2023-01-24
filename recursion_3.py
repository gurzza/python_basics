"""
Define a function linear_seq(sequence) which converts a passed sequence to a
sequence without nested sequences.

In: [1, 2, 3, [4, 5, (6, 7)], (8, 9)]
Out: [1, 2, 3, 4, 5, 6, 7]
"""


def linear_seq(sequance):
    lst = []
    for item in sequance:
        if not type(item) in [list, tuple]:
            lst.append(item)
        else:
            lst.extend(linear_seq(item))

    return lst


sequence = [1, 2, 3, [4, 5, (6, 7)]]

print(linear_seq(sequence))
