#Domenic Vacanti
def q1(L, goalX, goalY):
    finalXGoal = 100000000000
    finalYGoal = 100000000000
    lastVar = ""
    for lS in L:
        xGoal = abs(lS[0] - goalX)
        yGoal = abs(lS[1] - goalY)
        if xGoal < finalXGoal:
            finalXGoal = xGoal
            xMax = lS
        if yGoal < finalYGoal:
            finalYGoal = yGoal
            yMax = lS
    if finalXGoal < finalYGoal:
        lastVar += "x"
        finalVar = xMax
    elif finalYGoal < finalXGoal:
        finalVar = yMax
        lastVar += "y"
    return (finalVar, lastVar)

def q2(L):
    listOfSums = []
    totalMoreThanZ = 0
    smallest = L[0][0]
    for lS in L:
        counter = 0
        runningTotal = 0
        counter2 = 0
        while counter < len(lS):
            runningTotal += lS[counter]
            if lS[counter] < 0:
                counter2 += -1
            elif lS[counter] == 0:
                counter2 += 0
            else:
                counter2 += 1
            if lS[counter] < smallest:
                smallest = lS[counter]
            counter += 1
        if counter2 > 0:
            totalMoreThanZ += 1
        listOfSums.append(runningTotal)
    return([listOfSums, totalMoreThanZ, smallest])

def q3(listOfLists, infoDict):
    list1 = []
    list2 = []
    list3 = []
    empt = {}
    counter = 0
    for L in listOfLists:
        colorL = []
        for i in range(0, len(L)):
            if L[i] in infoDict:
                myColor = infoDict[L[i]]
            else:
                myColor = "green"
            colorL.append(myColor)
        list1.append(colorL)
    for L in list1:
        blueCounter = 0
        redCounter = 0
        greenCounter = 0
        for lS in L:
            if lS == 'green':
                greenCounter += 1
            elif lS == 'blue':
                blueCounter += 1
            elif lS == "red":
                redCounter += 1
        if greenCounter > blueCounter and greenCounter > redCounter:
            list2.append("green")
        elif blueCounter > greenCounter and blueCounter > redCounter:
            list2.append("blue")
        else:
            list2.append("red")
    for i in range(0,len(listOfLists)):
        if list2[i] == "red":
            for r in range(0,len(listOfLists[i])):
                firstInList = listOfLists[i][0]
                if firstInList > listOfLists[i][r]:
                    firstInList = listOfLists[i][r]
            list3.append(firstInList)
        elif list2[i] == "blue":
            for r in range(0,len(listOfLists[i])):
                firstInList = listOfLists[i][0]
                if firstInList < listOfLists[i][r]:
                    firstInList = listOfLists[i][r]
            list3.append(firstInList)
        else:
            if len(listOfLists[i]) == 1:
                list3.append(listOfLists[i][0])
            else:
                dict1 = {}
                count, itm = 0, ''
                for item in reversed(listOfLists[i]):
                    dict1[item] = dict1.get(item,0)+1
                    if dict1[item]>=count:
                        count,itm = dict1[item],item
                list3.append(item)
    return list3