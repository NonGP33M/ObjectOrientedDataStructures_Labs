'''

Chapter : 5 - item : 2 - Doubly Linked List(append,insert,remove)

ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า

4. def isEmpty(self): return list นั้นว่างหรือไม่

5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

6. def insert(self, index, data): insert data ใน index ที่กำหนด

7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append       ->  A
2. add_before -> Ab
3. insert          ->   I
4. remove       ->  R

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********


'''

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
        string = "linked list : "
        temp = self.head
        for i in range(self.size):
            if(temp != self.tail):
                string += str(temp.data) + "->" 
            else:
                string += str(temp.data)
            temp = temp.next
        return string

    def str_reverse(self):
        string = "reverse : "
        temp = self.tail
        for i in range(self.size):
            if(temp != self.head):
                string += str(temp.data) + "->" 
            else:
                string += str(temp.data)
            temp = temp.prev
        return string

x = input("Enter Input : ").split(',')
ll = LinkList()
for i in x:
    y = i.split()
    if(y[0] == 'A'):
        ll.append(y[1])
    elif(y[0] == 'Ab'):
        ll.addHead(y[1])
    elif(y[0] == 'I'):
        t1,t2 = y[1].split(':')
        if(int(t1) < 0 or int(t1) > ll.size):
            print("Data cannot be added")
        else:
            print("index = " + t1 + " and data = " + t2)
            ll.insert(int(t1),t2)
    else:
        if(ll.isEmpty() or not ll.isIn(y[1])):
            print("Not Found!")
        else:
            print("removed : " + y[1] + " from index : " + str(ll.indexOf(y[1])))
            ll.remove(y[1])
    print(ll)
    print(ll.str_reverse())