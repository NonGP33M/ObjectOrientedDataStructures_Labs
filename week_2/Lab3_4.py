class Stack:

    def __init__(self):
        self.order = []
        self.x = []
        self.ls = []
        self.c = 0
        self.temp = 0

    def getOrder(self,order):
        self.order = order
        for i in range(len(self.order)):
            self.x = self.order[i].split()
            if(self.x[0] == 'A'):
                self.ls.append(int(self.x[1]))
            else:
                self.count()
    def count(self):

        for i in reversed(range(len(self.ls))):
            if(self.temp < self.ls[i]):
                self.temp = self.ls[i]
                self.c += 1
        print(self.c)
        self.c = 0
        self.temp = 0



S = Stack()
inp = input('Enter Input : ').split(',')

S.getOrder(inp)