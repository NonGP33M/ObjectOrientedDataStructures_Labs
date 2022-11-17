'''

Chapter : 10 - item : 3 - Fun with hashing

ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ



class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    # Code Here

'''

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,maxSize,maxCol,nowCol=0):
        self.table=[]
        for i in range(maxSize):
            self.table.append(None)
        self.maxSize=maxSize
        self.maxCol = maxCol

    def insert(self,key,value):
        index=0
        if(not self.isFull()):
            for cha in list(key):
                index+=ord(cha)%self.maxSize
            index%=self.maxSize
            if(self.table[index]==None):
                self.table[index]=Data(key,value)
            elif self.table[index]!=None:
                r=0
                newIndex = index
                print('collision number {0} at {1}'.format(r+1,newIndex))
                while(self.table[newIndex]!=None):
                    r+=1 
                    newIndex = (index + (r**2)) % self.maxSize
                    if(self.table[newIndex]==None):
                        self.table[newIndex]=Data(key,value)
                        break
                    #print(self.maxCol)
                    #print(self.nowCol)
                    if(self.maxCol <= r):
                        print('Max of collisionChain')
                        break  
                    print('collision number {0} at {1}'.format(r+1,newIndex))
            return True
        else:
            return False
    def isFull(self):
        for i in self.table:
            if i == None:
                return False
        return True
    
    def print(self):
        for i in range(len(self.table)):
            print('#{0}      {1}'.format(i+1,self.table[i]))

print(' ***** Fun with hashing *****')
inp1,inp2=input('Enter Input : ').split('/')
sizeTable,maxCol=inp1.split()
inp2=[e for e in inp2.split(',')]
hashTable = hash(int(sizeTable),int(maxCol))
for i in inp2:
    if(hashTable.insert(i.split()[0],i.split()[1])):
        hashTable.print()
        print('---------------------------')
    else:
        print('This table is full !!!!!!')
        break