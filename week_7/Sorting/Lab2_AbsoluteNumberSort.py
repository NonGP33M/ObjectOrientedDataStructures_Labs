'''

Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ

ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

'''

def findIndexOfMaxPositive(lists):
    index = None
    for i in range(len(lists)):
        if index == None and lists[i] >= 0:
            index = i
        elif index != None and lists[i] >lists[index]:
            index = i
    return index

def selectionSort(lists):
    for i in range(len(lists)-1,-1,-1):
        if lists[i] >= 0:
            indexOflastPositive = i
            swapIndex = findIndexOfMaxPositive(lists[:indexOflastPositive])
            if swapIndex != None and lists[swapIndex]>=lists[indexOflastPositive]:
                lists[indexOflastPositive],lists[swapIndex] = lists[swapIndex],lists[indexOflastPositive]
    return lists

lists = list(map(int,input("Enter Input : ").split(" ")))
temp = selectionSort(lists)
for i in temp:
    print(i,end=" ")