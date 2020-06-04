# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:30:23 2020

@author: james
"""

def numberInput():
    '''
    number input subroutine
    '''
    while True:#continues looping until the input is of the integer type
        try:
            number = int(input("Input the number you would like to know the prime factors of: "))#requests input
        except ValueError:#checks to see for ValueError
            print("That is an invalid input.")#If it sees one prints error message
            continue#loop continues
        else:#if no error message
            break#loop ended as there is a valid input
        
    return number#returns the valid input

def factorFinder(number):
    '''
    subroutine to find the factors of a given number
    '''
    factors = []#empty factors list
    
    for factor in range(2, int(number**0.5)+1):#loops through prospective factors from 2 to the sqrt of the number as this is the max factor
        if number%factor == 0:#checks to see if its a factor
            factors.append([factor, int(number/factor)])#if it is a factor the pair is appended to the factors list
    
    return factors#returns the list of factor pairs

def primeFactorFinder(number):
    '''
    the prime factor calculator routine (the main function of the program)
    '''
    primeFactors = []#an empty list for the results we require
    
    factors = factorFinder(number)#finds the factors of the requested number
    
    toPrime = factors[0]#picks the first pair
    toPrimeAltered = []#an empty list for functionality
    
    primed = False#variable to see whether the function has been complete
    
    while not primed:#while it hasnt completed
        for num in toPrime:#loops through non-prime factors
            factorsOfNum = factorFinder(num)#finds the factors of these factors
            if len(factorsOfNum) == 0:#if the length of factors is 0 then the factor is a prime number
                primeFactors.append(num)#as it is prime it is added to the results list
            else:
                toPrimeAltered.append(factorsOfNum[0][0])#if not then the first pair of factors now becomes the pair that need to be reduced to prime number
                toPrimeAltered.append(factorsOfNum[0][1])#the compatriate factor
        toPrime = toPrimeAltered#the required priming factors is re-established
        toPrimeAltered = []#the to alter factors is emptied for the next iteration
        
        if len(toPrime) == 0:#if the action is completed then there is no more factors that require priming
            primed = True#the process is complete
    
    return primeFactors#once the process is completed the results are returned

def printPrimeFactors(number, factorsToPrint):
    '''
    a printing process for the prime factors
    '''
    print("The prime factors of", number, "are:")#formal printing
    #Next three lines produce the printing of prime factors
    printing = str(factorsToPrint[0])
    for i in range(1, len(factorsToPrint)):
        printing += " x "+str(factorsToPrint[i])
    print(printing)#the prime factors are printed

def runProgram():
    '''
    routine for running the whole program
    '''
    toFind = 0#intialise variable
    
    while toFind < 2:#until a suitable value is inputted
        toFind = numberInput()#request an input
        if toFind < 2:#if the value is invalid
            print("That is an invalid input, you need a number greater than 1.")#print error message
    
    if len(factorFinder(toFind)) == 0:#if the number inputted is a prime has no pairs
        print("This is a prime number already")#printing message
    else:
        primeFactors = primeFactorFinder(toFind)#run the routine to determine the prime factors
        printPrimeFactors(toFind, primeFactors)#run routine for printing the prime factors

again = 'y'#so that the program runs at least once

while again == 'y':#while they want the prime factors for more numbers
    runProgram()#run the program that requests input and provides solution
    again = input("Do you want to find the prime factors of another number? (y/n)")#checks to see if user wants to check any more numbers
    