class Stack :

    def __init__(self):
        self.newnum = 0
        self.decnum = 0
        self.x = []

    def convert(self,decnum):
        self.decnum = decnum
        while(self.decnum != 0):
            self.newnum = self.decnum%2
            self.x.append(self.newnum)
            self.decnum = self.decnum//2
        return self.x

def dec2bin(decnum):
    s = Stack()
    a = ""
    y = s.convert(decnum)
    for i in range(len(y)):
        a += str(y.pop())
    return a


print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))
