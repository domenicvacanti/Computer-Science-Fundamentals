def q1(origString, charsToReplace, count):
    myString =""
    for char in origString:
        charReplacement = char*count
        if (char).lower() in charsToReplace:
           myString += charReplacement
        else:
            myString += char
    return myString

def q2(minLetter, inputString):
    finalCount = 0
    finalLetter = ''
    lastIndex = 0
    for char in inputString:
        checkChar = char.lower()
        count = 0
        for char in inputString:
            if checkChar == char.lower():
                count += 1
        if count > finalCount:
            finalCount = count
            finalChar = checkChar
        elif count == finalCount:
            if finalChar > checkChar:
                finalCount
                finalChar
    for char in inputString:
        if char > minLetter:
            lexiSmall = char
    index = 0
    for char in inputString:
        if lexiSmall == (char).lower():
            break
        elif lexiSmall != (char).lower():
            index += 1
    lexiLexiSmall = None
    for char in inputString:
        if (char).lower() > lexiSmall:
            lexiLexiSmall = char
            break
    if lexiLexiSmall == None:
        lastIndex = None
    else:
        for char in inputString:
            if lexiLexiSmall != (char).lower():
                lastIndex += 1
            elif lexiLexiSmall == (char).lower():
                break
    return (lexiSmall, index, lexiLexiSmall, lastIndex, finalChar, finalCount)

def q3(string1,string2):
    index = 0
    myString = ''
    while index < len(string1):
        if string1[index] == string2[index]:
            myString += string1[index]
        index += 1
    if len(myString) == (len(string1)-1):
        return True
    else:
        return False

def q4(string1, string2):
    myList = []
    myString = ''
    if len(string1) > len(string2):
        myString = string2
    else:
        myString = string1
    for i in range(0,len(myString)):
        if string1[i] == string2[i]:
            myList.append(i)
    return myList