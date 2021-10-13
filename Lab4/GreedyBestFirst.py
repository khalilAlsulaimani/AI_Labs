from timeit import default_timer as timer


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

    def greedyH1(self, cost, h, fringe, goal):
        if self:
            if self.check_goal(goal):
                fringe.append(self.state)
                print("node found ! using h{} and the fringe contains {} ".format(h, fringe))
            else:
                fringe.append(self.state)

                if self.rightChild and self.leftChild:

                    self.rightChild.set_cost(self.rightChild.heuristic(goal, h))
                    self.leftChild.set_cost(self.leftChild.heuristic(goal, h))

                    if self.rightChild.cost < self.leftChild.cost:
                        cost = cost + self.rightChild.cost
                        self.rightChild.greedyH1(cost, h, fringe, goal)

                    else:
                        cost = cost + self.leftChild.cost
                        self.leftChild.greedyH1(cost, h, fringe, goal)

                elif self.leftChild:
                    cost = cost + self.leftChild.cost
                    self.leftChild.set_cost(self.leftChild.heuristic(goal, h))
                    self.leftChild.greedyH1(cost, h, fringe, goal)

                elif self.rightChild:
                    cost = cost + self.rightChild.cost
                    self.rightChild.set_cost(self.rightChild.heuristic(goal, h))
                    self.rightChild.greedyH1(cost, h, fringe, goal)

                else:
                    print("no goal node found ", fringe.__str__())

    def greedy_best_first_search(self, cost, h, goal):
        if h == 1 or h == 2 or h == 3:
            fringe = []
            return self.greedyH1(cost, h, fringe, goal)


class tree_heuristic:
    def __init__(self):
        self.root = None

    def greedy_best_first(self, h, goal):
        self.root.greedy_best_first_search(0, h, goal)

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
    [3, 8, 0],
    [4, 5, 6],
    [7, 2, 1],
]

state3 = [
    [0, 8, 3],
    [4, 5, 6],
    [7, 1, 2],
]

state4 = [
    [0, 7, 3],
    [4, 5, 6],
    [8, 2, 1],
]

state5 = [
    [0, 3, 7],
    [4, 5, 6],
    [8, 2, 1],
]
state6 = [
    [0, 7, 8],
    [4, 5, 6],
    [3, 1, 2],
]
state7 = [
    [5, 7, 8],
    [4, 0, 6],
    [3, 2, 1],
]
state8 = [
    [0, 7, 3],
    [2, 5, 8],
    [7, 4, 1],
]
 
tree = tree_heuristic()
tree.insert(0, "first", 0, 0, state1)
tree.insert(-1, "second", 0, 0, state2)
tree.insert(1, "third", 0, 0, state3)
tree.insert(2, "fourth", 0, 0, state4)
tree.insert(3, "fourth", 0, 0, state5)
tree.insert(-3, "fourth", 0, 0, state6)
tree.insert(4, "fourth", 0, 0, state7)
tree.insert(5, "fourth", 0, 0, goal)

start = timer()
tree.greedy_best_first(1, goal)
end = timer()
time = end - start

print("H1 timer : {} ".format(time))

start = timer()
tree.greedy_best_first(2, goal)
end = timer()
time = end - start

print("H2 timer : {} ".format(time))

start = timer()
tree.greedy_best_first(3, goal)
end = timer()
time = end - start

print("H3 timer : {} ".format(time))
