import time;

temps = []
days = 5
temp = 0
count = 0

for i in range(0,days):
    x = input("Please enter a temperature for day " + str(i+1) + " : ")
    y = float(x)
    temps.append(y)
    temp = temp + y
    print(temps)

print("Thank you...please wait")
time.sleep(5)
print("Their sum is ", temp)
average = temp / days;
print("Their average is ", average)
for i in range(0,days):
    if (temps[i] >  average):
        count = count + 1
print("There were ", count, "days hotter than ", average);


#temps.remove(2)   #this removes elements in list!!!!!!!!!!!!!

