# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:30:23 2020

@author: james
"""

def numberInput():
    while True:
        try:
            number = int(input("Input the number you would like to know the prime factors of: "))
        except ValueError:
            print("That is an invalid input.")
            continue
        else:
            break
        
    return number

def factorFinder(number):
    factors = []
    
    for factor in range(2,int(number**0.5)+1):
        if number%factor == 0:
            factors.append([factor,int(number/factor)])
    
    return factors

def primeFactorFinder(number):
    primeFactors = []
    
    factors = factorFinder(number)
    
    toPrime = factors[0]
    toPrimeAltered = []
    
    primed = False
    
    while not primed:
        for num in toPrime:
            factorsOfNum = factorFinder(num)
            if len(factorsOfNum) == 0:
                primeFactors.append(num)
            else:
                toPrimeAltered.append(factorsOfNum[0][0])
                toPrimeAltered.append(factorsOfNum[0][1])
        toPrime = toPrimeAltered
        toPrimeAltered = []
        
        if len(toPrime) == 0:
            primed = True
    
    return primeFactors

def printPrimeFactors(number,factorsToPrint):
    print("The prime factors of",number,"are:")
    printing = str(factorsToPrint[0])
    for i in range(1,len(factorsToPrint)):
        printing += " x "+str(factorsToPrint[i])
    print(printing)

def runProgram():
    toFind = 0
    
    while toFind < 2:
        toFind = numberInput()
        if toFind < 2:
            print("That is an invalid input.")
    
    if len(factorFinder(toFind)) == 0:
        print("This is a prime number already")
    else:
        primeFactors = primeFactorFinder(toFind)
        printPrimeFactors(toFind,primeFactors)

again = 'y'

while again == 'y':
    runProgram()
    again = input("Do you want to find the prime factors of another number? (y/n)")

