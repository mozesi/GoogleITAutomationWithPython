
# While loop

def aLoopingFunction(numberOfTimesToLoop, initialNumberOfTimes):
    while initialNumberOfTimes < numberOfTimesToLoop :
        print("AM here")
        initialNumberOfTimes += 1
    
num  = input("Enter initial number") 
num2 = input( "Enter  number of times to loop")  

aLoopingFunction(int(num2),int(num)) 