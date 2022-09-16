# Chapter : 5 - item : 5 - Radix Sort (มากไปน้อย)

# ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย

# โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

class LinkList():
    class Node():
        def __init__(self,data,prev = None):
            self.prev = prev
            self.data = data
            self.next = None
            self.digit = None

        def __str__(self):
            return self.data

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
        self.mod = 10
        self.count = 1
        self.div = 1

    def getSize(self):
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

    def findIndex(self,index):
        temp = self.head
        for i in range(self.size) :
            if i == index :
                return temp.data
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
            elif(self.indexOf(item) == self.size - 1):
                self.pop()
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

    def radixSort(self):
        allMoved = False
        while(not allMoved):
            allMoved = True
            present = self.head
            for i in range(self.getSize()):
                if(present != self.tail):
                    present = present.next
                temp = present.prev.data
                if(int(temp) < int(present.data)):
                    self.remove(temp)
                    self.append(temp)
                    allMoved = False

        present = self.head
        for i in range(self.getSize()):
            present = present.next
            if(present is None):
                temp = self.tail
            else:
                temp = present.prev
            check = abs(int(temp.data))//self.div
            for j in range(10):
                if(check%self.mod == j):
                    temp.digit = j

        print("Round :",self.count)
        for i in range(10):
            string = str(i)+" :"
            present = self.head
            for j in range(self.size):
                if(present.digit == i):
                    string += " "+str(present.data)
                present =  present.next
            print(string)
        self.count += 1
        self.div *= 10
        print("------------------------------------------------------------")

    def allInZero(self):
        temp = self.head
        for i in range(self.size):
            if(temp.digit != 0):
                return 0
            temp = temp.next
        return 1

    def getTime(self):
        return self.count-2
                
    def __str__(self):
        string = ''
        temp = self.head
        while (temp.next is not None):
            if(temp.next != self.tail):
                string += str(temp.data) + " -> " 
            else:
                string += str(temp.data) + " -> " + str(temp.next.data)
            temp = temp.next
        return string

x = input("Enter Input : ").split()
ll = LinkList()
nll = LinkList()
for i in x:
    ll.append(i)
    nll.append(i)
print("------------------------------------------------------------")
while(not nll.allInZero()):
    nll.radixSort()
print(str(nll.getTime()),"Time(s)")
print("Before Radix Sort : " + str(ll))
print("After  Radix Sort : " + str(nll))
