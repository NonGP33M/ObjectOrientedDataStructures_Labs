'''

Chapter : 6 - item : 1 - Factorial

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

หา Factorial ของ input ที่รับมา โดยใช้ Recursive

'''

def factorial(value):
    x = value
    if(x <= 1):
        return 1
    else:
        return value*factorial(value-1)

inp = int(input("Enter Number : "))
print(str(inp) + '! = ' + str(factorial(inp)))