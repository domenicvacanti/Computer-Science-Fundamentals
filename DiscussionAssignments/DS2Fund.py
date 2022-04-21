#Domenic Vacanti DS2
def q1(num):
    if num > 0:
        if num % 14 == 0:
            print("{} is a multiple of 14".format(num))
        elif num % 7 == 0:
            print("{} is a multiple of 7".format(num))
        elif num % 2 == 0:
            print("{} is a multiple of 2".format(num))
        else:
            print("{} is not a multiple of 2, 7, or 14".format(num))
    else:
        print("{} is not a multiple of 2, 7, or 14".format(num))
    return
        
def q2(n):
    otherN = 1
    while n > 0:
        printState = q1(otherN)
        if printState != None:
            print(printState)
        else:
            printState
        n = n -1
        otherN = otherN + 1
    return

def printDigitsOf(number):
    while number > 0:
        printNum = number % 10
        print(printNum)
        number = number //10
    return
        
def sumDigitsOf(n):
    result = 0
    while n > 0:
        addNum = n % 10
        result = result + addNum
        n = n // 10
    return result