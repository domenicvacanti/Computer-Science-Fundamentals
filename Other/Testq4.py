def q3(listOfLists, vLow, vHigh):
    empt = {}
    empt1 = {}
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
                empt[i] = i
            index += 1
    counter += 1
    while index < len(listOfLists[counter]):
        index = 0
        for i in range(0,len(listOfLists[counter])):
            if i not in empt:
                empt1[i] = i  
            index += 1
    print(result, sorted(empt), sorted(empt1))
            
            
    