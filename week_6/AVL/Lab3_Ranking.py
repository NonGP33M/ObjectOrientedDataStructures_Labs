'''

Chapter : 8 - item : 3 - Ranking

จงเขียนฟังก์ชั่นในการหา Rank ของ input ที่รับเข้ามา โดย Rank คือการแบ่งเป็นชั้นๆตามข้อมูลของ BST โดยจะเริ่มจากค่าที่น้อยกว่าค่าใน BST ที่น้อยที่สุดจะมีค่า Rank = 0 และค่าที่อยู่ตั้งแต่ค่าที่น้อยที่สุดจนถึงตัวถัดไปจะมีค่า Rank +=1 ไปเรื่อยๆจนถึงชั้นของตัวสุดท้ายหรือตัวมากสุด เช่น

จากรูป ค่าที่น้อยที่สุดคือ -2 ดังนั้น rank(-2) จะได้ 1 แต่ rank ของค่าที่น้อยกว่า -2 จะเท่ากับ 0

และ rank(0) จะเท่ากับ 1 ส่วน rank(1) จะเท่ากับ 2 เป็นต้น

'''

class BST:
    def __init__(self):
        self.root = None
    def setRoot(self,node):
        self.root = node
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        elif self.root != None:
            p=self.root
            while(p!=None):
                if data >= p.data:
                    if p.right == None:
                        p.right = Node(data)
                        break
                    p=p.right

                elif data < p.data:
                    if p.left == None:
                        p.left = Node(data)
                        break
                    p=p.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

def findRank(node,value):
    global rank
    global ans
    global found
    if node == None:
        return
    findRank(node.left,value)
    rank+=1
    #print('data : ' + str(node.data) +' rank : ' + str(rank))
    if node.data == value:
        if not found:
            ans = rank-1
            return
    elif node.data > value:
        if not found:
            found = True
            #print('elif : ' + str(node.data) + ' rank : ' + str(rank))
            ans = rank-1
            return
    findRank(node.right,value)
    if not found:
        ans=rank

inp,val=input('Enter Input : ').split('/')
inpLis = [int(e) for e in inp.split()]
ans=0
rank=0
found = False
T = BST()
for data in inpLis:
    T.insert(data)
T.printTree(T.root)
findRank(T.root,int(val))
print('--------------------------------------------------')
print('Rank of {0} : '.format(val) + str(ans))