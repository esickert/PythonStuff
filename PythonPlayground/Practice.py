import unittest
class TestingPython(unittest.TestCase):
    print("This is a practice file")

    def test_palindrome(self):
        word = "aaa"
        back = "aa"
        if word == back:
            print("\nThis is a Palindrome");
            print("line 10")
        else:
            print("\nThis is NOT A PALINDROME")
#  end of test_palindrome
#**********************************************
    def test_fibinacci(self):
        a = 0
        b = 1
        for i in range(0, 5):
           #print("fibinacci sequence- line 16  IT WORKED i!!!", i);
            c = a + b
            print(c, end=' ')
            a = b
            b = c


