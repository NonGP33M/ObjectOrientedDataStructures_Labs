class Queue():
    def __init__(self,code):
        self.code = code.replace(' ','')
        self.lst1 = [i for i in self.code]

    def enqueue(self,inp):
        self.lst1.append(inp)

    def dequeue(self):
        return self.lst1.pop(0)

    def retlst(self):
        return self.lst1

    def items(self):
        return self.code

    def size(self):
        return len(self.code)

def encodemsg(a,b):
    for i in range(a.size()):
        currentchr = a.items()[i]
        currentnum = int(b.retlst()[i])
        newchr = ord(currentchr)+currentnum
        b.enqueue(b.retlst()[i])

        if(currentchr.isupper()):
            if(ord(currentchr)+currentnum > ord("Z")):
                a.enqueue(chr(newchr-26))
            else:
                a.enqueue(chr(newchr))
        elif(currentchr.islower()):
            if(newchr > ord("z")):
                a.enqueue(chr(newchr-26))
            else:
                a.enqueue(chr(newchr))

        a.dequeue()
    print("Encode message is :  ",end='')
    print(a.retlst())

def decodemsg(a,b):
    for i in range(a.size()):
        currentchr = a.retlst()[0]
        currentnum = int(b.retlst()[i])
        newchr = ord(currentchr)-currentnum
        b.enqueue(b.retlst()[i])

        if(currentchr.isupper()):
            if(newchr < ord("A")):
                a.enqueue(chr(newchr+26))
            else:
                a.enqueue(chr(newchr))
        elif(currentchr.islower()):
            if(newchr < ord("a")):
                a.enqueue(chr(newchr+26))
            else:
                a.enqueue(chr(newchr))

        a.dequeue()
    print("Decode message is :  ",end='')
    print(a.retlst())

temp = 0
x = input("Enter String and Code : ").split(',')
string,number = x[0],x[1]
q1 = Queue(string)
q2 = Queue(number)

encodemsg(q1, q2)
decodemsg(q1, q2)