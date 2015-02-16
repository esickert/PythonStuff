names = [
		"Elena", "Thomas", "Hamilton", "Suzie", "Phil", "Matt", "Alex",
		"Emma", "John", "James", "Jane", "Emily", "Daniel", "Neda",
		"Aaron", "Kate"
		]
		
times = [
		341, 273, 278, 329, 445, 402, 388, 275, 243, 334, 412, 393, 299,
		343, 317, 265
		]
print("Name:", "		","Time:")
print("*************************")
#***********************************************************************
temp = times[0];
for i in range(0,len(times)):
	if (names[i] == "Hamilton"):
		print(names[i],"	",times[i], " minutes");
	else:
		print (names[i], "		" ,times[i]," minutes");
#***********************************************************************
for i in range(0,len(times)):
	if (times[i] < temp):
		temp = times[i];
		index = i;
print("*************************");
print(names[index], "has the best time of ", temp, " minutes");
#***********************************************************************
#use the index of the best time to figure out the time of the second best runner.
temp = times[0];
for i in range(0,len(times)):
	if (i == index):
		continue;
	elif (times[i]  < temp):  
		temp = times[i];
print(names[i], "has the second best time of ", temp, " minutes");
print();
