import unittest
import os
#**************************************************************************************
#for i in range(4,0,-1):
#    print str(i) + " bottles of beer on the wall, " + str(i -1) + " Bottles of beer"
i = 0
while i < 7:
    #print("heloo")
    print (str(i) + " bottles of beer on the wall, " + str(i - 1) + " bottles of beer")
    i = i + 1  
#while i < 4:
    print ("Hello")
#    i = i + 1
#**************************************************************************************
# import OS module
# Get the list of files and directories

path = ("//home/esickert")
print("Prints contents of " +  path);
print(path);
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)
