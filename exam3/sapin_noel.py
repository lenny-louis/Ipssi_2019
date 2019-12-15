import sys
from math import floor
import random  

jumpline="\n"

def show_tree(lar):
    hauteur=floor((lar/5))+1
    if (lar%2 == 0):
        lar=lar+1
    if lar <= 3:
        tronc=1
    else:
        tronc=3
    tree=""
    nombre_boule=floor(random.random()*lar)

    for i in range(1,lar+1,2):

        tree=tree +(i*"x").center(lar)
        tree=tree+jumpline
    chaine= list(tree)

    for i in range(len(chaine)):
        if (random.random() < lar/100):
            if (chaine[i] == 'x'):
                chaine[i] = 'O'
    tree= "".join(chaine)
    
    for i in range(hauteur):
        if (i<hauteur-1):
            tree=tree+(tronc*"x").center(lar)
            tree=tree+jumpline
        else:
            tree=tree+(tronc*"x").center(lar)
    
    
    return tree
if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))

