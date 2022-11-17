'''

Chapter : 5 - item : 1 - Locomotive-(101)

มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list) 


 *** Locomotive ***
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1


 *** Locomotive ***
Enter Input : 1 2 3 0
Before : 1 <- 2 <- 3 <- 0
After : 0 <- 1 <- 2 <- 3

'''

class LinkList():
    class Node():
        def __init__(self,data):
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
        return self.size() == 0

    def indexOf(self,item):
        temp = self.head
        for i in range(self.size()) :
            if temp.data == item :
                return i
            temp = temp.next
        return -1

    def isIn(self,item):
        return self.indexOf(item) >= 0

    def push(self,item):
        if (self.head is None):
            self.head = self.Node(item)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = self.Node(item)
            self.tail = self.tail.next
            self.size += 1

    def addHead(self,item):
        self.head.next = self.head
        self.head = self.Node(item)
        self.size += 1

    def popHead(self):
        temp = self.head
        self.head = self.head.next
        return temp

    def __str__(self):
        string = ''
        temp = self.head
        while (temp.next is not None):
            if(temp.next != self.tail):
                string += str(temp.data) + " <- " 
            else:
                string += str(temp.data) + " <- " + str(temp.next.data)
            temp = temp.next
        return string


print(' *** Locomotive ***')
x = input('Enter Input : ').split()
ll = LinkList()
for i in x:
    ll.push(i)
print("Before : "+str(ll))

while(ll.head.data != "0"):
    ll.push(ll.head.data)
    ll.popHead()
print("After : "+str(ll))
