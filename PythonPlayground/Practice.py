import unittest
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
#**********************************************
    def test_fibinacci(self):
        a = 0
        b = 1
        for i in range(0, 10):
           #print("fibinacci sequence- line 16  IT WORKED i!!!", i);
            c = a + b
            print(c, end=' ')
            a = b
            b = c
#**********************************************
    def test_fibrecusive(self):
        print("test of fibanacci recusive")
        for i in range(1, 6):
            print("hellofibinacci sequence- line IT WORKED i!!!", i);
"""
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

"""

#***********************************************
print("find largest!!!")
a = {3,66,4,65,2,3,54,8,5,76,444,6,7,8}
print(a)

"""
int[] a = {3,66,4,65,2,3,54,8,5,76,444,6,7,8};
    int temp = 0;
    for(int i = 0; i < a.length -1; i++)  {
      if (temp < a[i])
        temp = a[i];
    }
    System.out.println("The largest is " + temp);
"""


