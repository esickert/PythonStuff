print("Please enter a word all in caps:");
n = input();
print(n)
n = input("Please enter a word all in capitals:")
print "The word is " + n
word = list(n)  #converts the string into a list of chars
score = 0;
while n != "quit":      #this will loop until user types 'quit'
    score = 0
    word = list(n)
    for i in range (0, len(word)):
        if (word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or  word[i] == 'L' or word[i] == 'N' or
            word[i] == 'O' or  word[i] == 'R' or word[i] == 'S' or word[i] == 'T' or word[i] == 'U'):     #note parentheses!!!!! for long lines
            score = score + 1;
#            print("line 22 score is " + str(score));
        elif  word[i] == 'D' or word[i] == 'G':
            score = score + 2;
#            print("line 25 score is " + str(score));
        elif word[i] == 'B' or word[i] == 'C' or word[i] == 'M' or word[i] == 'P':
            score = score + 3;
#            print ("line 28 score is " + str(score));
        elif  word[i] == 'F' or word[i] == 'H' or word[i] == 'V' or  word[i] == 'W' or word[i] == 'Y':
            score = score + 4;
#            print("line 32 score is " + str(score));
        elif word[i] == 'K':
            score = score + 5;
#            print("line 35 score is " + str(score));
        elif word[i] == 'J' or word[i] == 'X':
            score = score + 8;
#            print("line 38 score is " + str(score));
        elif word[i] == 'Q' or word[i] == 'Z':
            score = score + 10;word
#            print("line 41 score is " + str(score));
        else:
            print ("Wrong input")
            break;
    print(n + " is worth " + str(score) + " points!!  :-) ")
    n = input("Please enter an another word:")
    if n == "quit":
        print("Bye Bye!!");
        break;
    else:
        print("The word is " + n)


#A, E, I, L, N, O, R, S, T, U
#Points 	Letters
#1 	A, E, I, L, N, O, R, S, T, U
#2 	D, G
#3 	B, C, M, P
#4 	F, H, V,W, Y
#5 	K
#8 	J, X
#10 Q, Z    



