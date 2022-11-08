'''

Chapter : 1 - item : 3 - loop

จงเขียนโปรแกรมรับตัวเลขจำนวนเต็ม ไม่เกิน 30 หลัก แล้วหาผลรวมของเลขโดด แต่ละหลัก 

รับตัวเลข 123 => 1+2+3=6
รับตัวเลข 7892 => 7+8+9+2=26 
รับตัวเลข 32189657 => 3+2+1+8+9+6+5+7=41

'''

print(" *** Summation of each digit ***")
x = input("Enter a positive number : ")
t = 0
for i in x:
    t += int(i)
print("Summation of each digit = ",str(t))