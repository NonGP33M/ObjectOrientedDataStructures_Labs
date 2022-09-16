a = input("Enter expresion : ")
list(a)
s = []
for i in range(len(a)):
    if a[i] == '{' or a[i] == '}' or a[i] == '[' or a[i] == ']' or a[i] == '(' or a[i] == ')':
        s.append(a[i])
s = ''.join(s)

stack = []
check = True
for i in range(len(s)):
    if s[i] == '{' or s[i] == '[' or s[i] == '(':
        stack.append(s[i])

    try:
        if s[i] == '}':
            if stack.pop() != '{':
                print(a + " Unmatch open-close")
                check = False
                break

        elif s[i] == ']':
            if stack.pop() != '[':
                print(a + " Unmatch open-close")
                check = False
                break

        elif s[i] == ')':
            if stack.pop() != '(':
                print(a + " Unmatch open-close")
                check = False
                break
    except:
        print(a + " close paren excess")
        check = False
        break

if check:
    if len(stack) != 0:
        print(a + " open paren excess   " + str(len(stack)),end=' : ')
        for item in stack:
            print(item,end='')
    else :
        print(a + " MATCH")
