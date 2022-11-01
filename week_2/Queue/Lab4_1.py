# Chapter : 4 - item : 1 - Basic Queue

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

# D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

#                     หลังจากทำการ dequeue แล้ว

# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***

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
