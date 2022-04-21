#Domenic Vacanti
#Fundementals 1 DA1

def averageOf(num1, num2, num3):
    return( (num1 + num2 + num3) / 3 )

def averageOfV2(num1, num2, num3):
    sumOfInputs = num1 + num2 + num3
    average = sumOfInputs / 3
    return average

def printMinAndMax(num1, num2, num3):
    minOfInputs = min(num1, num2, num3)
    maxOfInputs = max(num1, num2, num3)
    print((minOfInputs, maxOfInputs))

def returnMinAndMax(num1, num2, num3):
    minOfInputs = min(num1, num2, num3)
    maxOfInputs = max(num1, num2, num3)
    return(minOfInputs, maxOfInputs)

def costOfTrip(distanceInKilometers, speedInKPH, KmPerLiter, gasCostPerLiter):
    timeReq = distanceInKilometers/speedInKPH
    litersNeeded = distanceInKilometers/KmPerLiter
    cost = litersNeeded * gasCostPerLiter
    return (timeReq,cost)

def printTwoTripCosts(distanceInKilometers, veh1Name, veh1SpeedKPH, veh1KmPerLiter,
    veh2Name, veh2SpeedKPH, veh2KmPerLiter, gasCostPerLiter):
    cost = costOfTrip(distanceInKilometers, veh1SpeedKPH, veh1KmPerLiter, gasCostPerLiter)
    print("A trip of " + str(distanceInKilometers) + " kilometers in " + veh1Name + " takes " + str(cost[0]) + " hours and costs $" + str(round(cost[1],2)) + ".")
    cost1 = costOfTrip(distanceInKilometers, veh2SpeedKPH, veh2KmPerLiter, gasCostPerLiter)
    print("A trip of " + str(distanceInKilometers) + " kilometers in " + veh2Name + " takes " + str(cost1[0]) + " hours and costs $" + str(round(cost1[1],2)) + ".")
    return
