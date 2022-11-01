# Chapter : 5 - item : 4 - VIM Text Editor

# กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

# ***** อธิบาย Input 5 แบบ *****

# 1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

# 2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

# 4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

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
                
    def __str__(self):
        string = ""
        temp = self.head
        for i in range(self.size):
            if(temp != self.tail):
                string += str(temp.data) + " " 
            else:
                string += str(temp.data)
            temp = temp.next
        return string

x = input("Enter Input : ").split(',')
ll = LinkList()
ll.append('|')
for i in x:
    y = i.split()
    curpos = ll.indexOf('|')
    if(y[0] == 'I'):
        ll.insert(ll.indexOf('|'),y[1])
    elif(y[0] == 'L'):
        if(curpos == 0):
            pass
        else:
            ll.remove('|')
            ll.insert(curpos-1,'|')
    elif(y[0] == 'R'):
        if(curpos == ll.getSize()-1):
            pass
        else:
            ll.remove('|')
            ll.insert(curpos+1,'|')
    elif(y[0] == 'B'):
        if(curpos == 0):
            pass
        else:
            ll.remove(ll.findIndex(curpos-1))
    else:
        if(curpos == ll.getSize()-1):
            pass
        else:
            ll.remove(ll.findIndex(curpos+1))
print(ll)