#Domenic Vacanti, Homework 1
#CS:1210

import math
def tripCostInfo(distanceKM, vehSpeedMPS, vehKPL, gasCostPerLiter, hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay):
    hoursTaken = ((((distanceKM*1000)/vehSpeedMPS)/60)/60)
    daysNeededDriving = hoursTaken/8
    hotelsNeeded = (hoursTaken/8)-1
    daysNeededCeil = math.ceil(hotelsNeeded)
    bAndDCost = (daysNeededCeil)*(breakfastCostPerDay+dinnerCostPerDay)
    lastDayHours = (daysNeededDriving - daysNeededCeil)*8
    lunchesNeeded = daysNeededCeil
    if lastDayHours > 4:
        lunchesNeeded = lunchesNeeded + 1
    else:
        lunchesNeeded = lunchesNeeded
    lunchesCost = lunchesNeeded * lunchCostPerDay
    hotelCost = daysNeededCeil * hotelCostPerNight
    gasCost = (distanceKM/vehKPL)*gasCostPerLiter
    totalPrice = (bAndDCost + lunchesCost + hotelCost + gasCost)
    return (totalPrice, gasCost, daysNeededCeil, lunchesNeeded, (bAndDCost + lunchesCost))
    
def bestVehicleForTrip(distanceM, veh1Name, veh1SpeedMPH, veh1MPG, veh2Name, veh2SpeedMPH, veh2MPG, gasCostPerGallon, hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay):
    veh1Info = tripCostInfo((distanceM*1.609344),(veh1SpeedMPH*0.44704),(veh1MPG*0.425144),(gasCostPerGallon/3.785411784), hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay)
    veh2Info = tripCostInfo((distanceM*1.609344),(veh2SpeedMPH*0.44704),(veh2MPG*0.425144),(gasCostPerGallon/3.785411784), hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay)
    print("{:.1f} miles in vehicle '{}' will cost ${:.2f}, including: ${:.2f} for {} hotel nights, ${:.2f} for gas, and ${:.2f} for food (including {} lunch(es))".format(distanceM, veh1Name, veh1Info[0], (hotelCostPerNight*veh1Info[2]), veh1Info[2], veh1Info[1], veh1Info[4], veh1Info[3]))
    print("{:.1f} miles in vehicle '{}' will cost ${:.2f}, including: ${:.2f} for {} hotel nights, ${:.2f} for gas, and ${:.2f} for food (including {} lunch(es))".format(distanceM, veh2Name, veh2Info[0], (hotelCostPerNight*veh2Info[2]), veh2Info[2], veh2Info[1], veh2Info[4], veh2Info[3]))
    if veh1Info[0] < veh2Info[0]:
        print("To save money, use '{}'".format(veh1Name))
    else:
        print("To save money, use '{}'".format(veh2Name))
    
def Q1():
    test1 = tripCostInfo(1500,10,500,2,5,1.0,2,3)
    print(test1)
    test2 = tripCostInfo(1000,10,500,2,5,1.0,2,3)
    print(test2)
    test3 = tripCostInfo(2000,10,500,2,5,1.0,2,3)
    print(test3)
    test4 = tripCostInfo(1500,10,500,2,5,4.0,2,3)
    print(test4)
    test5 = tripCostInfo(1500,10,50,2,5,1.0,2,3)
    print(test5)

def Q2():
    test1 = bestVehicleForTrip(1000.0, "Camero", 100.0, 1.0, "Honda", 27.0, 100.0, 2.10, 6.50, 11.0, 23.0, 55.0)
    test2 = bestVehicleForTrip(1500.0, "Bugatti", 100.0, 1.0, "Vespa", 27.0, 100.0, 2.10, 6.50, 11.0, 23.0, 55.0)
    test3 = bestVehicleForTrip(1000.0, "Bugatti", 100.0, 1.0, "Vespa", 27.0, 100.0, 7.40, 6.50, 11.0, 23.0, 55.0)
    test4 = bestVehicleForTrip(1000.0, "Bugatti", 50.0, 1.0, "Vespa", 27.0, 100.0, 2.10, 6.50, 11.0, 23.0, 55.0)
    test5 = bestVehicleForTrip(1000.0, "Bugatti", 1.0, 1.0, "Vespa", 27.0, 100.0, 2.10, 6.50, 11.0, 23.0, 55.0)