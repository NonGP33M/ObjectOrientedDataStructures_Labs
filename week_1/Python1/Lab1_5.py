# Chapter : 1 - item : 5 - Countdown มหาสนุก

# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ

#     โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

print("*** Fun with countdown ***")
x = input("Enter List : ").split()
y = [int(i) for i in x]
y.append(0)
a = 0
templst = []
lst = []
for i in range(len(y)-1):
    if(y[i] == y[i+1]+1 or y[i] == 1):
        templst.append(y[i])
        if(y[i] == 1):
            lst.append(templst)
            templst = []
            a += 1
templst.append(a)
templst.append(lst)
print(templst)