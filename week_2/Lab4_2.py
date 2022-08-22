x = input("Enter Input : ").split(",")
queueN = []
queueS = []
for i in range(len(x)):
    y = x[i].split()
    if(y[0] == 'EN'):
        queueN.append(y[1])
    elif(y[0] == 'ES'):
        queueS.append(y[1])
    else:
        if(len(queueS)>0):
            print(queueS.pop(0))
        elif(len(queueN)>0):
            print(queueN.pop(0))
        else:
            print("Empty")