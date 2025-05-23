import unittest
class TestingPython(unittest.TestCase):
#print("This is a practice file");

    def test_palindrome(self):
        word = "aaa"
        back = "aa"[::-1]
        if word == back:
            print("\nThis is a Palindrome")
        else:
            print("\nThis is NOT A PALINDROME")
#********************************
print("This is a fibinacci recursive method")