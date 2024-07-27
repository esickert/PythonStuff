import unittest
class TestingPython(unittest.TestCase):
#print("This is a practice file");

    def test_palindrome(self):
        word = "aaaa"
        back = "aaaaa"[::-1]
        if word == back:
            print("\nThis is a Palindrome")
        else:
            print("\nNOT A PALINDROME")

#*******************************

    def test_fibinacci(self):
        # Fibonacci Series in Python Using For Loop
        # initialize two variables, with value 0
        a, b = 0, 1
        series_length = 10
        print(a, b, end=' ')
        for i in range(series_length):
            c = a + b
            print(c, end=' ')
            a = b
            b = c
#*******************************
"""
self = 1
nterms = 0
print("nterms")

def test_recur_fibo(self):
    if self == 1
   print("self")
 #   else:
 #   return(test_recur_fibo(self - 1) + test_recur_fibo(self - 2))

nterms = 0
print("nterms")

# check if the number of terms is valid
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
    for i in range(nterms):
        print(test_recur_fibo(i), "", end="", flush=True)
"""








