def getMeANumber():
    x = input("Please enter a positive interger: ")
    something = int(x);    
    return something;

def purrFect(num):
    temp = 0
    for i in range(1, num):
        if ((number % i) == 0):
            temp=(temp + i);
            #print(i, " is a factor of ", num)
    if (temp == num):
        print(num, " is a purrfect number!!!  OPA");
        return True
    else: 
        return False 

def isItPurrfect(number):
    if (purrFect(number) == True):
        print(number, " is a purrrrfect number")
    else: 
        print(number," is a dud!  :-( ")

number = getMeANumber()
isItPurrfect(number)
number = number + 1 
while (purrFect(number) == False):
    number = number + 1;
print(number, " is the next purrrfect number!!  OPA")

#getMeANumber()
#nextPurrfect(number)
