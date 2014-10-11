''' function to check if inputs are zero
inputs: 
1) int1(1st user integer input), 
2) int2(2nd user integer input), 
3) int3(3rd user integer input)

outputs: 
returns True if all inputs are zero
returns False if none of the inputs are zero'''
def zeroCheck(int1, int2, int3):
    if (int1 == 0              #checks if int1 is 0 
    or int2 == 0               #checks if int2 is 0
    or int3 == 0):             #checks if int3 is 0
        return True            #returns True if int1, int2 and int3 have zeros
    else:                      #if int1, int2 and int3 do not have zeros
        return False           #returns False if int1, int2 and int3 do not have zeros

""" ---start main program--- """
print "Please enter three numbers:"

var1 = int(raw_input()) #1st user input
var2 = int(raw_input()) #2nd user input
var3 = int(raw_input()) #3rd user input

if zeroCheck(var1, var2, var3):
    print "there was a zero in the entered numbers" #prints message if zeroCheck returns True
else:
    print "there were NO zeros in the entered numbers" #prints message if zeroCheck returns False
""" ---end main program--- """