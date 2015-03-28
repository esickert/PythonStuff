# NumCalculator prompts the user for 3 integers. It then displays
# the sum, product and average of those numbers.  It then calls the 
# function greaterNum to find the greatest of the 3 integers.

#greaterNum() takes 2 integer parameters and returns the larger
def greaterNum(x,y):
    "This returns the greater of 2 numbers", x ,"and", y
    if x > y:
        return x;
    else: return y;

#input is string. The strings need to be converted to integers.
xString = input("Please enter an interger: ")
x = int(xString)
yString = input("...and another integer: ")
y = int(yString)
zString = input("...and one more: ")
z = int(zString)

print("The sum of x, y and z is ",  (x + y + z))
print("The product of x, y and z is", (x * y * z)) 
print("The average of ",x," and ",y," and ",z," is ", (x+y+z)/3)

temp = greaterNum(x,y)
greatest = greaterNum(temp,z)
print (greatest, " is the largest number of ", x,",",y," and ",z)

#examples of a while and for loop
x = 0
while (x < 10):
    print ("SPAM", end=" ");
    x = x + 1;

print(" ")

for x in range (1, 10):
    print("More Spam", end=" ")  # prints a space instead of a newline


