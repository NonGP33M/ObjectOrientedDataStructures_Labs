def range(*args):
    start = 0
    end = 0
    step = 1
    a = []
    if(len(args[0]) == 1):
        end = float(args[0][0])

        while(start < end):
            if(start <= end):
                a.append(float(start))
                start += step
        return a

    elif(len(args[0]) == 2):
        start = float(args[0][0])
        end = float(args[0][1])

        while(start < end):
            if(start <= end):
                a.append(float(start))
                start += step
        return a

    else:
        start = float(args[0][0])
        end = float(args[0][1])
        step = float(args[0][2])
        d = args[0][0].split(".")+args[0][1].split(".")+args[0][2].split(".")
        d = sorted(list(map(int,d)))
        d = list(map(str,d))
        nd = len(d[len(d)-1])

        while(start < end):
            if(start <= end):
                a.append(round(float(start),nd))
                start += step
        return a




print("*** New Range ***")
x = input("Enter Input : ").split()
print(tuple(range(x)))
