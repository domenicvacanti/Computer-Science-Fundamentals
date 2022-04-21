#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:09:45 2020

@author: domenicvacanti
"""

import pylab
import math

def tryOutPyLab(name = "No Name", numberOfPlots = 10):
    pylab.title(name + "'s Graph")
    x = 0
    while x < 2:
        oC = 0
        numC = 0
        nimA = (numberOfPlots/(numberOfPlots+(numberOfPlots/2)))
        while oC < numberOfPlots:
            i = 0
            xList = []
            yList = []
            if x == 1:
                numC = numC - nimA
            else:
                numC = numC + nimA
            while i < 20:
                yList.append(i)
                xList.append((numC * math.sqrt(i)))
                i += 1
            pylab.plot(xList,yList,linestyle = "-")
            oC += 1
        x += 1
    pylab.savefig("upsideDownRainbow")
    pylab.show()
        
        