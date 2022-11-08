'''

Chapter : 4 - item : 3 - Secret Message

จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue

รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :

    - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)

    - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 

***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

โดยรูปแบบการ run ดังนี้ :

q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)

'''

class Queue():
    def __init__(self,code):
        self.code = code.replace(' ','')
        self.lst1 = [i for i in self.code]

    def enqueue(self,inp):
        self.lst1.append(inp)

    def dequeue(self):
        return self.lst1.pop(0)

    def retlst(self):
        return self.lst1

    def items(self):
        return self.code

    def size(self):
        return len(self.code)

def encodemsg(a,b):
    for i in range(a.size()):
        currentchr = a.items()[i]
        currentnum = int(b.retlst()[i])
        newchr = ord(currentchr)+currentnum
        b.enqueue(b.retlst()[i])

        if(currentchr.isupper()):
            if(ord(currentchr)+currentnum > ord("Z")):
                a.enqueue(chr(newchr-26))
            else:
                a.enqueue(chr(newchr))
        elif(currentchr.islower()):
            if(newchr > ord("z")):
                a.enqueue(chr(newchr-26))
            else:
                a.enqueue(chr(newchr))

        a.dequeue()
    print("Encode message is :  ",end='')
    print(a.retlst())

def decodemsg(a,b):
    for i in range(a.size()):
        currentchr = a.retlst()[0]
        currentnum = int(b.retlst()[i])
        newchr = ord(currentchr)-currentnum
        b.enqueue(b.retlst()[i])

        if(currentchr.isupper()):
            if(newchr < ord("A")):
                a.enqueue(chr(newchr+26))
            else:
                a.enqueue(chr(newchr))
        elif(currentchr.islower()):
            if(newchr < ord("a")):
                a.enqueue(chr(newchr+26))
            else:
                a.enqueue(chr(newchr))

        a.dequeue()
    print("Decode message is :  ",end='')
    print(a.retlst())

temp = 0
x = input("Enter String and Code : ").split(',')
string,number = x[0],x[1]
q1 = Queue(string)
q2 = Queue(number)

encodemsg(q1, q2)
decodemsg(q1, q2)