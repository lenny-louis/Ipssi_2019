import random as r
import sys
#get input
#n = int(input())
n = int(sys.argv[1])
#make the top of the tree
print(n*' '+'x')
#this loop draws the entire tree's body--
#--------------------------------
for i in range(1,n):
 #s is stored as a string of length i*2 with * and ~ in random positions, this is used for the body of the tree
 s = ''.join(r.choice(['x','o',r.choice(['x','o'])]) for i in range(i*2))
 #string sl and sr holds the random string for the left and right side boundary of the tree's body
 sl = r.choice(['x'])
 sr = r.choice(['o'])
 #print all of 'em at last
 print((n-i)*' '+sl+s+sr)
#print the trunk

if (n%2 == 0):
        n=n+1
        if (n <= 3):
            print((n-1)*' ' + "x")
            print((n-1)*' ' + "x")
        else:
            print((n-1)*' ' + "xx")
            print((n-1)*' ' + "xx")
    
#print((n-1)*' ' + "xx")