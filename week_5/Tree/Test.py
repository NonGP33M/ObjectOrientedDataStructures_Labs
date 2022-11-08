class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = newNode
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newNode
                        break
                    else:
                        temp = temp.right
        return self.root
    def getMin(self):
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp.data

    def getMax(self):
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.data

    def getLowerNode(self, node, data):
        if node == None:
            return 0
        else:
            if data > node.data:
                n += self.getLowerNode(node.right,data)
            else:
                n = self.getLowerNode(node.left,data)
        return  n

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [i for i in input('Enter Input : ').split('/')]
k = inp[-1]
newInp = [int(i) for i in inp[0].split()]
for i in newInp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.getLowerNode(root,int(k)))  