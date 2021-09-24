from collections import deque
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

    # BFS using queue and recursion
    def BFS(self, goal):
        fringe = deque()
        if self:
            fringe.append(self.id)

            if self.id == goal:
                return goal
            fringe.popleft()
            if self.leftChild:
                fringe.append(self.leftChild.id)
                # print(fringe.__len__())
                self.leftChild.BFS(goal)

            if self.rightChild:
                fringe.append(self.rightChild.id)
                # print(fringe.__len__())
                self.rightChild.BFS(goal)

    # DFS using stack
    def DFS(self, goal):
        stack = []
        if self:
            stack.append(self)
            while len(stack) > 0:
                #print(stack.__len__())
                node = stack.pop()
                if node is not None:
                    if node.id == goal:
                        return node.id
                    else:
                        if node.rightChild:
                            stack.append(node.rightChild)
                        if node.leftChild:
                            stack.append(node.leftChild)



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
        self.root.BFS(goal)

    def DFS(self, goal):
        return self.root.DFS(goal)

    def inorder(self):
        self.root.inorder()

    def findParent(self, goal):
        return self.root.findParent(goal)

    def findChildern(self, goal):
        return self.root.findChildern(goal)



tree = AI_Tree()
# id ,name ,status ,cost ,state
tree.insert(1, "k", 0, 1, 0)
tree.insert(2, "a", 0, 2, 0)
tree.insert(3, "b", 0, 3, 0)
tree.insert(4, "c", 0, 4, 0)
tree.insert(-20, "kp", 0, 1, 0)
tree.insert(5, "d", 0, 5, 0)
tree.insert(6, "v", 0, 5, 0)
tree.insert(0, "kp", 0, 1, 0)
tree.insert(-1, "kp", 0, 1, 0)
tree.insert(9, "kp", 0, 1, 0)
tree.insert(-2, "kp", 0, 1, 0)
tree.insert(-3, "kp", 0, 1, 0)
tree.insert(-4, "kp", 0, 1, 0)
tree.insert(8, "kp", 0, 1, 0)
tree.insert(10, "kp", 0, 1, 0)
tree.insert(11, "kp", 0, 1, 0)
tree.insert(-11, "kp", 0, 1, 0)
tree.insert(12, "kp", 0, 1, 0)
tree.insert(100, "kp", 0, 1, 0)

print("chidlren of node 1 are {}".format(tree.findChildern(1)))
print("parent of node -1 is {}".format(tree.findParent(-1)))

start = timer()
tree.BFS(3)
end = timer()
time = end - start

print("BFS timer : {} ".format(time))

start2 = timer()
tree.DFS(3)
end2 = timer()
time2 = end2 - start2
print("DFS timer : {} ".format(time2))

print("node 0 id is {}".format(tree.getID(0)))
print("node 0 name is {}".format(tree.getName(0)))
print("node 0 status is {}".format(tree.getStatus(0)))
print("node 0 cost is {}".format(tree.getCost(0)))
print("node 0 state is {}".format(tree.getState(0)))


