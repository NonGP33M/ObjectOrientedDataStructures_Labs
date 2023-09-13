'''

Chapter : 6 - item : 2 - Palindrome

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่

'''

def isPalindrome(value):
    if len(value) < 2: return True
    if value[0] != value[-1]: return False
    return isPalindrome(value[1:-1])

inp = input("Enter Input : ")
if(isPalindrome(inp)):
    print("'{}' is palindrome".format(inp))
else:
    print("'{}' is not palindrome".format(inp))

