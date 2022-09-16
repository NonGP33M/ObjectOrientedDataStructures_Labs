class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.sizes == 0

    def append(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        self.sizes += 1

    def addHead(self, item):
        newNode = Node(item)
        if not self.isEmpty():
            temp = self.head
            self.head = newNode
            self.head.next = temp
            self.head.next.previous = self.head
            self.sizes += 1
        else:
            self.append(item)

    def insert(self, pos, item):
        if self.isEmpty() or pos >= self.sizes:
            self.append(item)
        elif pos == 0 or pos <= -(self.sizes):
            self.addHead(item)
        else:
            newNode = Node(item)
            if pos < 0:
                run = self.tail
                for i in range(-(pos)):
                    run = run.previous
                run.next.previous = newNode
                run.next.previous.next = run.next
                run.next = newNode
                run.next.previous = run
            else:
                run = self.head
                for i in range(pos):
                    run = run.next
                run.previous.next = newNode
                newNode.previous = run.previous
                run.previous = newNode
                newNode.next = run
            self.sizes += 1

    def search(self, item):
        run = self.head
        for i in range(self.sizes):
            if (item.strip(" ") == run.value):
                return 'Found'
            else:
                run = run.next
            return 'Not Found'

    def index(self, item):
        run = self.head
        for i in range(self.sizes):
            if item == run.value:
                return i
            run = run.next
        return -1

    def size(self):
        return self.sizes

    def pop(self, pos):
        run = self.head
        if not self.isEmpty():
            if pos >= self.sizes or pos < 0:
                return 'Out of Range'
            elif pos == 0:
                run = self.head
                if (self.sizes > 1):
                    self.head.next.previous = None
                self.head = self.head.next
                self.sizes -= 1
                return 'Success'

            elif pos == self.sizes-1:
                self.tail = self.tail.previous
                self.tail.next = None
                self.sizes -= 1
                return 'Success'

            else:
                for i in range(pos):
                    run = run.next
                run.previous.next = run.next
                run.next.previous = run.previous
                self.sizes -= 1
                return 'Success'
        else:
            return 'Out of Range'


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())