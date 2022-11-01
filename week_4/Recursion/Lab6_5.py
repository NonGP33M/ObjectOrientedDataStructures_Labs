# Chapter : 6 - item : 5 - ดาวเคราะห์น้อย

# นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
# สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

# ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

# 1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

# 2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

# 3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def asteroid_collision(asts,idx):
    if idx == -1:
        return asts
    temp=asteroid_collision(asts,idx-1)
    nowAst=temp[idx]
    if nowAst > 0 and idx < len(temp)-1:
        newAst = temp[idx+1]
        if newAst < 0:
            if abs(newAst) < nowAst:
               temp[idx+1]=nowAst
               temp[idx]=0
               temp = asteroid_collision(temp,idx+1)
            elif abs(newAst) > nowAst:
                temp[idx] = newAst
                temp[idx+1]=0
                temp = asteroid_collision(temp,idx)
            else:
                temp[idx]=0
                temp[idx+1]=0
        if newAst==0:
            temp[idx+1]=nowAst
            temp[idx]=0
            temp=asteroid_collision(temp,idx+1)
    if nowAst < 0 and idx > 0:
        newAst = temp[idx-1]
        if newAst > 0:
            if abs(nowAst) < newAst:
                temp[idx]=newAst
                temp[idx-1]=0
                temp = asteroid_collision(temp,idx)
            elif abs(nowAst) > newAst:
                temp[idx-1]=nowAst
                temp[idx]=0
                temp = asteroid_collision(temp,idx-1)
            else:
                temp[idx]=0
                temp[idx-1]=0
        if newAst==0:
            temp[idx-1]=nowAst
            temp[idx]=0
            temp=asteroid_collision(temp,idx-1)
    return temp

inp = input("Enter Input : ").split(",")
inp = list(map(int,inp))
print(str(asteroid_collision(inp,len(inp)-1)).replace(' 0,','').replace('[0, ','[').replace(', 0]',']').replace('[0]','[]'))