import copy

def rotateright(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    return liste

def rotateleft(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    return liste

def rotation(liste,cadran,sens):
    if sens == True:
        if cadran == 1:
            pass

liste = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

cadran1 = copy.deepcopy(liste)

for i in range(len(liste)//2):
    cadran1.pop(i-len(liste)//2)
    for x in range(len(cadran1)//2 +1):
        cadran1[x].pop(-1)

cadran1 = rotateright(cadran1)
liste[0][0]
print(cadran1)
print (liste)
