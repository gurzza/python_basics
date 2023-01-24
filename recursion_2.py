"""
Define a function seq_sum(sequence) which allows counting the sum of elements.
Elements of all nested sequences should be included

In: [1,2,3,[4,5, (6,7)]]
Out: 28
"""


def linear_seq(sequence):
    res = 0
    for item in sequence:
        if type(item) in [float, int]:
            res += item
        else:
            res += linear_seq(item)
    return res


sequence = [1, 2, 3, [4, 5, (6, 7)]]
print(linear_seq(sequence))
