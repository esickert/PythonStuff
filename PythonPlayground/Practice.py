import unittest
class TestingPython(unittest.TestCase):
#print("This is a practice file");

    def test_palindrome(self):
        word = "aaa"
        back = "aaa"[::-1]
        if word == back:
            print("\nThis is a Palindrome")
        else:
            print("\nNOT A PALINDROME")

#********************************
#This is fibinacci recursive