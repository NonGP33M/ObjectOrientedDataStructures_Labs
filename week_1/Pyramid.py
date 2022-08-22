print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
c = 1
y = 4*x-3
print("#"*y)
print("#."+"."*(y-4*c)+".#")

for i in range(y//2-1):
    if(i!=0 and i%2==0):
        c += 1
        print(("#."*c)+"."*(y-4*c)+(".#"*c))
    elif(i!=0 and i%2!=0):
        print(("#."*c)+"#"*(y-4*c)+(".#"*c))

c+=1

for i in range(y//2-1,0,-1):
    if(i%2!=0):
        c -= 1
        print(("#."*c)+"#"*(y-4*c)+(".#"*c))
    elif(i!=y//2 and i%2==0):
        print(("#."*c)+"."*(y-4*c)+(".#"*c))

print("#."+"."*(y-4*c)+".#")
print("#"*y)
