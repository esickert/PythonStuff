#test = open("newFile","w")
#test.write("hello world")

f = open('test.dat', 'r')
count = 0
while True:
    ch = f.read()
    print ch
    if not ch: break
    if ch == "1":
        count = count + 1
#print count

#Two different coding styles for the same thing

#n = raw_input("Please enter 'hello':")
#while n.strip() != 'hello':
#    n = raw_input("Please enter 'hello':")


#while True:
#    n = raw_input("Please enter 'hello':")
#    if n.strip() == 'hello':
#        break
