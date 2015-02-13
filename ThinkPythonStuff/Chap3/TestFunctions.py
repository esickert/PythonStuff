        

def lumberJack(bruce):
    print("I'm a lumberjack and I'm okay!");
    print(bruce)
def repeat_lyrics(b):
    lumberJack(b)
    lumberJack(b)
    lumberJack(b)

#using a function in python
#a = 17
#lumberJack(a)
#repeat_lyrics(a)

def rightJustify(s):
    print((65 * " ") + s)

a = "monty"
print(len(a))
rightJustify(a)

def printSpam(b):
    print("Spam")
    print(b)

def printTwice(f,x):
    f(x)
    f(x)

x = "Im here"    
#printSpam()
printTwice(printSpam, x)
