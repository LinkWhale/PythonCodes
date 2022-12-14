total = 0
startnum = int(input("input starting number"))
lastnum = int(input("input last number"))
for x in range(startnum,lastnum + 1,2):
    total += x
    print(total)
