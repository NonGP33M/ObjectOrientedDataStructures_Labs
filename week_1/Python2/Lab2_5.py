# Chapter : 2 - item : 5 - รหัสลับ

# ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
# โดยรหัสจะประกอบไปด้วย english word that have repeat character
# เช่น bon("ball") = 48 หรือ bon("aah") = 4

def bon(w):
    a = [i for i in w]
    b = max(set(a), key=a.count)
    return (ord(b) - 96)*4
    
secretCode = input("Enter secret code : ")
print(bon(secretCode))
#repeat character * 4