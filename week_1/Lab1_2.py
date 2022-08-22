# Enter your High and Weight : 1.7 70
# More than Normal Weight\
h,w = input("Enter your High and Weight : ").split()
bmi = int(w)/(float(h)**2)
if(bmi<18.5):
    print("Less Weight")
elif(bmi<23):
    print("Normal Weight")
elif(bmi<25):
    print("More than Normal Weight")
elif(bmi<30):
    print("Getting Fat")
else:
    print("Fat")