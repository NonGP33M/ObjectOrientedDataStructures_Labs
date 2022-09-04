class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList():
    def __init__(self, max):
        self.head = None
        self.tail = None
        self.max = max
        self.count = 0
        self.max_length = 1

    def push(self, value):
        node = Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node
        self.count+=1
    
    def sort(self):
        temp = []
        if not self.is_empty():
            while not self.is_empty():
                temp.append(int(self.pop_front()))
            for x in sorted(temp):
                self.push_front(str(x))

    def push_back(self, value):
        node = Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node
        self.count+=1

    def push_front(self, value):
        node = Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.prev, node.next = node, self.tail
            self.tail = node
        self.count+=1

    def pop_front(self):
        temp = self.tail.data
        try:
            self.tail = self.tail.next
            self.tail.prev = None  
            self.count-=1
        except:
            self.head = None
            self.tail = None
            self.count = 0
        return temp

    def __str__(self):
        temp = ''
        current = self.tail
        while current:
            temp += str(current.data) + ' -> '
            current = current.next
        return temp[:-3]

    def get_report(self):
        temp = ''
        current = self.tail
        while current:
            temp += str(current.data) + ' '
            current = current.next
        return temp

    def redix_sort(self):
        box = []
        for i in range(10):
            box.append(LinkedList(0))
        print("------------------------------------------------------------")
        stop = False
        counter = 0
        stop = False
        for i in range(self.max_length+1):
            print("Round : " + str(i+1))
            while not self.is_empty():
                temp = self.pop_front()[::-1]
                try:
                    box[int(temp[i])].push_front(temp[::-1])   
                except:
                    box[0].push_front(temp[::-1])
            if box[0].length() == self.max:
                stop = True
            for j in range(10):
                box[j].sort()
                print(str(j) + ' : ' + box[j].get_report())
                while not box[j].is_empty():
                    temp = box[j].pop_front()
                    self.push_back(temp)
            print("------------------------------------------------------------")
            counter += 1
            if stop:
                break
        self.max_length = counter

    def length(self):
        return self.count

    def get_max_length(self):
        return str(self.max_length-1)

    def is_empty(self):
        return self.count == 0

#inp = "-1 -9 -3 -6 -5 -4 -7 0 -8 -2 3 2 5 1 4 9 8 7 6".split()
inp = input("Enter Input : ").split()

lk_master = LinkedList(len(inp))
lk_org = LinkedList(len(inp))
for x in inp:
    lk_master.push(x)
    lk_org.push(x)

lk_master.redix_sort()
print(lk_master.get_max_length() + ' Time(s)')
print('Before Radix Sort : ' + str(lk_org))
print('After  Radix Sort : ' + str(lk_master))