# Chapter : 7 - item : 5 - ส่วนไหน

# นำ code จากข้อ 1 มาเปลี่ยนเป็น

# T = BST()
# inp = [int(i) for i in input('Enter Input : ').split()]
# for i in range(1, len(inp)):
#     root = T.insert(inp[i])
# T.printTree(root)
# T.checkpos(inp[0])
# เพื่อหาว่าค่าแรกที่ใส่เข้าไปอยู่ที่ตำแหน่งใดใน BST
# ##code output

# print("Not exist")
# print("Root")
# print("Inner")
# print("Leaf")

class BST:
    def __init__(self):
        self.root = None
        self.level = 0

    def insert(self, data):
        level = 0
        if self.root == None:
            self.root = Node(data)
        elif self.root != None:
            p=self.root
            while(p!=None):
                level+=1
                if data >= p.data:
                    if p.right == None:
                        self.level = max(level,self.level)
                        p.right = Node(data)
                        break
                    p=p.right

                elif data < p.data:
                    if p.left == None:
                        self.level = max(level,self.level)
                        p.left = Node(data)
                        break
                    p=p.left
    def checkpos(self,data):
        temp=[]
        dataLv=0
        level=0
        found=False
        p=self.root
        temp.append(p)
        temp.append(level)
        q=Queue()
        q.push(temp)
        while(not q.isEmpty()):
            if(q.front()[0]==None):
                q.pop()
                continue
            if(q.front()[0].data==data):
                dataLv=q.front()[1]
                found=True
                break
            nextL=q.front()[0].left
            nextR=q.front()[0].right
            temp=[nextL,q.front()[1]+1]
            q.push(temp)
            temp=[nextR,q.front()[1]+1]
            q.push(temp)
            q.pop()
        if dataLv==0 and found:
            print('Root')
        elif dataLv == self.level:
            print('Leaf')
        elif not found:
            print("Not exist")
        else:
            print("Inner")
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        temp=''
        for i in range(len(self.queue)):
            if i != len(self.queue)-1:
                temp+=str(self.queue[i])
                temp+=' '
            else:
                temp+=str(self.queue[i])
        return str(temp)
    def size(self):
        return int(len(self.queue))
    def pop(self):
        if(len(self.queue)>0):
            return self.queue.pop(0)
    def front(self):
        if(len(self.queue)>0):
            return self.queue[0]   
        return None
    def push(self,arg):
        self.queue.append(arg)
    def isEmpty(self):
        if(len(self.queue)>0):
            return False
        else:
            return True
    def reset(self):
        self.queue=[]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    T.insert(inp[i])
T.printTree(T.root)
T.checkpos(inp[0])