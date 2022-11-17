'''

Chapter : 9 - item : 3 - insertion sort [recursive]

เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

'''

def findPlace(lis,value,index=0):
    if index == len(lis):
        return index
    if lis[index]>=value:
        return index
    return findPlace(lis,value,index+1)
def insertionSort(st,lis,index=0):
    if len(lis)==0:
        return st
    placeIndex=findPlace(st,lis[index])
    if placeIndex == -1:
        temp=[]
        temp.append(lis[index])
        st=temp+st
        num=lis.pop(0)
        print('insert {0} at index {1} : '.format(num,0)+str(st),end='')
        if len(lis)!=0:
            print(' '+str(lis))
        else:
            print('')
    elif placeIndex == len(st):
        st.append(lis[index])
        num=lis.pop(0)
        print('insert {0} at index {1} : '.format(num,len(st)-1)+str(st),end='')
        if len(lis)!=0:
            print(' '+str(lis))
        else:
            print('')
    else:
        temp1=st[:placeIndex]
        temp2=st[placeIndex:]
        temp3=[]
        temp3.append(lis[index])
        st=temp1+temp3+temp2
        num=lis.pop(0)
        print('insert {0} at index {1} : '.format(num,placeIndex)+str(st),end='')
        if len(lis)!=0:
            print(' '+str(lis))
        else:
            print('')
    return insertionSort(st,lis)
inp=[int(e) for e in input('Enter Input : ').split()]
lis1 = inp[0:1]
lis2 = inp[1:]
sorted_list=insertionSort(lis1,lis2)

print('sorted')
print(sorted_list)