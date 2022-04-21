def q1(n):
    if n == 0:
        result = [1]
        return result
    else:
        theResult = [(n+1)**2]
        return q1(n-1) + theResult + q1(n-1)
    

def q2(listOfStrings, n):
    if listOfStrings == []:
        return 0
    if len(listOfStrings[0]) > n:
        return 1 + q2(listOfStrings[1:],n)
    else:
        return q2(listOfStrings[1:],n)
    
def q3(item1,item2):
    if type(item1) == type(item2) or ((type(item1) == int) and (type(item2) == float)) or ((type(item2) == int) and (type(item1) == float)):
        if (type(item1) == list) and (type(item2) == list):
            if len(item1) == len(item2):
                if (len(item1) == 0) and (len(item2) == 0):
                    return True
                if (type(item1[0]) == list) and (type(item2[0]) == list):
                    print(item1, "       ",  item2)
                    print(type(item1[0]), "       ", type(item2[0]))                    
                    return q3(item1[0],item2[0])
                elif type(item1[0]) == type(item2[0]) or ((type(item1[0]) == int) and (type(item2[0]) == float)) or ((type(item2[0]) == int) and (type(item1[0]) == float)):
                    print(item1, "       ",  item2)
                    print(type(item1[0]), "       ", type(item2[0]))
                    return q3((item1[1:]),(item2[1:]))
                else:
                    return False
            else:
                return False
        else:
            return True
    else:
        return False
    
def q4(inString):
    if len(inString) == 1:
        return [inString]
    else:
        perm = []
        mightBePerm = q4(inString[1:])
        for i in mightBePerm:
            for index in range(len(i)+1):
                thePerm = i[0:index]+inString[0]+i[index:]
                perm.append(thePerm)
        return perm