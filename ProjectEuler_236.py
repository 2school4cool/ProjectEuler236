# Project Euler 236
# By Nick Molinari
# July 2019

import math
from fractions import Fraction

# Gather problem input
n = int(input())
listOfA = [int(x) for x in input().split()]
listofB = [int(x) for x in input().split()]
totalA = sum(listOfA) 
totalB = sum(listofB) 

# Find minimum amount of a given a certain amount of b
def findMinimumA (b) :
    totalFractionB = Fraction(b, totalB)
    return math.ceil(totalFractionB * totalA)

# Calculate M for two given total amounts of product
def calculateM (a, b) :
    totalFractionA = Fraction(j,totalA)
    totalFractionB = Fraction(b, totalB)
    return Fraction(totalFractionA, totalFractionB)

currentM = -1
# Iterate through all possible totals in B shipment
for i in range(1, totalB) :
    # Iterate through all possible totals in A shipment
    for j in range(findMinimumA(i), totalA) :
        # Determine resulting M from given iteration
        m = calculateM (j, i)
        # Only consider M values greater than 1 as given by problem statement
        if m > Fraction(1) :
            runningTotals = []
            # Iterate through each shipment totalling every combination of whole 
            # numbers which fit into the shipment and obey the M value
            # relationship we are currently testing.
            # If one permutation of totals is equal to the total numbers for
            # the entire shipment then we have found a valid M value.
            for k in range(n) :
                # Set previous totals to totals from last loop
                previousRunningTotals = runningTotals
                runningTotals = []
                # Number of spoiledA * "factor" = Number of spoiledB
                factor = Fraction(1, listOfA[k]) * m * listofB[k]
                # All possible whole number options which fit into the shipment
                possibleMultiples = min(math.floor(listOfA[k] / factor.denominator), math.floor(listofB[k] / factor.numerator))
                # Iterate through all possible combinations of spoiled A and 
                # spoiled B that could fit as a whole number into this shipment
                # while maintaining the spoiledA * factor = spoiledB relationship
                for l in range(1, possibleMultiples+1) :
                    spoiledA = factor.denominator * l
                    spoiledB = factor.numerator * l
                    if k == 0:
                        runningTotals.append([spoiledA, spoiledB])
                    else: 
                        # Add possible spoiled values to all the 
                        # potential running totals of spoiled products
                        for option in previousRunningTotals :
                            runningTotals.append([option[0] + spoiledA, option[1] + spoiledB])
                # If no options were found for this shipment then our M is disqualified
                if runningTotals == [] :
                    break;
            if k == n-1 and runningTotals != []:
                # Check if the actual total is one of the possible running totals
                if [j,i] in runningTotals:
                    if currentM == -1:
                        currentM = m
                    elif currentM != m:
                        print(m)
                        
print(currentM)
