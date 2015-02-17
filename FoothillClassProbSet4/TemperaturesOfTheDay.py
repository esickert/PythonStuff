# This is assignment 4 from the java class at Foothill College. The
# java program is under /FoothillCollege/ProblemSet4

import time;   # this allows me to use the time module

temperature = []
days = 5

def getInput(myList):
    for i in range(0,days):
        x = input("Please enter a temperature for day " + str(i+1) + " : ")
        y = float(x) #input and raw_input inport characters from the keyboard as
        myList.append(y) # strings. Those characters need to be converted to use!!!!!
        print(myList);
    return(myList) 

def getSum(myList):
    add = 0;
    for i in range(0,days):
        add = myList[i] + add;
    print("Their sum is ", add)
    return(add);

def getAverage(theSum):
    average = theSum / days;
    print("Their average is ", average);
    return(average);

def getHottestDays(myList, average):
    count = 0;
    for i in range(0,days):
        if myList[i] > average:
            count = count + 1;
    print("There were ", count," days hotter than ", average);

temperature = getInput(temperature);
print("The list is : ",temperature);
print("Thank you...please wait!");
time.sleep(5);                   # pauses the application for 5 seconds 
average = (getAverage(getSum(temperature)));
getHottestDays(temperature,average);

#temps.remove(2)             #this removes elements in list!!!!!!!!!!!!!

