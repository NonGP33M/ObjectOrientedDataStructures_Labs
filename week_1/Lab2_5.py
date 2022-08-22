def bon(w):
    a = [i for i in w]
    b = max(set(a), key=a.count)
    return (ord(b) - 96)*4
    
secretCode = input("Enter secret code : ")
print(bon(secretCode))
#repeat character * 4