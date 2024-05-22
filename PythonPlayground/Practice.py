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

#*****************************

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
#*********************************

 #   def test_fibrec(self):
 #       a = 0;
        b = 1;
        c = a + b;

  #      def fibrec(c):
  #      if c == 1:
  #          return 1
  #      for c  in range(3):
  #          print("practice recursion")

   #         fibrec()

 #***********************************




