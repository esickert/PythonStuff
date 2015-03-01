from random import randint
#randint(2,9) #Inclusive

numList1 =  [1, 4, 8, 9, 11, 15, 17, 28, 41, 59,59]
numList2 =   [4, 7, 11, 17, 19, 20, 23, 28, 37, 59, 59]
numList3 = []

for i in range (0, len(numList1)):
    numList1[i] = randint(1, 20)

for i in range(0, len(numList2)):
    numList2[i] = randint(1,20)

print(numList1)

#count = 0
#while (count < 5):
 #   x = input("Please type a number ");
 #   y = int(x);
 #   numList1.append(y);
 #   count = count + 1;

def remove_duplicates(numList):     
    output = []
    seen = set()
    for num in numList:     # lists as an iterable, different kind of for loop
        # If element num is not been encountered yet,
        # ... add it to both list and set.
        if num not in seen:
            output.append(num)
            seen.add(num)
    return output



for i in range (0, len(numList1)):
    for j in range (0, len(numList2)):
        if (numList1[i] == numList2[j]):
            numList3.append(numList1[i])
            
#for i in range(0 , (len(numList3))):
#    for j in range(1, len(numList3)):
#        if (numList3[i] == numList3[j]):
#            numList3.remove(numList3[j])
print("Before dupping: " + str(numList3))
numList3 = remove_duplicates(numList3)



print(numList1)
print(numList2)
print("List3 after duping " + str(numList3))
