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

    def check_goal(self, state):
        if self:
            for row in range(len(self.state)):
                for column in range(len(self.state)):
                    if self.state[row][column] == state[row][column]:
                        continue
                    else:
                        return False
            return True

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
                if i == 8:
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
                if column + 1 < 3:
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

    def GreedyH1(self, tree, goal):
        pass

    def GreedyH2(self, tree, goal):
        pass

    def GreedyH3(self, tree, goal):
        pass


class tree_heuristic:
    def __init__(self):
        self.root = None

    def greedy_best_first(self, h, goal, tree):
        if h == 1:
            return self.root.GreedyH1(tree, goal)
        if h == 2:
            return self.root.GreedyH2(tree, goal)
        if h == 3:
            return self.root.GreedyH3(tree, goal)


goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

state1 = [
    [0, 8, 3],
    [4, 5, 6],
    [7, 2, 1],
]
