# Chapter : 1 - item : 1 - รับ h m s --> คำนวณวินาที

# รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
# เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที

# แล้วแสดงผลเป็น วินาที
# แสดงผลตามตัวอย่าง

print("*** Converting hh.mm.ss to seconds ***")
hh,mm,ss = input("Enter hh mm ss : ").split()
h,m,s = int(hh),int(mm),int(ss)
t = (h*3600)+(m*60)+s
if(0<=h and 0<=m<60 and 0<=s<60):
    if(h<10):
        hh = "0"+hh
    if(m<10):
        mm = "0"+mm
    if(s<10):
        ss = "0"+ss
    print(hh+":"+mm+":"+ss,"=","{:,}".format(t),"seconds")
else:
    if(m<0 or m>=60):
        print("mm("+str(m)+")","is invalid!")
    elif(s<0 or s>=60):
        print("ss("+str(s)+")","is invalid!")