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

    def set_cost(self, cost):
        if self:
            self.cost = cost

    def set_status(self, status):
        if self:
            self.status = status

    def insert(self, node):
        if self.id > node.id:
            if self.leftChild:
                return self.leftChild.insert(node)
            else:
                self.leftChild = node

        elif self.id < node.id:
            if self.rightChild:
                return self.rightChild.insert(node)
            else:
                self.rightChild = node

    def check_goal(self, state):
        if self:
            for row in range(len(self.state)):
                for column in range(len(self.state)):
                    if self.state[row][column] != state[row][column]:
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

    def greedyH1(self, fringe, goal):
        if self:
            if self.check_goal(goal):
                fringe.append(self.state)
                return self, fringe.__str__()
        else:
            self.set_cost(self.heuristic(self.state, 1))
            fringe.append(self.state)
            while self.leftChild or self.rightChild:
                if self.leftChild:
                    self.leftChild.set_cost(self.leftChild.heuristic(goal, 1))
                if self.rightChild:
                    self.rightChild.set_cost(self.rightChild.heuristic(goal, 1))

                if self.rightChild.cost < self.rightChild.cost:
                    self.rightChild.greedyH1(fringe, goal)
                else:
                    self.leftChild.greedyH1(fringe, goal)

    def greedyH2(self, tree, goal):
        pass

    def greedyH3(self, tree, goal):
        pass


class tree_heuristic:
    def __init__(self):
        self.root = None

    def greedy_best_first(self, h, goal):
        if h == 1:
            return self.root.greedyH1([], goal)
        if h == 2:
            return self.root.greedyH2(goal)
        if h == 3:
            return self.root.greedyH3(goal)

    def insert(self, id, name, status, cost, state):
        node = Heuristic_Node(id, name, status, cost, state)
        if self.root:
            self.root.insert(node)
        else:
            self.root = node


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

state2 = [
    [0, 8, 3],
    [4, 5, 6],
    [7, 2, 1],
]

state3 = [
    [0, 8, 3],
    [4, 5, 6],
    [7, 2, 1],
]

state4 = [
    [0, 8, 3],
    [4, 5, 6],
    [7, 2, 1],
]

tree = tree_heuristic()
tree.insert(0, "first", 0, 0, state1)
tree.insert(-1, "secound", 0, 0, state2)
tree.insert(1, "third", 0, 0, state3)
tree.insert(-2, "fourth", 0, 0, state4)

(node, fringe) = tree.greedy_best_first(1, goal)

print("node is goal {} and fringe is {} ".format(node, fringe))
