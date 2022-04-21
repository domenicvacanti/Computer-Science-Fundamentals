import tkinter as tk
import random

attemptCount = 0
totAttempt = 0
solvedCount = 0
avgGuess = 0
addList = []
minList = []
multiList = []
divList = []
ans = False


def beginGame():
    beginButton["state"] = tk.DISABLED
    correctButton["state"] = tk.NORMAL
    newButton["state"] = tk.NORMAL
    newProblem()
    

def newProblem():
    global attemptCount
    global totAttempt
    correctButton["state"] = tk.NORMAL
    attemptCount = 0
    entryWindow["state"] = tk.NORMAL
    entryWindow.delete(0,'end')
    progLabel["text"] = "Input Possible Solution"
    checkLabel["text"] = "Input Possible Solution"
    if v.get() == 0:
        randomProb = random.randint(1,4)
        if randomProb == 1:
            addQ()
        elif randomProb == 2:
            minQ()
        elif randomProb == 3:
            multiQ()
        elif randomProb == 4:
            divQ()
    elif v.get() == 1:
        addQ()
    elif v.get() == 2:
        minQ()
    elif v.get() == 3:
        multiQ()
    elif v.get() == 4:
        divQ()

def checkAns():
    global ans
    global solvedCount
    global attemptCount
    global totAttempt
    if ans == var.get():
        entryWindow["state"] = tk.DISABLED
        correctButton["state"] = tk.DISABLED
        solvedCount += 1
        attemptCount += 1
        totAttempt += 1
        checkLabel["text"] = "Correct"
        if progLabel["text"] == "Input Possible Solution" or progLabel["text"] == "Correct on First Attempt, Nice!":
            progLabel["text"] = "Correct on First Attempt, Nice!"
        else:
            progLabel["text"] = "{} Attempt(s) on Current Question".format(attemptCount)
    else:
        entryWindow.delete(0,'end')
        attemptCount += 1
        totAttempt +=1
        checkLabel["text"] = "Incorrect, Try Again"
        progLabel["text"] = "{} Attempt(s) on Current Question".format(attemptCount)

def quitGame():
    global solvedCount
    global totAttempt
    global avgGuess
    global addList
    global minList
    global multiList
    global divList    
    totalProblemCount = len(addList) + len(minList) + len(multiList) + len(divList)
    problemLabel["text"] = "Thanks For Playing! Closing Program."
    if totalProblemCount == 0:
        print("No Problems Attempted")
        window.quit()
    else:
        avgGuess = totAttempt/totalProblemCount
        print("Attempted: {}\nSolved: {}\nAverage Attempts: {}".format(totalProblemCount,solvedCount, avgGuess))
        window.quit()

def addQ():
    global addList
    global ans
    haveNums = False
    while haveNums == False:
        n1 = random.randint(0,1000)
        n2 = random.randint(0,1000)
        if [n1,n2] not in addList:
            haveNums = True
    problemLabel["text"] = str(n1) + " + " + str(n2) + " ="
    addList.append([n1,n2])
    ans = n1 + n2

def minQ():
    global minList
    global ans   
    haveNums = False
    while haveNums == False:
        n1 = random.randint(0,1000)
        n2 = random.randint(0,1000)
        if [n1,n2] not in minList and n1 - n2 > 0:
            haveNums = True
    problemLabel["text"] = str(n1) + " - " + str(n2) + " ="
    minList.append([n1,n2])
    ans = n1 - n2

def multiQ():
    global multiList
    global ans   
    haveNums = False
    while haveNums == False:
        n1 = random.randint(0,100)
        n2 = random.randint(0,100)
        if [n1,n2] not in multiList:
            haveNums = True
    problemLabel["text"] = str(n1) + " * " + str(n2) + " ="
    multiList.append([n1,n2])
    ans = n1 * n2

def divQ():
    global divList
    global ans   
    haveNums = False
    while haveNums == False:
        n1 = random.randint(1,1000)
        n2 = random.randint(1,1000)
        num1 = n1/n2
        if num1 == int(num1):
            if [n1,n2] not in divList:
                haveNums = True
    problemLabel["text"] = str(n1) + " / " + str(n2) + " ="
    divList.append([n1,n2])
    ans = n1/n2

window = tk.Tk()
v = tk.IntVar()
var = tk.IntVar()
window.title("Simple Math Game")
beginButton = tk.Button(text="Start Game",command=beginGame,state=tk.NORMAL)
beginButton.pack(side=tk.TOP)
problemLabel = tk.Label(text = "Press Start Game to Begin!")
problemLabel.pack(side = tk.TOP)
frame1 = tk.Frame(master=window)
frame1.pack()
label1 = tk.Label(master = frame1, text="Answer:")
label1.pack(side=tk.LEFT)
entryWindow = tk.Entry(master=frame1,textvariable=var,state=tk.NORMAL)
entryWindow.pack(side = tk.LEFT)
checkLabel = tk.Label(text = "Input Possible Solution")
checkLabel.pack(side = tk.TOP)
correctButton = tk.Button(text = "Check Answer",command=checkAns,state=tk.DISABLED)
correctButton.pack(side = tk.TOP)
progLabel = tk.Label(text = "Input Possible Solution")
progLabel.pack(side = tk.TOP)
newButton = tk.Button(text = "New Problem",command=newProblem,state=tk.DISABLED)
newButton.pack(side = tk.TOP)
anyButton = tk.Radiobutton(text = "Any", variable = v, value = 0)
anyButton.pack(side = tk.LEFT)
addButton = tk.Radiobutton(text = "+", variable = v, value = 1)
addButton.pack(side = tk.LEFT)
minButton = tk.Radiobutton(text = "-", variable = v, value = 2)
minButton.pack(side = tk.LEFT)
multButton = tk.Radiobutton(text = "*", variable = v, value = 3)
multButton.pack(side = tk.LEFT)
divButton = tk.Radiobutton(text = "/", variable = v, value = 4)
divButton.pack(side = tk.LEFT)
quitButton = tk.Button(text = "Quit Game",command=quitGame)
quitButton.pack(side = tk.TOP)
entryWindow.delete(0,'end')
window.mainloop()