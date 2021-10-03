class Heuristic_Node:
    def __init__(self, id, name, status, cost, state):
        self.name = name
        self.status = status
        self.cost = cost
        self.state = state
        self.id = id
        self.root = None
        self.leftChild = None
        self.rightChild = None

    def misplaced_tile(self, goal):
        misplaced = 0

        for row in range(len(goal)):
            for column in range(len(goal)):
                if self.state[row][column] != goal[row][column]:
                    misplaced += 1

        return misplaced

    def findTile(self, tile):
        for row in range(len(self.state)):
            for column in range(len(self.state)):
                if self.state[row][column] == tile:
                    return row, column

        return -1, -1

    def manhatten_distance(self, goal):
        distance = 0
        i = 1
        for row in range(len(goal)):
            for column in range(len(goal)):
                x, y = self.findTile(i)
                if x == -1:
                    break
                else:
                    distanceX = abs(row - x)
                    distanceY = abs(column - y)
                    distance += distanceY + distanceX
                    i += 1
        return distance

    def permutation(self, goal):
        distance = 0
        permutes = 0
        for row in range(len(goal)):
            distance = 0
            for column in range(len(goal)):
                if column+1<3:
                    if self.state[row][column] > goal[row][column + 1]:
                        distance += 1
            permutes += distance

        return permutes

    def heuristic(self, goal, h):

        if h == 1:
            return self.misplaced_tile(goal)
        elif h == 2:
            return self.manhatten_distance(goal)
        else:
            return self.permutation(goal)


goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

state1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

node1 = Heuristic_Node(0, "one", 0, 0, state1)
print("goal state ", goal)
print("test state ", state1)

print("h1( misplaced tiles ) = {}".format(node1.heuristic(goal, 1)))

print("h2( manhatten distance ) = {}".format(node1.heuristic(goal, 2)))

print("h3( permutation  ) = {}".format(node1.heuristic(goal, 3)))
