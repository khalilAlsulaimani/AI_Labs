# check goal of the 2d array if any elements are not a match return false if they match keep going
def check_goal(state,goal):
    if state:
        for row in range(len(state)):
            for column in range(len(state)):
                if state[row][column] == goal[row][column]:
                    continue
                else:
                    return False
        return True


def findZero(state):
    for row in range(len(state)):
        for column in range(len(state)):
            if state[row][column] == 0:
                return row, column


def swap(state, x1, y1, x2, y2):
    temp_puz = state
    temp = temp_puz[x2][y2]
    temp_puz[x2][y2] = temp_puz[x1][y1]
    temp_puz[x1][y1] = temp
    return temp_puz


def up(state, x, y):
    if x - 1 > -1:
        childState = swap(state, x, y, x - 1, y)
        return childState


def down(state, x, y):
    if x + 1 < 3:
        childState = swap(state, x, y, x + 1, y)
        return childState


def right(state, x, y):
    if y + 1 < 3:
        childState = swap(state, x, y, x, y + 1)
        return childState


def left(state, x, y):
    if y - 1 > -1:
        childState = swap(state, x, y, x, y - 1)
        return childState


class test:
    stateIntial = [
        [4, 1, 3],
        [5, 7, 2],
        [8, 0, 6],
    ]

    stateIntial1 = [
        [4, 1, 3],
        [5, 7, 2],
        [8, 0, 6],
    ]
    stateIntial2 = [
        [4, 1, 3],
        [5, 7, 2],
        [8, 0, 6],
    ]
    print(stateIntial1)

    stateD = [
        [4, 1, 3],
        [5, 0, 2],
        [8, 7, 6],
    ]
    print(stateIntial, "starting state")

    goalState = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]

    x, y = findZero(stateIntial)
    x1, y1 = findZero(stateD)
    state = up(stateIntial, x, y)
    print(state, "up")
    print(stateD, "starting for down")
    state2 = down(stateD, x1, y1)
    print(state2, "down")

    print(stateIntial, "starting state")

    print(stateIntial1, "hopde not modified")
    state3 = right(stateIntial1, x, y)
    print(state3, "right")

    print(stateIntial2, "hopde not modified")
    state3 = left(stateIntial2, x, y)
    print(state3, "left")

    print("is node {} a goal state ? {} ".format(goalState,check_goal(goalState,goalState)))
