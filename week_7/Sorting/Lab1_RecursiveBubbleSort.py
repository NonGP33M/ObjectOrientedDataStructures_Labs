'''

Chapter : 9 - item : 1 - bubble sort [recursive]

เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***


'''

def bubbleSort(ar):
   
    # Base Case: If array
    # contains a single element
    if len(ar) <= 1:
        return ar
       
    # Base Case: If array
    # contains two elements
    if len(ar) == 2:
        return ar if ar[0] < ar[1] else [ar[1], ar[0]]
 
    # Store the first two elements
    # of the list in variables a and b
    a, b = ar[0], ar[1]
 
    # Store remaining elements
    # in the list bs
    bs = ar[2:]
 
    # Store the list after
    # each recursive call
    res = []
     
    # If a < b
    if a < b:
        res = [a] + bubbleSort([b] + bs)
         
    # Otherwise, if b >= a
    else:
        res = [b] + bubbleSort([a] + bs)
         
    # Recursively call for the list
    # less than the last element and
    # and return the newly formed list
    return bubbleSort(res[:-1]) + res[-1:]

inp = list(map(int, input("Enter Input : ").split()))
print(bubbleSort(inp))