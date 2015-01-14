import os
# subprocess permits system commands to be called from within the script
#import subprocess

f = open('test.dat','w')
for x in range(0, 3):
    f.write("1110011001100100001")

f = open('test.dat', 'r')
count = 0
while True:
    ch = f.read(1)
    #print ch
    if not ch: break
    if ch == "0":
        count = count + 1
        #print (ch)
print (count)

#The following line deletes the file created with f = open(<filename>,'w')
os.remove('test.dat')

#Two different coding styles for the same thing

#n = raw_input("Please enter 'hello':")
#while n.strip() != 'hello':
#    n = raw_input("Please enter 'hello':")


#while True:
#    n = raw_input("Please enter 'hello':")
#    if n.strip() == 'hello':
#        break
