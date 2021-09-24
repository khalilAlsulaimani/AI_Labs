
from timeit import default_timer as timer


class AI_Node():

    def __init__(self, id, name, status, cost, state):
        self.name = name
        self.status = status
        self.cost = cost
        self.state = state
        self.id = id
        self.root = None
        self.leftChild = None
        self.rightChild = None

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

    # BFS using queue and recursion
    def BFS(self, goal):
        queue = []
        visited = []
        if self and (self.id not in visited):
            queue.append(self)
            visited.append(self.id)
            while len(queue) > 0:
                # print(stack.__len__())
                node = queue.pop(0)
                if node is not None:
                    if node.check_goal(goal):
                        return node.id, visited.__str__()
                    else:
                        if node.leftChild:
                            queue.append(node.leftChild)
                            visited.append(node.leftChild.id)
                        if node.rightChild:
                            queue.append(node.rightChild)
                            visited.append(node.rightChild.id)

    # DFS using stack
    def DFS(self, goal):
        stack = []
        visited = []
        if self and (self.id not in visited):
            stack.append(self)
            visited.append(self.id)
            while len(stack) > 0:
                # print(stack.__len__())
                node = stack.pop()
                if node is not None:
                    if node.check_goal(goal):
                        return node.id, visited.__str__()
                    else:
                        if node.rightChild:
                            stack.append(node.rightChild)
                            visited.append(node.rightChild.id)
                        if node.leftChild:
                            stack.append(node.leftChild)
                            visited.append(node.leftChild.id)

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


class AI_Tree:
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
        node = AI_Node(id, name, status, cost, state)
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

    def generate_children(self, state):
        idNum =1+self.counter
        self.counter+=1
        self.insert(idNum, "name", 0, 1, state)


tree = AI_Tree()
# id ,name ,status ,cost ,state
state1 = [
    [4, 1, 3],
    [5, 7, 2],
    [8, 0, 6],
]

goalState = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

state2 = [
    [4, 1, 3],
    [5, 7, 2],
    [8, 0, 6],
]
state3 = [
    [8, 7, 6],
    [5, 4, 3],
    [2, 1, 0],
]
state4 = [
    [4, 1, 3],
    [5, 7, 2],
    [8, 0, 6],
]

tree.insert(1, "k", 0, 1, state1)
tree.generate_children(goalState)
tree.generate_children(state2)
tree.generate_children(state2)
tree.generate_children(state2)

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
