def printList(names, times):
	print("Name:", "		","Time:")
	print("*************************")
	for i in range(0,len(times)):
		if (names[i] == "Hamilton"):
			print(names[i],"	",times[i], " minutes");
		else:
			print (names[i], "		" ,times[i]," minutes");

def bestTime(names, times):
	temp = times[0];
	for i in range(0,len(times)):
		if (times[i] < temp):
			temp = times[i];
			index = i;
	return index;

def secondBestTime(list1, list2):
	temp = times[0];
	index2 = bestTime(list1, list2) #this is printing out the best time twice
	for i in range(0,len(times)):
		if (i == index2):
			continue;
		elif (times[i]  < temp):  
			temp = times[i]
			index3 = i;   #i changes in the for loop; index3 saves it.
	return index3


names = [
		"Elena", "Thomas", "Hamilton", "Suzie", "Phil", "Matt", "Alex",
		"Emma", "John", "James", "Jane", "Emily", "Daniel", "Neda",
		"Aaron", "Kate"
		]
		
times = [
		341, 273, 278, 329, 445, 402, 38, 275, 243, 334, 412, 393, 29,
		343, 317, 265
		]

printList(names,times)
index = bestTime(names, times)
print(names[index], "has the best time of", times[index], "minutes");
index = secondBestTime(names, times)
print(names[index], "has the second best time of ", times[index], " minutes");
print()


