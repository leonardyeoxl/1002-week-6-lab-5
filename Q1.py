''' function takes in var as a input and returns message containing var 
Input:
var (user's name)

Output:
constructed string which includes the user's name
'''
def printHello(var):
    return "Hello "+var+", how are you doing?"  #concats static message with user's name

""" ---start main program--- """
var = raw_input("Please enter your name: ") #user's name input

print printHello(var) #print output of printHello function
""" ---end main program--- """
