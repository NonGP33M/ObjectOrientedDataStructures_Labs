'''

Chapter : 4 - item : 4 - Canteen

รงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

'''

x,y = input("Enter Input : ").split('/')
a = x.split(',')
b = y.split(',')
ID = []
isAdded = 0
mark = 0
qlst = []

for i in a:
    temp = i.split()
    ID.append(temp[0])
    ID.append(temp[1])

for i in b:
    isAdded = 0
    temp = i.split()
    if(temp[0]=="D"):
        if(qlst==[]):
            print("Empty")
        else:
            if(qlst[0]==[]):
                qlst.pop(0)
            else:
                print(qlst[0].pop(0))
                if(qlst[0]==[]):
                    qlst.pop(0)
    else:
        if(qlst==[]):
            qlst.append([])
            qlst[0].append(temp[1])
        else:
            mark = ID[ID.index(temp[1])-1]
            for j in range(len(qlst)):
                if(ID[ID.index(qlst[j][0])-1] == mark and isAdded == 0):
                    qlst[j].append(temp[1])
                    isAdded = 1
            if(isAdded == 0):
                qlst.append([])
                qlst[len(qlst)-1].append(temp[1])
