print("*** Fun with countdown ***")
x = input("Enter List : ").split()
y = [int(i) for i in x]
y.append(0)
a = 0
templst = []
lst = []
for i in range(len(y)-1):
    if(y[i] == y[i+1]+1 or y[i] == 1):
        templst.append(y[i])
        if(y[i] == 1):
            lst.append(templst)
            templst = []
            a += 1
templst.append(a)
templst.append(lst)
print(templst)