x = input("Enter Input : ").split(",")
stack = []
for i in range(len(x)):
    y = x[i].split()
    if(y[0] == 'A'):
        stack.append(y[1])
        print("Add =",str(y[1]),"and","Size =",str(len(stack)))
    else:
        if(len(stack)>0):
            print("Pop =",str(stack.pop()),"and","Index =",str(len(stack)))
        else:
            print(-1)
if(len(stack)>0):
    print("Value in Stack =",*stack)
else:
    print("Value in Stack = Empty")
