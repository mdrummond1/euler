def listMulThree():
    for num in range(1000):
        if (num % 3 == 0):
            print(num)

def listMulFive():
    for num in range(1000):
        if (num % 5 == 0):
            print(num)

def addMuls():
    sum = 0
    for num in range(1000):
        if (num % 3) == 0:
            sum += num
        if (num % 3) == 0 and (num % 5) == 0:
            continue
        if (num % 5) == 0:
            sum += num

    return sum

listMulThree()
listMulFive()
print("Sum of all multiples of three or five is %i" % (addMuls()))