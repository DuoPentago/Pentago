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

    if len(liste) == 4:
        if sens == True:

            if cadran == 1:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2):
                    cadrancopy.pop(i-len(liste)//2)
                    for x in range(len(cadrancopy)//2 +1):
                        cadrancopy[x].pop(-1)
                cadrancopy = rotateright(cadrancopy)
                liste[0][0] = cadrancopy[0][0]
                liste[0][1] = cadrancopy[0][1]
                liste[1][0] = cadrancopy[1][0]
                liste[1][1] = cadrancopy[1][1]

            if cadran == 2:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2):
                    cadrancopy.pop(i-len(liste)//2)
                    for x in range(len(cadrancopy)//2 +1):
                        cadrancopy[x].pop(0)
                cadrancopy = rotateright(cadrancopy)
                liste[0][2] = cadrancopy[0][0]
                liste[0][3] = cadrancopy[0][1]
                liste[1][2] = cadrancopy[1][0]
                liste[1][3] = cadrancopy[1][1]

            if cadran == 3:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2):
                    cadrancopy.pop(0)
                    for x in range(len(cadrancopy)//2 +1):
                        cadrancopy[x].pop(-1)
                cadrancopy = rotateright(cadrancopy)
                liste[2][0] = cadrancopy[0][0]
                liste[2][1] = cadrancopy[0][1]
                liste[3][0] = cadrancopy[1][0]
                liste[3][1] = cadrancopy[1][1]

            if cadran == 4:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2 ):
                    cadrancopy.pop(0)
                for x in range(len(liste)//2):
                    cadrancopy[x].pop(0)
                    cadrancopy[x].pop(0)
                print(cadrancopy)
                cadrancopy = rotateright(cadrancopy)
                liste[2][2] = cadrancopy[0][0]
                liste[2][3] = cadrancopy[0][1]
                liste[3][2] = cadrancopy[1][0]
                liste[3][3] = cadrancopy[1][1]

        else:
            if cadran == 1:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2):
                    cadrancopy.pop(i-len(liste)//2)
                    for x in range(len(cadrancopy)//2 +1):
                        cadrancopy[x].pop(-1)
                cadrancopy = rotateleft(cadrancopy)
                liste[0][0] = cadrancopy[0][0]
                liste[0][1] = cadrancopy[0][1]
                liste[1][0] = cadrancopy[1][0]
                liste[1][1] = cadrancopy[1][1]

            if cadran == 2:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2):
                    cadrancopy.pop(i-len(liste)//2)
                    for x in range(len(cadrancopy)//2 +1):
                        cadrancopy[x].pop(0)
                cadrancopy = rotateleft(cadrancopy)
                liste[0][2] = cadrancopy[0][0]
                liste[0][3] = cadrancopy[0][1]
                liste[1][2] = cadrancopy[1][0]
                liste[1][3] = cadrancopy[1][1]

            if cadran == 3:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2):
                    cadrancopy.pop(0)
                    for x in range(len(cadrancopy)//2 +1):
                        cadrancopy[x].pop(-1)
                cadrancopy = rotateleft(cadrancopy)
                liste[2][0] = cadrancopy[0][0]
                liste[2][1] = cadrancopy[0][1]
                liste[3][0] = cadrancopy[1][0]
                liste[3][1] = cadrancopy[1][1]

            if cadran == 4:
                cadrancopy = copy.deepcopy(liste)
                for i in range(len(liste)//2 ):
                    cadrancopy.pop(0)
                for x in range(len(liste)//2):
                    cadrancopy[x].pop(0)
                    cadrancopy[x].pop(0)
                print(cadrancopy)
                cadrancopy = rotateleft(cadrancopy)
                liste[2][2] = cadrancopy[0][0]
                liste[2][3] = cadrancopy[0][1]
                liste[3][2] = cadrancopy[1][0]
                liste[3][3] = cadrancopy[1][1]

