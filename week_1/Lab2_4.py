def hbd(age):
    if(age%2==0):
        return 20
    else:
        return 21
year = input("Enter year : ")
print("saimai is just",str(hbd(int(year)))+",","in base",str(int(year)//2)+"!")