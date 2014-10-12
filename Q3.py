''' 
function to check if inputs are in ordered list

inputs: 
1) int1(1st user's integer input),
2) int2(2nd user's integer input),
3) int3(3rd user's integer input)

outputs: 
returns True if the inputs are in ordered list
returns False if the inputs are not in ordered list
'''
def ordered3(int1, int2, int3):

    if (int1 < int2         #checks if int1 is smaller than int2
    and int2 < int3         #checks if int2 is smaller than int3
    and int3 > int2         #checks if int2 is smaller than int3
    and int3 > int1):       #checks if int1 is smaller than int3
        return True         #returns True if the inputs(int1, int2, int3) are in a order
    else:
        return False        #returns False if the inputs(int1, int2, int3) are not in a order

""" ---start main program--- """
continueVar = "y"
while(continueVar == "y"):
    print "Please enter three numbers:"

    var1 = int(raw_input()) #1st number user input
    var2 = int(raw_input()) #2nd number user input
    var3 = int(raw_input()) #3rd number user input

    if ordered3(var1, var2, var3):
        print "The inputs are ordered" #prints message if ordered3 returns True
    else:
        print "The inputs are unordered" #prints message if ordered3 returns False
    
    continueVar = raw_input("Continue?(y/n): ") #prompts user whether to continue or not
""" ---end main program--- """
