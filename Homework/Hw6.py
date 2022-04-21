import random
class Box:
    def __init__(self, centerX=0.0, centerY=0.0, centerZ=0.0, width=1.0, height=1.0, depth=1.0):
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.width = width
        self.height = height
        self.depth = depth
    
    def setCenter(self,x,y,z):
        self.centerX = x
        self.centerY = y
        self.centerZ = z
    
    def setWidth(self,width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height
    
    def setDepth(self, depth):
        self.depth = depth
    
    def volume(self):
        v = (self.width)*(self.height)*(self.depth)
        return v
    
    def surfaceArea(self):
        sA = (2*(self.width)*(self.height))+(2*(self.width)*(self.depth))+(2*(self.depth)*(self.height))
        return sA
    
    def overlaps(self, otherBox):
        wDif = abs(self.centerX - otherBox.centerX)
        hDif = abs(self.centerY - otherBox.centerY)
        dDif = abs(self.centerZ - otherBox.centerZ)
        if wDif <= abs(((self.width)/2) + ((otherBox.width)/2)):
            if hDif <= abs(((self.height)/2) + ((otherBox.height)/2)):
                if dDif <= abs(((self.depth)/2) + ((otherBox.depth)/2)):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def isInside(self, otherBox):
        wDif = abs(self.centerX - otherBox.centerX)
        hDif = abs(self.centerY - otherBox.centerY)
        dDif = abs(self.centerZ - otherBox.centerZ)
        print((1/2)*(otherBox.width)), wDif + (1/2*(self.width))
        if ((1/2)*(otherBox.width)) > wDif + (1/2*(self.width)):
            if ((1/2)*(otherBox.height)) > hDif + (1/2*(self.height)):
                if ((1/2)*(otherBox.depth)) > dDif + (1/2*(self.depth)):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __repr__(self):
        return "< {}-by-{}-by-{} 3D box with center at ({}, {}, {}) >".format(round(self.width),round(self.height),round(self.depth),self.centerX,self.centerY,self.centerZ)

class NimGame:
    
    def __init__(self, listOfBalls):
        self.list1 = listOfBalls
        print("Nim game initialized with {} heaps.".format(len(self.list1)))
    
    def __repr__(self):
        result = "Nim game with {} heap(s)\n".format(len(self.list1))
        for i in range(len(self.list1)):
            result = result + "    Heap {}: {} balls\n".format(i, self.list1[i])
        return result
    
    def remove(self,ball,heap):
        if heap > len(self.list1)-1:
            return "Try a heap that we have here in front of us! :)"
        if ball > self.list1[heap]:
            return "Cannot take {} balls from heap {}".format(ball, heap)
        self.list1[heap] = self.list1[heap] - ball
        print("You took {} balls from heap {}.".format(ball,heap))
        if sum(self.list1) == 0:
            return "Game over! You win!"
        heap = random.randint(0,len(self.list1)-1)
        while self.list1[heap] == 0:
            heap = random.randint(0,len(self.list1)-1)
        ball = random.randint(0,self.list1[heap])
        self.list1[heap] = self.list1[heap] - ball
        print("Computer took {} balls from heap {}".format(ball,heap))
        if sum(self.list1) == 0:
            return "Game Over! Computer Wins!"

class Animal ():
    
    numAnimals = 0

    def __init__ (self, name = 'NoName', numLegs = 0):
        self.name = name
        self.numLegs = numLegs
        Animal.numAnimals = Animal.numAnimals + 1
        self.id = Animal.numAnimals

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("...")

    def __repr__(self):
        return ('<{} the animal. ID:{}>'.format(self.name, self.id))

class Cat(Animal):
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ('<{} the {} cat. ID: {}>'.format(self.name, self.color, self.id))

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching ...")

    def __repr__(self):
        return '<{} the dog. ID:{}>'.format(self.name, self.id)

class Snake(Animal):
    
    def __init__(self, name = 'Slither', stripes = False):
        Animal.__init__(self, name, 0)
    
    def speak(self):
        print("ssssssss")
    
    def stripes(self):
        if self.stripes == True:
            return "{} has stripes.",format(self.name)
        else:
            return "{} does not have stripes.".format(self.name)
    
    def __repr__(self):
        return "< {} the snake. ID:{} >".format(self.name,self.id)

        
def testAnimal():
    c1 = Cat("Milo")
    c2 = Cat(furColor = "black")
    d1 = Dog()
    d2 = Dog()
    s1 = Snake()
    for animal in [c1, c2, d1, d2, s1]:
        print(animal)
        animal.speak()
    d1.fetch()
    print(c2.getFurColor())
    print(s1.stripes())