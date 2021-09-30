from collections import deque
from timeit import default_timer as timer


class Puzzle_Node:

    def __init__(self, id, name, status, cost, state):
        self.nodeCount = 0
        self.name = name
        self.status = status
        self.cost = cost
        self.state = state
        self.id = id
        self.root = None
        self.leftChild = None
        self.rightChild = None

    def findZero(self, state):
        for row in range(len(state)):
            for column in range(len(state)):
                if state[row][column] == 0:
                    return row, column

    def swap(self, state, x1, y1, x2, y2):
        temp_puz = state
        temp = temp_puz[x2][y2]
        temp_puz[x2][y2] = temp_puz[x1][y1]
        temp_puz[x1][y1] = temp
        return temp_puz

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

    # check goal of the 2d array if any elements are not a match return false if they match keep going
    def check_goal(self, state):
        if self:
            for row in range(len(self.state)):
                for column in range(len(self.state)):
                    if self.state[row][column] == state[row][column]:
                        continue
                    else:
                        return False
            return True

    def makeCopyList(self, state, newList):
        newList = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        for row in range(len(state)):
            for column in range((len(state))):
                newList[row][column] = state[row][column]

        return newList

    def up(self, state, x, y):
        childState = self.swap(state, x, y, x - 1, y)
        self.insert(Puzzle_Node(self.nodeCount, "e", 0, 1, childState))
        self.nodeCount += 1
        return childState

    def down(self, state, x, y):
        childState = self.swap(state, x, y, x + 1, y)
        self.insert(Puzzle_Node(self.nodeCount, "e", 0, 1, childState))
        self.nodeCount += 1
        return childState

    def right(self, state, x, y):
        childState = self.swap(state, 2, 1, 2, 2)
        self.insert(Puzzle_Node(self.nodeCount, "e", 0, 1, childState))
        self.nodeCount += 1
        return childState

    def left(self, state, x, y):
        childState = self.swap(state, x, y, x, y - 1)
        self.insert(Puzzle_Node(self.nodeCount, "e", 0, 1, childState))
        self.nodeCount += 1
        return childState

    def generate_children(self, state):
        (x, y) = self.findZero(state)
        children = []

        stateList1 = []
        stateList1 = self.makeCopyList(state, stateList1)

        stateList2 = []
        stateList2 = self.makeCopyList(state, stateList2)

        stateList3 = []
        stateList3 = self.makeCopyList(state, stateList3)

        stateList4 = []
        stateList4 = self.makeCopyList(state, stateList4)

        stateStorage = [stateList1, stateList2, stateList3, stateList4]

        if x + 1 < 3:
            children.append(self.down(stateStorage[0], x, y))

        if x - 1 > -1:
            children.append(self.up(stateStorage[1], x, y))

        if y - 1 > -1:
            children.append(self.left(stateStorage[2], x, y))

        if y + 1 < 3:
            children.append(self.right(stateStorage[3], x, y))

        return children

    # BFS using queue and recursion
    def BFS(self, goal):
        queue = []
        visited = []
        if self:
            queue.append(self)
            while len(queue) > 0:
                # print(stack.__len__())
                node = queue.pop(0)
                if node is not None:
                    if node.state is not None:
                        if node.state not in visited:
                            if node.check_goal(goal):
                                return node.state, visited.__str__()
                            else:
                                visited.append(node.state)
                                queue.append(node.generate_children(node.state))

    # DFS using stack
    def DFS(self, goal):
        stack = []
        visited = []
        if self:
            stack.append(self)
            while len(stack) > 0:
                node = stack.pop()
                if node is not None:
                    if node.state not in visited:
                        if node.check_goal(goal):
                            return node.state, visited.__str__()
                        else:
                            visited.append(node.state)
                            stack.append(node.generate_children(node.state))

    # liner search to find node using id
    def find(self, id):
        if self.id == id:
            return self
        elif self.id > id:
            if self.leftChild:
                return self.leftChild.find(id)

        else:
            if self.rightChild:
                return self.rightChild.find(id)

    # printing tree inorder
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()

            print(str(self.id))

            if self.rightChild:
                self.rightChild.inorder()

    # finding parent by using find child class to see if parent has those children
    def findParent(self, goal):
        children = []
        if self:
            children = self.findChildern(self.id)
            if self.rightChild:
                if self.rightChild.id == children[0] or (len(children) >= 2 and self.rightChild.id == children[1]):
                    return self.id
                if self.leftChild.id == children[0] or (len(children) >= 2 and self.leftChild.id == children[1]):
                    return self.id

    # using the find to retrieve its left and right children if they exist
    def findChildern(self, root):
        parent = self.find(root)
        children = []
        if parent.leftChild:
            children.append(parent.leftChild.id)
        if parent.rightChild:
            children.append(parent.rightChild.id)
        return children


class puzzle_Tree:
    def __init__(self):
        self.counter = 1
        self.root = None

    def getID(self, id):
        node = self.root.find(id)
        return node.id

    def getName(self, id):
        node = self.root.find(id)
        return node.name

    def getStatus(self, id):
        node = self.root.find(id)
        return node.status

    def getCost(self, id):
        node = self.root.find(id)
        return node.cost

    def getState(self, id):
        node = self.root.find(id)
        return node.state

    def insert(self, id, name, status, cost, state):
        node = Puzzle_Node(id, name, status, cost, state)
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def find(self, id):
        if self.root:
            return self.root.find(id)

    def BFS(self, goal):
        return self.root.BFS(goal)

    def DFS(self, goal):
        return self.root.DFS(goal)

    def inorder(self):
        self.root.inorder()

    def findParent(self, goal):
        return self.root.findParent(goal)

    def findChildern(self, goal):
        return self.root.findChildern(goal)


tree = puzzle_Tree()
# id ,name ,status ,cost ,state
state1 = [
    [4, 1, 3],
    [5, 7, 2],
    [8, 0, 6],
]
print(state1, "starting state")
goalState = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

tree.insert(1, "k", 0, 1, state1)

start = timer()
(id, path) = tree.BFS(goalState)
end = timer()
time = end - start

print("BFS timer : {}  and the path to goal node is {} and its id is  {}".format(time, path, id))

start2 = timer()
(id2, path2) = tree.DFS(goalState)
end2 = timer()
time2 = end2 - start2

print("DFS timer : {} and path  {} and id {}".format(time2, path2, id2))
