'''

Chapter : 8 - item : 1 - Huffman Encoding

ให้นักศึกษาเขียนโปรแกรมในการเข้ารหัส Huffman (บีบอัดข้อมูล) โดยใช้ Tree และแสดงผลตามตัวอย่าง

#อ่านวิธีการเข้ารหัสได้ที่ http://datastructurealgori.blogspot.com/2017/06/huffmans-code.html

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data[0])

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

class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        s=''
        for i in self.items:
            s+=str(i)
            s+=', '
        return s
    def reverse(self):
        self.items.reverse()
    def push(self,i):
        self.items.append(i)
    def top(self):
        if self.size() != 0:
            return self.items[len(self.items)-1]
    def pop(self):
        if not self.isEmpty():
            poped=self.items.pop(len(self.items)-1)
            return poped
    def isEmpty(self):
        if(len(self.items)==0):
            return True
        else: 
            return False
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        temp=''
        for i in range(len(self.queue)):
            if i != len(self.queue)-1:
                temp+=self.queue[i].data[0]
                temp+=', '
            else:
                temp+=self.queue[i].data[0]
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
    def second(self):
        if(len(self.queue)>1):
            return self.queue[1]   
        return None

    def push(self,arg):
        self.queue.append(arg)
    def isEmpty(self):
        if(len(self.queue)>0):
            return False
        else:
            return True

def findEncode(root,codeWord):
    if(root.left == None and root.right == None):
        encodedDic.update({root.data[0]:codeWord})
        return
    findEncode(root.right,codeWord+'1')
    findEncode(root.left,codeWord+'0')
inp = input('Enter Input : ')
count = {}
for i in inp:
    if i not in count:
        count.update({i:1})
    else:
        count[i]+=1
sort_count = dict(sorted(count.items(), key=lambda x: x[::-1],reverse=False))
st=Stack()
q=Queue()
for i in sort_count.items():
    q.push(Node(i))
#st.reverse()
q2=Queue()
while not q.isEmpty():
    if q2.isEmpty():
        q2.push(q.pop())
    else:
        while q2.size()>=2 and q.front().data[1] >= q2.front().data[1] + q2.second().data[1]:
            pop1 = q2.pop()
            pop2 = q2.pop()
            newNode = Node(('*',pop1.data[1]+pop2.data[1]))
            newNode.left = pop1
            newNode.right = pop2
            q2.push(newNode)
        
        q2.push(q.pop())
while not q2.isEmpty():
    pop1=q2.pop()
    pop2=q2.pop()
    newNode = Node(('*',pop1.data[1]+pop2.data[1]))
    newNode.left=pop1
    newNode.right=pop2
    q2.push(newNode)
    if q2.size()==1:
        root = q2.pop()

encodedDic = {}
findEncode(root,'')
print(encodedDic)
bst = BST()
bst.setRoot(root)
bst.printTree(bst.root)
encodedWord=''
for i in inp:
    encodedWord+=encodedDic[i]
print('Encoded! : '+encodedWord)