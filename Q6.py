''' function to return the number of times "y" is being entered
Output:
returns the number of times "y" that is being entered '''
def getContinue():

    varInput = "y"                                                  #init varInput variable
    counter = 0                                                     #init counter variable

    while(varInput == "y"):                                         #loops as long as y is being entered
        varInput = raw_input("Do you want to continue(y/n): ")      #prompts user whether to continue or not

        varInput = varInput.lower()                                 #converts varInput into lower case

        if(varInput == "y"):                                        #check if varInput is "y"
            counter += 1                                            #counter increments by 1

    return "number of times you choose to continue: "+str(counter)  #returns the calculated value of varInput

""" ---start main program--- """
print getContinue()                                                 #prints the output from the function getContinue()
""" ---end main program--- """