import random

n=1


def down(num):
    for i in range(100):
        print(num)
        if num%2==0:
            num//=2
        else:
            num*=3
            num+=1

def propagate(i):
    newi=[]
    if ((i - 1) / 3) % 2 != 0:
        i1 = (i - 1) / 3
        i2 = i * 2
        if i1.is_integer():
            newi.append([i1, i2])
        else:
            newi.append(i2)
    else:
        i *= 2
        newi.append(i)
    return newi

def recurse(list_maybe):
    while type(list_maybe)== list:
        pass


tree=[1]
for clock, branch in enumerate(tree):
    while type(branch)==list:

    tree.append(propagate(branch))

#4,2,1
#future me: build the tree ground up