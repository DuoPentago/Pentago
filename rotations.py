import copy

def rotateleft(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    return liste

def rotateright(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    return liste

def rotation(liste,cadran,sens):
    if sens == True:

        if cadran == 1:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(-1)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(-1)
            cadrancopy = rotateright(cadrancopy)
            for x in range(len(liste)//2):
                for y in range(len(liste)//2):
                    liste[x][y] = cadrancopy[x][y]


        if cadran == 2:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(-1)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(0)
            cadrancopy = rotateright(cadrancopy)
            for x in range(len(liste)//2):
                for y in range(1,(len(liste)//2)+1):
                    liste[x][-y] = cadrancopy[x][-y]


        if cadran == 3:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(0)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(-1)
            cadrancopy = rotateright(cadrancopy)
            for x in range(1,(len(liste)//2)+1):
                for y in range(len(liste)//2):
                    liste[-x][y] = cadrancopy[-x][y]

        if cadran == 4:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(0)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(0)
            cadrancopy = rotateright(cadrancopy)
            for x in range(1,(len(liste)//2)+1):
                for y in range(1,(len(liste)//2)+1):
                    liste[-x][-y] = cadrancopy[-x][-y]

    else:
        if cadran == 1:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(-1)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(-1)
            cadrancopy = rotateleft(cadrancopy)
            for x in range(len(liste)//2):
                for y in range(len(liste)//2):
                    liste[x][y] = cadrancopy[x][y]


        if cadran == 2:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(-1)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(0)
            cadrancopy = rotateleft(cadrancopy)
            for x in range(len(liste)//2):
                for y in range(1,(len(liste)//2)+1):
                    liste[x][-y] = cadrancopy[x][-y]


        if cadran == 3:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(0)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(-1)
            cadrancopy = rotateleft(cadrancopy)
            for x in range(1,(len(liste)//2)+1):
                for y in range(len(liste)//2):
                    liste[-x][y] = cadrancopy[-x][y]

        if cadran == 4:
            cadrancopy = copy.deepcopy(liste)
            for i in range(len(liste)//2):
               cadrancopy.pop(0)
            for x in range (len(liste)//2 ):
                for j in range(len(liste)//2 ):
                    cadrancopy[x].pop(0)
            cadrancopy = rotateleft(cadrancopy)
            for x in range(1,(len(liste)//2)+1):
                for y in range(1,(len(liste)//2)+1):
                    liste[-x][-y] = cadrancopy[-x][-y]

