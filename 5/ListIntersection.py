# This assignment 5.1 from the Foothill College java class. The java code
# is under JavaStuff/FoothillCollege/ProblenmSet5

from random import randint
#randint(2,9) inclusive

# these are the two sample lists from the assignment
numList1 =  [1, 4, 8, 9, 11, 15, 17, 28, 41, 59,59]
numList2 =   [4, 7, 11, 17, 19, 20, 23, 28, 37, 59, 59]
numList3 = []

# This is generating two lists with random numbers. Its replacing the
# elements in the lists above. Commenting these out will use the lists above
for i in range (0, len(numList1)):
    numList1[i] = randint(1, 20)
for i in range(0, len(numList2)):
    numList2[i] = randint(1,20)
print("###############################################################")
#To iterate over a sequence means to visit each element of the sequence,
# and do some operation for each element. In Python, we say that a value
# is an iterable when your program can iterate over it. In short,
# an iterable is a value that represents a sequence of one more values. 
#######################################################################
def remove_duplicates(numList):     
    anotherList = []
    aSet = set()
    for number in numList: # lists as an iterable, different kind of for loop
        # If element num is not been encountered yet,
        # ... add it to both the list and set.
        if number not in aSet:
            anotherList.append(number) #anotherList is a list
            aSet.add(number)      #aSet is a set, in java I converted them back and forth
    return anotherList

for i in range (0, len(numList1)):
    for j in range (0, len(numList2)):
        if (numList1[i] == numList2[j]):
            numList3.append(numList1[i])
print("List1: ",numList1)
print("List2: ",numList2)
print("Intersection List3 before removing duplicates: " + str(numList3))

numList3 = remove_duplicates(numList3)

print("Intersection List3 after removing duplicates: " + str(numList3))
