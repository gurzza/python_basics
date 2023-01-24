# find an exit (exit is 2)
import sys
import time

map = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 2, 1, 1, 1]
]


def outMap():
    for line in map:
        for i in line:
            print(i, end='')
        print()
    print()


def action(x, y):
    if map[x][y] == 2:
        print('EXIT IS FOUND!')
        sys.exit()

    if map[x][y] == 0:
        map[x][y] = '*'
        route(x, y)


def route(x, y):
    outMap()
    time.sleep(1)
    action(x - 1, y)
    action(x + 1, y)
    action(x, y - 1)
    action(x, y + 1)

    if map[x][y] == '*':  # false route
        map[x][y] = 0


route(2, 1)
