'''
Q5, printAsterisks function
function prints a line of n asterisks

input:
n (number of times to be repeated)

output:
line of n asterisks
'''
def printAsterisks(n):
    limit = 20                  #init limit as 20
    if(n > limit):              #check if n ("number of times to be executed" input) is more than the limit
        for x in range(limit):  
            print "*",          #prints the output in a line
        print "\n"              #next line
    else:                       #if n is less than the limit
        for x in range(n):
            print "*",          #prints the output in a line
        print "\n"              #next line

''' 
Q5a 
function that prints a line of n character

input:
n (number of times to be repeated)
char (the character)

output:
line of n character
'''
def printsLinesOfChar(n, char):
    for x in range(n):          #loops from a range of n
            print char,         #prints the characters in a line
    print "\n"                  #next line

''' 
Q5c 
function that prints multiple lines of n characters from a given string

input:
n (number of times to be repeated)
string (string)
'''
def printsLinesOfCharFromString(string, n):
    listVar = list(string)          #breaks down the string into characters and save into a list array
    for y in range(len(listVar)):   #loops from the length of the list array
        for x in range(n):          #loops n ("number of times to be executed" input) of times
            print listVar[y],       #prints the indexed character in a line.
        print "\n"                  #next line


""" ---start main program--- """
print "1. print asterisks\n2. print lines of character only\n3. print lines of characters from a string "
choiceVar = int(raw_input("Enter your option: "))

if(choiceVar == 1):
    varInt = int(raw_input("n: "))  #get "number of times to be executed" input
    printAsterisks(varInt) #Q5
elif(choiceVar == 2):
    varInt = int(raw_input("n: ")) #get "number of times to be executed" input
    varChar = raw_input("char: ") #get the character input
    printsLinesOfChar(varInt, varChar) #Q5b
else:
    varInt = int(raw_input("n: ")) #get "number of times to be executed" input
    varString = raw_input("String: ") #get "string" input
    printsLinesOfCharFromString(varString, varInt) #Q5c
""" ---end main program--- """