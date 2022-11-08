'''

Chapter : 2 - item : 4 - nong saimai

หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล

เช่น

hbd(65) = "saimai is just 21, in base 32!"

hdb(21) = "saimai is just 21, in base 10!"

hdb(8888) = "saimai is just 20, in base 4444!"

'''

def hbd(age):
    if(age%2==0):
        return 20
    else:
        return 21
year = input("Enter year : ")
print("saimai is just",str(hbd(int(year)))+",","in base",str(int(year)//2)+"!")