x = input("Enter Input : ").split(",")
queue = []
for i in range(len(x)):
    y = x[i].split()
    if(y[0] == 'E'):
        queue.append(y[1])
        print("Add",str(y[1]),"index is",str(len(queue)-1))
    else:
        if(len(queue)>0):
            print("Pop",str(queue.pop(0)),"size in queue is",str(len(queue)))
        else:
            print(-1)
if(len(queue)>0):
    print("Number in Queue is : ",queue)
else:
    print("Empty")
