def reverseGraph(g):
    newG = {}
    keyList = list(g.keys())
    valList = list(g.values())
    c = 0
    for L in valList:
        if L == []:
            L
        else:
            for i in range(0,len(L)):
                newG[L[i]] = keyList[c]
        c += 1
    return newG