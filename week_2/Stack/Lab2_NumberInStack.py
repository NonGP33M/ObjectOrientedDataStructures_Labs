'''

Chapter : 3 - item : 2 - Number in Stack

จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***

ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ

'''

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