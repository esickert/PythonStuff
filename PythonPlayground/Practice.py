import unittest
class TestingPython(unittest.TestCase):
#print("This is a practice file");

    def test_palindrome(self):
        word = "aaaaa"
        back = "aaaaa"[::-1]
        if word == back:
            print("This is a Palindome")
        else:
            print("NOT A PALINDROME")

#("************************************")

    def test_fibinacci(self):
        variable = "abcdef[::-1]"
        if variable != variable:
            print("FIBINACCI SEQUENCE")
        else:
            print("end of else")

