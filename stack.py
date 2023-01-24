# LIFO = Last In First Out

stack = []


def push(value):
    stack.append(value)


def pop():
    if not len(stack):
        print('The stack is already empty!')
    else:
        stack.pop(-1)


push(1)
push(2)
push(3)
print(stack)
pop()
print(stack)
pop()
pop()
pop()
print(stack)
