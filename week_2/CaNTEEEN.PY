class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self,inp):
        self.items.append(inp)

    def dequeue(self):
        return self.items.pop(0)

    def id(self):
        return self.items

    def size(self):
        return len(self.items)
x,y = input("Enter Input : ").split('/')
a = x.split(',')
b = y.split(',')
isAdded = 0
mark = 0
q=Queue()
ID=Queue()
for i in a:
    temp = i.split()
    ID.enqueue(temp[0])
    ID.enqueue(temp[1])
print(ID.id())
# for i in b:
#     isAdded = 0
#     temp = i.split()
#     if(temp[0]=="D"):
#         if(q.__str__()=='[]'):
#             print(q.__str__())
#             print("Empty")
#         else:
#             if(q.__str__()=='[]'):
#                 q.dequeue()
#             else:
#                 print(qlst[0].pop(0))
#             if(qlst[0]==[]):
#                 qlst.pop(0)
