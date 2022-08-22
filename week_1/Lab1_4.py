print("*** Minesweeper ***")
l = []
x = input("Enter input(5x5) : ").split(",")
for i in x:
    l.append([j for j in i.split()])
print("\n",*l,sep="\n")

for i in range(5):
    for j in range(5):
        if(l[i][j]== '-'):
            l[i][j] = 0
        else:
            l[i][j] = -999

for i in range(5):
    for j in range(5):
        if(l[i][j] < 0):
            if(i-1>=0 and j-1>=0):
                l[i-1][j-1] += 1
            if(i-1>=0):
                l[i-1][j] += 1
            if(i-1>=0 and j+1<5):
                l[i-1][j+1] += 1
            if(j-1>=0):
                l[i][j-1] += 1
            if(j+1<5):
                l[i][j+1] += 1
            if(i+1<5 and j-1>=0):
                l[i+1][j-1] += 1
            if(i+1<5):
                l[i+1][j] += 1
            if(i+1<5 and j+1<5):
                l[i+1][j+1] += 1

for i in range(5):
    for j in range(5):
        if(l[i][j] >= 0):
            l[i][j] = str(l[i][j])
        else:
            l[i][j] = "#"

print("\n",*l,sep="\n")