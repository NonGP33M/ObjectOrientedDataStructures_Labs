'''

Chapter : 2 - item : 1 - Simple OOP Calculator

จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)

'''
class Calculator :

    def __init__(self,value):
        self.value = value

    def __add__(self,other):

        return self.value + other.value

    def __sub__(self,other):

        return self.value - other.value

    def __mul__(self,other):

        return self.value * other.value

    def __truediv__(self,other):

        return self.value / other.value

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")