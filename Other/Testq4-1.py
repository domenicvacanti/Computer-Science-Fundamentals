def q3(listOfLists, vLow, vHigh):
    empt = []
    empt1 = []
    result = 0
    index = 0
    counter = 0
    for L in listOfLists:
        for l in L:
            if l > vLow:
                result += 1
                break
    while index < len(listOfLists[counter]):
        index = 0
        for i in range(0,len(listOfLists[counter])):
            if i not in empt:
                empt.append(listOfLists[counter][i])
            index += 1
    counter += 1
    index = 0
    while index < len(listOfLists[counter]):
        for i in range(0,len(listOfLists[counter])):
            print(listOfLists[counter][i])
            if i not in empt1:
                empt1.append(listOfLists[counter][i])
            index += 1
    print(result, sorted(empt)[-1], sorted(empt1)[-1])
            
            
    