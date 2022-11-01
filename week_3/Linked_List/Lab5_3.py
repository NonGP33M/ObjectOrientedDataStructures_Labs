# Chapter : 5 - item : 3 - รวม Linked List

# ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง

class LinkList():
    class Node():
        def __init__(self,data,prev = None):
            self.prev = prev
            self.data = data
            self.next = None

        def __str__(self):
            return self.data

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self,item):
        temp = self.head
        for i in range(self.size) :
            if temp.data == item :
                return i
            temp = temp.next
        return -1

    def isIn(self,item):
        return self.indexOf(item) >= 0

    def append(self,item):
        if (self.head is None):
            self.head = self.Node(item)
            self.tail = self.head
        else:
            self.tail.next = self.Node(item,self.tail)
            self.tail = self.tail.next
        self.size += 1

    def addHead(self,item):
        if(not self.isEmpty()):
            temp = self.head
            self.head = self.Node(item)
            self.head.next = temp
            self.head.next.prev = self.head
            self.size += 1
        else:
            self.append(item)

    def remove(self,item):
        if(self.isIn(item)):
            if(self.indexOf(item) == 0):
                self.popHead()
            else:
                temp = self.head
                for i in range(self.indexOf(item)):
                    temp = temp.next
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.size -= 1

    def pop(self):
        temp = self.tail.data
        if(self.tail != None):
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head = None
        self.size -= 1
        return temp

    def popHead(self):
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp

    def insert(self, index, data):
        if(index >= 0 and index <= self.size):
            if(index == self.size):
                self.append(data)
            elif(index == 0):
                self.addHead(data)
            else:
                new = self.Node(data)
                temp = self.head
                for i in range(index):
                    if(temp.next is not None):
                        temp = temp.next
                temp.prev.next = new
                new.prev = temp.prev
                temp.prev = new 
                new.next = temp
                self.size += 1
                
    def __str__(self):
        string = ""
        temp = self.head
        for i in range(self.size):
            string += str(temp.data) + " " 
            temp = temp.next
        return string

    def str_reverse(self):
        string = ""
        temp = self.tail
        for i in range(self.size):
            if(temp != self.head):
                string += str(temp.data) + " " 
            else:
                string += str(temp.data)
            temp = temp.prev
        return string

x = input("Enter Input (L1,L2) : ").split()
l1 = LinkList()
l2 = LinkList()
y = x[0].split('->')
z = x[1].split('->')
for i in y:
    l1.append(i)
for i in z:
    l2.append(i)
print("L1    : "+str(l1))
print("L2    : "+str(l2))
print("Merge : "+str(l1)+str(l2.str_reverse()))