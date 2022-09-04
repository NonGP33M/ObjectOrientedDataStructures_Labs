class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        cur = self.head
        while cur.next != None: cur = cur.next
        cur.next = new_node

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        cur = self.head
        found = False
        while cur.next != None :
            if cur.value == item : found = True
        return found 

    def index(self, item):
        if item >= self.size() : return None
        cur_idx = 0
        cur_node = self.head
        while True :
            cur_node = cur_node.next
            if cur_idx == item : return cur_node.data
            cur_idx += 1

    def size(self):
        size = 0
        cur = self.head
        while cur.next == None :
            cur = cur.next
            size += 1
        return size

    def pop(self, pos):
        temp = "Out of Range"
        count = 0
        cur = self.head
        while cur.next != None :
            if count+1 == pos :
                temp

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), i[3:]))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)