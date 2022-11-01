# Chapter : 6 - item : 4 - หอคอยแห่งฮานอย

# เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

# คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
# และให้ระวังเรื่องการสลับ list ให้ดีๆ

# หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html

def move(n, source, dest, aux):
    if (n>0):
        move(n-1, source, aux, dest)
        poleLst[aux-1].append(poleLst[source-1].pop())
        print("move",n,"from ",chr(ord('A')+source-1), "to" ,chr(ord('A')+aux-1))
        print('|  |  |')
        printPole(inp,poleLst[0],poleLst[1],poleLst[2])
        move(n-1, dest, source, aux)

def printPole(n, p1, p2 ,p3):
    if (n!=0):
      if (len(p1) >= n):
         print(p1[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if (len(p2) >= n):
         print(p2[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if (len(p3) >= n):
         print(p3[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      print()
      printPole(n-1,p1,p2,p3)
    else:
        return

def init(n):
    if n == 0:
        return []
    return [n] + init(n-1)

inp = int(input("Enter Input : "))
poleLst = [[],[],[]]
poleLst[0] = init(inp)
print('|  |  |')
printPole(inp,poleLst[0],poleLst[1],poleLst[2])
move(inp,1,2,3)