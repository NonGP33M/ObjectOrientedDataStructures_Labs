# Chapter : 6 - item : 2 - Palindrome

# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่

def isPalindrome(value):
    return value == value[::-1]

inp = input("Enter Input : ")
if(isPalindrome(inp)):
    print("'{}' is palindrome".format(inp))
else:
    print("'{}' is not palindrome".format(inp))

