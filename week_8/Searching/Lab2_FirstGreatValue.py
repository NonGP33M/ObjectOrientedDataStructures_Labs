'''

Chapter : 10 - item : 2 - First Greater Value

ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

'''

def findUpperBound(l,r,arr,x):
    mid = int((l+r)/2)
    if l==r:
        if r == len(arr)-1:
            return 'No First Greater Value'
        else:
            return str(arr[mid])
    if arr[mid] <= x:
        l = mid+1
    elif arr[mid] > x :
        r = mid
    return findUpperBound(l,r,arr,x)
inp1,inp2=input('Enter Input : ').split('/')
inp1=[int(e) for e in inp1.split()]
inp2=[int(e) for e in inp2.split()]
for i in inp2:
    print(findUpperBound(0,len(inp1)-1,sorted(inp1),i))