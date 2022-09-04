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