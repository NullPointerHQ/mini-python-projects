#Objective: This program will determine if a number is Prime or not

#We can test if the number 'n' is prime by:
#Checking if n is 2 or less | Check if n is divisible by 2 | Check if n is divisible from 3 up to sqrt(n)

#Checks if the number provided is 2 or less
import math#For Square Root Function
def is_two_or_less(number):
    #print("Received")
    if(number <= 2):#The number is 2 or less
        #print("Returning as TRUE")
        return True
    else:
        #print("Returning as FALSE")
        return False

def is_even (number):
    #Checks if the number given can easily be split by two
    if (number % 2 == 0):
        return True
    else:
        return False

def divisible (number):
    for i in range( 3 , int(( math.sqrt(n) + 1 ))):
        if (is_even(i) == False and n % i == 0):
            return True#Number is divisible by another number
    return False#Number is not divisible by another number



#################################################################
######################    MAIN FUNCTION    ######################
#################################################################

choice = "Y"

while choice == "Y" or choice == "y":
    
    n = int(input("Enter a whole number: ")) #Number being checked
    
    #Checks if n is two or less
    if (is_two_or_less(n) == False and is_even(n) == False and divisible(n) == False):
        print(n, "is Prime!")

    else:
        print(n ,"is not Prime!")
        
    choice = input("Continue? (Y/N): ")


