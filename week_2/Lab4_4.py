x,y = input("Enter Input : ").split('/')
a = x.split(',')
b = y.split(',')
ID = []
isAdded = 0
mark = 0
qlst = []

for i in a:
    temp = i.split()
    ID.append(temp[0])
    ID.append(temp[1])

for i in b:
    isAdded = 0
    temp = i.split()
    if(temp[0]=="D"):
        if(qlst==[]):
            print("Empty")
        else:
            if(qlst[0]==[]):
                qlst.pop(0)
            else:
                print(qlst[0].pop(0))
                if(qlst[0]==[]):
                    qlst.pop(0)
    else:
        if(qlst==[]):
            qlst.append([])
            qlst[0].append(temp[1])
        else:
            mark = ID[ID.index(temp[1])-1]
            for j in range(len(qlst)):
                if(ID[ID.index(qlst[j][0])-1] == mark and isAdded == 0):
                    qlst[j].append(temp[1])
                    isAdded = 1
            if(isAdded == 0):
                qlst.append([])
                qlst[len(qlst)-1].append(temp[1])
