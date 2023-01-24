# Implement a function foo(List[int]) -> List[int] which, given a list of integers,
# returns a new list such that each element at index i of the new list is the product of all the numbers in the original
# array except the one at i.

# Ex:
# input: foo([1, 2, 3, 4, 5])
# output: [120, 60, 40, 30, 24]

def foo(lst):
    m = 1
    for item in lst:
        m *= item

    new_lst = [0] * len(lst)
    for i in range(len(lst)):
        new_lst[i] = m / lst[i]

    return new_lst


if __name__ == '__main__':
    assert foo([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert foo([3, 2, 1]) == [2, 3, 6]
