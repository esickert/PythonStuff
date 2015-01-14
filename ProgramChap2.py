num = input("Enter a number ")
x = num % 10;
print "The right most digit in ", num,"is ", x
y = num / 10
print y
z = y % 10
print "The right most digit in ", y," is", z
a = y / 10
print a 
b = a % 10
print "The right most digit in ", a, "is", b
print "Added up they equal ", x + z + b
