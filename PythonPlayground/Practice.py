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
    for i in range(1, 11):
        print("fibinacci sequence- line 16  IT WORKED i!!!", i);
