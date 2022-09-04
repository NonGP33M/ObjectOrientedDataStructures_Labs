# Chapter : 3 - item : 1 - รู้จักกับ STACK

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



# A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

# P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

# *** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

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
