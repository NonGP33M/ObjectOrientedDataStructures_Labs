'''

Chapter : 2 - item : 2 - Class BUS

ให้เขียนคลาสของรถเมล์ซึ่มีเมท็อดดังนี้
1. __init__ สร้างรถเมล์ 1 คัน รับพารามิเตอร์ จำนวนคนบนรถ people และค่าโดยสาร fare
2. __str__ คืนค่าสตริงซ่ึงบอกจำนวนคนบนรถและค่าโดยสาร
3. __lt__ เปรียบเทียบรถเมล์โดยพิจารณาค่าโดยสารรวมของรถ (จำนวนคนบนรถคูณค่าโดยสารต่อคน)
4. people_in เพิ่มจำนวนคนบนรถ k คน ไม่คืนค่า
5. people_out ลดจำนวนคนบนรถ k คน (หากจำนวนคนน้อยกว่า 0 จะต้องแก้ไขจำนวนคนเป็น 0) ไม่คืนค่า
6. change_fare เปลี่นค่าโดยสารเป็นค่าโดยสารใหม่ new_fare ไม่คืนค่า

โดยให้แก้ไขจากส่วนของโปรแกรมต่อไปนี้ แล้วปรับปรุงให้สามารถแสดงผลได้ตามที่โจทย์กำหนด

class Bus:
    def __init__(people, fare):
        people = people
        fare = fare
    def __str__():
        return 'this bus has ' + str(people) \
        + ' people with fare = ' + str(fare)
    def __lt__(rhs):
        return people*fare < \
                 rhs.people*rhs.fare
    def people_in(k):
        return people += k
    def people_out(k):
        return people -= k
    def change_fare(new_fare):
        return fare = new_fare


การทำงานไม่ถูกต้อง มีจุดผิดดังนี้
- ไม่มีการใช้ self
- เมท็อด people_in, people_out และ change_fare ต้องไม่คืนค่า
- เมท็อด people_out ไม่ได้ตรวจสอบว่า จำนวนคนน้อยกว่าศูนย์หรือไม่

แล้วเพิ่ม code ต่อไปนี้ต่อท้าย class ที่สร้างขึ้นเพื่อส่งงาน

b1, b2, f1, f2 = input("Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()
b1 = Bus(int(b1), int(f1))
b2 = Bus(int(b2), int(f2))
if b1 < b2:
    print(b1)
else:
    print(b2)
b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)

'''
class Bus:
    def __init__(self, people, fare):
        self.people = people
        self.fare = fare
    def __str__(self):
        return 'this bus has ' + str(self.people) \
        + ' people with fare = ' + str(self.fare)
    def __lt__(self,rhs):
        return self.people*self.fare < \
                 rhs.people*rhs.fare
    def people_in(self,k):
        self.people += k
    def people_out(self,k):
        if(self.people - k <= 0):
            self.people = 0
        else:
            self.people -= k
        return self.people
    def change_fare(self,new_fare):
        self.fare = new_fare

b1, b2, f1, f2 = input("Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()
b1 = Bus(int(b1), int(f1))
b2 = Bus(int(b2), int(f2))
if b1 < b2:
    print(b1)
else:
    print(b2)
b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)