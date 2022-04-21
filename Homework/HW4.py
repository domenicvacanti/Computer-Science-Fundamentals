def analyzeTexts(fileName, minWordLengthToConsider = 1):
    myFile = open(fileName, encoding = "utf-8")
    spamCounter = 0
    hamCounter = 0
    hamDict = {}
    spamDict = {}
    index = 1
    messageCounter = 0
    totalHamWords = 0
    totalSpamWords = 0
    for line in myFile:
        messageCounter += 1
        splitLine = line.split()
        if splitLine[0] == "ham":
            index = 1
            hamCounter += 1
            while index < len(splitLine):
                if ((splitLine[index].strip(".?!-+*@;#&")).lower() in hamDict) and ((splitLine[index].strip(".?!-+*@;#&")).lower() != ""):
                    hamDict[(splitLine[index].strip(".?!-+*@;#&")).lower()] +=1 
                    totalHamWords += 1
                elif ((splitLine[index].strip(".?!-+*@;#&")).lower() not in hamDict) and ((splitLine[index].strip(".?!-+*@;#&")).lower() != ""):
                    hamDict[(splitLine[index].strip(".?!-+*@;#&")).lower()] = 1
                    totalHamWords += 1
                index += 1
        elif splitLine[0] == "spam":
            index = 1
            spamCounter += 1
            while index < len(splitLine):
                if ((splitLine[index].strip(".?!-+*@;#&")).lower() in spamDict) and ((splitLine[index].strip(".?!-+*@;#&")).lower() !=""):
                    spamDict[(splitLine[index].strip(".?!-+*@;#&")).lower()] +=1
                    totalSpamWords += 1
                elif ((splitLine[index].strip(".?!-+*@;#&")).lower() not in spamDict) and ((splitLine[index].strip(".?!-+*@;#&")).lower() !=""):
                    spamDict[(splitLine[index].strip(".?!-+*@;#&")).lower()] = 1
                    totalSpamWords += 1
                index += 1
    sortedHamDict = sorted(hamDict.items(),key=lambda x: x[1], reverse = True)
    sortedSpamDict = sorted(spamDict.items(),key=lambda x: x[1], reverse = True)
    print("There are {} messages, {} ham and {} spam.".format(messageCounter,hamCounter,spamCounter))
    print("Ham messages consist of {} words, with {} unique words.".format(totalHamWords, len(hamDict)))
    print("  Ham messages have an average of {} words per message.".format(round((totalHamWords/hamCounter),2)))
    print("Spam messages consist of {} words, with {} unique words.".format(totalSpamWords, len(spamDict)))
    print("  Spam messages have an average of {} words per message.".format(round((totalSpamWords/spamCounter),2)))
    i = 0
    t = 0
    place = 1
    print("~~~~~Ham: 10 most frequent words bigger than minimum length~~~~~")
    while i < 10:
        if len(sortedHamDict[i+t][0]) >= minWordLengthToConsider:
            print("{}.) Word: {}, shows up {} times with {}% frequency.".format(place, sortedHamDict[i+t][0], sortedHamDict[i+t][1], round((sortedHamDict[i+t][1]/totalHamWords)*100,2)))
            i += 1
            place += 1
        else:
            t += 1
    print("~~~~~Spam: 10 most frequent words bigger than minimum length~~~~~")
    i = 0
    t = 0
    place = 1
    while i < 10:
        if len(sortedSpamDict[i+t][0]) >= minWordLengthToConsider:
            print("{}.) Word: {}, shows up {} times with {}% frequency.".format(place, sortedSpamDict[i+t][0], sortedSpamDict[i+t][1], round((sortedSpamDict[i+t][1]/totalSpamWords)*100,2)))
            i += 1
            place += 1
        else:
            t += 1