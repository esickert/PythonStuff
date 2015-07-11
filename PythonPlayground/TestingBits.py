file = open('test.dat','w')
file.write("010101000111000000")

f = open('test.dat', 'r')
count = 0
while True:
    ch = f.read(1)
    print ch
    if not ch: break
    if ch == "1":
        count = count + 1
        print (count)
#print (count)


#Two different coding styles for the same thing

#this checks n.strip() if equal to "hello" and if so breaks out of the while loop
#n = raw_input("Please enter 'hello':")
#while n.strip() != 'hello':
#    n = raw_input("Please enter 'hello':")


#this while loop is aleays executed until they type "hello" the it breaks out
#while True:
#    n = raw_input("Please enter 'hello':")
#    if n.strip() == 'hello':
#        break
