# Chapter : 7 - item : 3 - Less Than or Equal

# ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k
# Chapter : 7 - item : 2 - หาค่า Min และ Max

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree

# ***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()
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
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def getMin(self):
        cur = self.root
        while cur.left != None:
            cur = cur.left
        return cur.data
    
    def getMax(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        return cur.data
    
    def getLowerNode(self, node, data):
        if node == None:
            return 0

        n = self.getLowerNode(node.left, data)
        if node.data > data:
            return n
        n += self.getLowerNode(node.right, data)

        if node.data <= data:
            n += 1
        return n

T = BST()
inp = [i for i in input('Enter Input : ').split('/')]
k = inp[-1]
newInp = [int(i) for i in inp[0].split()]
for i in newInp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.getLowerNode(root,int(k)))