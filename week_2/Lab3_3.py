# Chapter : 3 - item : 3 - Infix to Postfix

#  ส่งมาแล้ว 1 ครั้ง
# ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^



class Stack:
    def __init__(self):
        self.stack = []
        self.output = []
    def push(self, value):
        for i in value:
            if(i not in oprtr):
                self.output.append(i)
            elif(i == '('):
                self.stack.append('(')
            elif(i == ')'):
                while(self.stack and self.stack[-1] != '('):
                    self.output.append(self.stack.pop())
                self.stack.pop()
            else:
                while(self.stack and self.stack[-1] != '(' and priority[self.stack[-1]] >= priority[i]):
                    self.output.append(self.stack.pop())
                self.stack.append(i)

        while(self.stack):
            self.output.append(self.stack.pop()) 
        
    def pop(self):
        return self.output.pop(0)

    def size(self):
        return len(self.output)

    def isEmpty(self):
        return self.size() == 0
inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

oprtr = ['+','-','*','/','^','(',')']
priority = {'+':1,'-':1,'*':2,'/':2,'^':3}

S.push(inp)

while not S.isEmpty():

    print(S.pop(), end='')

print()