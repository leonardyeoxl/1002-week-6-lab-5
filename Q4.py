''' 
function to check if the range, 1 being the start and n being the end of range. 
Returns the total number between 1 and n that can be divisble by m

inputs: 
1)n (end of range)
2)m (number to be divided by)

outputs: 
returns the calculated list of numbers between 1 and n that can be divisble by m
'''
def modCount(n, m):
    counter = 0                 #init counter variable
    for x in range(1, n+1):     #loops from a range of 1 to n+1
        if x % m == 0:          #checks if a number can be evenly divided by m
            counter += 1        #if the number can be evenly divided by m, add into the "counter"
    
    return "Result: "+str(counter) #returns a calculated sum of numbers from "counter"

""" ---start main program--- """
print "Please enter 2 numbers:"

var1 = int(raw_input("n: ")) #get the end of range
var2 = int(raw_input("m: ")) #get the number which is used to divide

print modCount(var1, var2) #print the output from modCount function
""" ---end main program--- """