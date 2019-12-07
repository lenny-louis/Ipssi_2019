#!/usr/bin/python3

import sys

def show_tree(x):
    y=int(x/5)+1
    if (x%2 == 0):
        x=x+1
    if (x <= 3):
        tronc="x"
    else:
        tronc="xx"
    arbre=""
    for n in range(1,x+1,2):
        arbre=arbre +(n*"x").center(x)
        jumpline="\n"
        arbre=arbre+jumpline
        
    for n in range(y):
        if (n<y-1):
            arbre=arbre+(tronc).center(x)
            arbre=arbre+jumpline
        else:
            arbre=arbre+(tronc).center(x)
    return arbre

if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))
