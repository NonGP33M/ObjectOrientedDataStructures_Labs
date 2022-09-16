# Chapter : 6 - item : 3 - ( 2^(input) ) - 1

# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 

# *** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11

def binary(value,l):
    if(value >= 0):
        binary(value-1,l)
        print(bin(value)[2:].zfill(l))

inp = int(input("Enter Number : "))
if(inp < 0):
    print("Only Positive & Zero Number ! ! !")
else:
    l = len(str(bin(2**inp-1)[2:]))
    binary(2**inp-1,l)