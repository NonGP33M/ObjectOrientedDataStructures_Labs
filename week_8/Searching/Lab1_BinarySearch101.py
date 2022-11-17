'''

Chapter : 10 - item : 1 - หัดใช้ Binary Search

ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

def bi_search(l, r, arr, x):
    # Code Here

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

'''

def bi_search(l, r, arr, x):
    mid = int((l+r)/2)
    if l==r:
        if arr[r] == x:
            return True
        else:
            return False
    if(arr[mid]>=x):
        r=mid
    elif arr[mid]<x:
        l=mid+1
    return bi_search(l,r,arr,x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))