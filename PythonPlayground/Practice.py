import unittest
"""
System.out .println("********************************************************");
System.out.println("FIBINACI");
System.out.println("PALINDROME");
System.out.println("Find Largest");
System.out.println("********************************************************");
"""
class TestingPython(unittest.TestCase):
    print("This is a practice file/test of python unit test")

    def test_palindrome(self):
       # print("Testing for palindone")
        word = "aaa"
        back = "aa"
        if word == back:
            print("\nThis is a Palindrome");
            print("line 10")
        else:
            print("\nThis is NOT A PALINDROME")
#  end of test_palindrome
#******************************
    def test_fibinacci(self):
        a = 0
        b = 1
        for i in range(0, 10):
           #print("fibinacci sequence- line 16  IT WORKED i!!!", i);
            c = a + b
            print(c, end=' ')
            a = b
            b = c
#*********************************
print("TESTING GGGGGGGG  !!!!! line 26")
"""
 @Test
  public void fibRec()  {
    for(int i = 0; i <= 10; i++) {
      System.out.print(" " + recursive(i));
    }
    System.out.println("\n");
  }
  public int recursive(int x)  {
      if ((x == 0) || (x == 1))
        return x;
      else  {
        return (recursive(x-1) + recursive(x-2));
      }
  }
  //*********************************

print("TESTING GGGGGGGG  !!!!! line 43")

    def test_fibrecusive(n):
        print("test of fibanacci recusive")
        n = 5
        for i in range(0, n):
            print("!!!!!!!!!!!!", i)
# This doesnt work!~!!!!!!!!
    test_fibrecusive(5)
"""



