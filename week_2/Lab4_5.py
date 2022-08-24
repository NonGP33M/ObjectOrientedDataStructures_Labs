stk = input("Enter Input (Normal, Mirror) : ").split()
norStk,mirStk = [],[]
norLft,mirLft = [],[]
checkLft = []
tmpBmb = ''
item = []
isExplode = 0
out = 0
mirBmb = 0
norBmb = 0
intFailed = 0

for i in stk[1]:
    mirStk.append(i)
for i in stk[0]:
    norStk.append(i)

while(isExplode == 0 and out == 0):
    isExplode = 0
    checkLft = []
    for i in range(len(mirStk)):
        mirLft.append(mirStk.pop())
        if(len(mirLft) >= 3):
            if(mirLft[-1] == mirLft[-2] == mirLft[-3]):
                item.append(mirLft.pop())
                mirLft.pop()
                mirLft.pop()
                mirBmb += 1
                isExplode = 1
            if(isExplode == 0 and mirLft[-1] != mirLft[-2] != mirLft[-3]):
                out = 1
    for i in range(len(mirLft)):
        checkLft.append(mirLft.pop(0))
       
        if(len(checkLft) >= 3):
            if(checkLft[-1] == checkLft[-2] == checkLft[-3]):
                item.append(checkLft.pop())
                checkLft.pop()
                checkLft.pop()
                mirBmb += 1
                isExplode = 1
            if(isExplode == 0 and checkLft[-1] != checkLft[-2] != checkLft[-3]):
                out = 1
    mirLft = list(checkLft)
                
isExplode,out = 0, 0
while(isExplode == 0 and out == 0):
    isExplode = 0
    checkLft = []
    for i in range(len(norStk)):
        norLft.append(norStk.pop(0))
        if(len(norLft) >= 3):
            if(norLft[-1] == norLft[-2] == norLft[-3]):
                if(len(item) > 0):
                    tmpBmb = norLft.pop()
                    norLft.append(item.pop(0))
                    norLft.append(tmpBmb)
                    if(norLft[-1] == norLft[-2] == norLft[-3]):
                        norLft.pop()
                        norLft.pop()
                        norLft.pop()
                        intFailed += 1
                        isExplode = 1

                else:
                    norLft.pop()
                    norLft.pop()
                    norLft.pop()
                    norBmb += 1
                    isExplode = 1

                if(isExplode == 0 and norLft[-1] != norLft[-2] != norLft[-3]):
                    out = 1
    
    for i in range(len(norLft)):
        checkLft.append(norLft.pop(0))
       
        if(len(checkLft) >= 3):
            if(checkLft[-1] == checkLft[-2] == checkLft[-3]):
                item.append(checkLft.pop())
                checkLft.pop()
                checkLft.pop()
                norBmb += 1
                isExplode = 1
            if(isExplode == 0 and checkLft[-1] != checkLft[-2] != checkLft[-3]):
                out = 1
    norLft = list(checkLft)
        
print("NORMAL :")
print(len(norLft))
if(len(norLft) != 0):
    print(''.join(norLft[::-1]))
else:
    print("Empty")
print(str(norBmb),"Explosive(s) ! ! ! (NORMAL)")
if(intFailed > 0):
    print("Failed Interrupted", str(intFailed), "Bomb(s)")

print("------------MIRROR------------")

print(": RORRIM")
print(len(mirLft))
if(len(mirLft) != 0):
    print(''.join(mirLft[::-1]))
else:
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE", str(mirBmb))

