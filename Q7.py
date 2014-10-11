""" iterative structure for sumOfRange function that 
takes three integers and returns the sum of all integers 
between the first and the second argument 
with an increment of the third argument
Input:
1) int1 (first variable)
2) int2 (second variable)
3) int3 (incremental variable)

Output:
returns a calculated sum of all integers 
between the first and the second argument 
with an increment of the third argument
"""
def sumOfRange(int1, int2, int3):

    firstVar = 0+int1                       #init firstVar
    thirdVar = 1+int3                       #init thirdVar
    secondVar = int2+1                      #init secondVar

    counter = firstVar                      #init counter as firstVar
    counter2 = 0                            #init counter2 as 0

    for x in range(firstVar, secondVar):    #loops in a range from firstVar to secondVar
        if(counter < secondVar):            #checks if counter is less than secondVar
            counter2 = counter2 + counter   #calculates counter2 by adding counter2 and counter
            counter = counter + int3        #calculates counter by adding counter and int3

    return counter2                         #returns the calculated value of counter2

""" recursion for sumOfRange function that 
takes three integers and returns the sum of all integers 
between the first and the second argument 
with an increment of the third argument

Input:
1) int1 (first variable)
2) int2 (second variable)
3) int3 (incremental variable)

Output:
returns a calculated sum of all integers 
between the first and the second argument 
with an increment of the third argument
"""
def sumOfRangeRecursion(int1, int2, int3):
    if(int2 < int1):                                            #checks if int2 is less than int1
        return int1                                             #returns int1 as the base case
    elif(int1+int3 <= int2):                                    #checks if int2 is more than or equal to the calculated value of int1 and int3
        int1 += sumOfRangeRecursion(int1+int3, int2, int3)      #increments int1, while the function "sumOfRangeRecursion" is executed again. each time "sumOfRangeRecursion" is executed, int1 is incremented by int3

    return int1                                                 #returns the calculated value of int1


""" ---start main program--- """
print "1. sumOfRange iterative structure\n2. sumOfRange recursion"

choiceVar = int(raw_input("Choose: "))

var1 = int(raw_input("First variable: "))
var2 = int(raw_input("Second variable: "))
var3 = int(raw_input("Incremental variable: "))

if(choiceVar == "1"):
    print "The sum of range through iteractive structure is "+str(sumOfRange(var1, var2, var3)) #prints output from sumOfRange function
else:
    print "The sum of range through recursion is "+str(sumOfRangeRecursion(var1, var2, var3)) #prints output from sumOfrangeRecursion function
""" ---end main program--- """