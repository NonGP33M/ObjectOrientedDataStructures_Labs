x = input("Enter Input : ").split(",")

def ManageStack(arg):
    stack = []
    delete = []
    temp = []
    for i in range(len(arg)):
        y = x[i].split()
        if(y[0]=='A'):
            stack.append(int(y[1]))
            print("Add =",str(y[1]))
        elif(y[0]=='P'):
            if(len(stack)>0):
                print("Pop =",stack.pop())
            else:
                print(-1)
        elif(y[0]=='D'):
            if(len(stack)>0):
                for j in range(len(stack)):
                    if(stack[j]!=int(y[1])):
                        temp.append(int(stack[j]))
                    else:
                        delete.append(int(stack[j]))
                    if(len(delete)!=0):
                        print("Delete =",delete.pop())
                stack = temp
                temp = []
            else:
                print(-1)
        elif(y[0]=='LD'):
            if(len(stack)>0):
                for j in range(len(stack)):
                    if(stack[j]>=int(y[1])):
                        temp.append(int(stack[j]))
                    else:
                        delete.append(int(stack[j]))
                stack = temp
                temp = []
                for j in reversed(range(len(delete))):
                    print("Delete =",str(delete[j]),"Because",str(delete[j]),"is less than",str(y[1]))
                delete = []
            else:
                print(-1)
        else:
            if(len(stack)>0):
                for j in range(len(stack)):
                    if(stack[j]<=int(y[1])):
                        temp.append(int(stack[j]))
                    else:
                        delete.append(int(stack[j]))
                stack = temp
                temp = []
                for j in reversed(range(len(delete))):
                    print("Delete =",str(delete[j]),"Because",str(delete[j]),"is more than",str(y[1]))
                delete = []
            else:
                print(-1)
    return stack

print("Value in Stack =",ManageStack(x))