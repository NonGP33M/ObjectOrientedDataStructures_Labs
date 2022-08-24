temp = []
x = []
for i in range(5):
    x.append(i)

temp = list(x)

for i in range(5):
    x.pop()

print(temp)