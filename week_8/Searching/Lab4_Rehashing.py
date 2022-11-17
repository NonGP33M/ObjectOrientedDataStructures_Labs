'''

Chapter : 10 - item : 4 - Rehashing

ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด

'''

class hash:
    def __init__(self,maxSize,maxCol,Threshold):
        self.table=[]
        for i in range(maxSize):
            self.table.append(None)
        self.maxSize=maxSize
        self.maxCol = maxCol
        self.Threshold=Threshold
    def insert(self,value):
        index=0
        if(not self.isFull()):
            index=value%self.maxSize
            if(self.table[index]==None):
                self.table[index]=value
            elif self.table[index]!=None:
                r=0
                newIndex = index
                print('collision number {0} at {1}'.format(r+1,newIndex))
                while(self.table[newIndex]!=None):
                    r+=1 
                    newIndex = (index + (r**2)) % self.maxSize
                    if(self.maxCol <= r):
                        print('****** Max collision - Rehash !!! ******')
                        return False
                    if(self.table[newIndex]==None):
                        self.table[newIndex]=value
                        break
                    #print(self.maxCol)
                    #print(self.nowCol)
                    print('collision number {0} at {1}'.format(r+1,newIndex))
            return True
        else:
            print('****** Data over threshold - Rehash !!! ******')
            return False
    def isFull(self):
        k=int(self.maxSize*self.Threshold/100)
        leng=0
        for i in self.table:
            if i != None:
                leng+=1
        if leng>=k:
            return True
        return False
    
    def print(self):
        for i in range(len(self.table)):
            print('#{0}'.format(i+1),end='')
            print(' '*(7-len(str(i+1))),end='')
            print('{0}'.format(self.table[i]))

def findClosest(value):
    while True:
        value+=1
        for i in range(2,value):
            if value%i==0:
                break
            if i==value-1:
                return value
    
print(' ***** Rehashing *****')
inp1,inp2=input('Enter Input : ').split('/')
sizeTable,maxCol,Threshold=map(int,inp1.split())
inp2=[int(e) for e in inp2.split()]
print('Initial Table :')
global hashTable
hashTable = hash(sizeTable,maxCol,Threshold)
hashTable.print()
print('----------------------------------------')
hashTable.isFull()
lastAdd=-1
notAlldata=True
while(notAlldata):
    for i in range(len(inp2)):
        if(i >= lastAdd+1):
            print('Add : ' + str(inp2[i]))
        if(not hashTable.insert(inp2[i])):
            hashTable=hash(findClosest(hashTable.maxSize*2),maxCol,Threshold)
            lastAdd = i
            break
        else:
            if(i >= lastAdd):
                hashTable.print()
                print('----------------------------------------')
        if i == len(inp2)-1:
            notAlldata=False