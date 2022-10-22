__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

# I denne oppgaven skal vi først lage et sudoku-spill (før vi lager en sudoku-løser om noen år).
# Om du ikke kjenner reglene til sudoku kan du lese deg opp på de selv her: https://no.wikipedia.org/wiki/Sudoku. Del 1 tar seg av å lage et spillbart sudoku-brett.
# Du står fritt til å bygge opp brettet slik som du vil, men brettet skal oppfylle følgende krav:
#   Brukeren skal kunne skrive inn et tall i en valgfri celle. Dersom tallet ikke er gyldig, dvs. ikke mellom 1 og 9, skal en feilmelding skrives ut.
#   Brukeren skal ikke kunne fylle inn et tall som allerede finnes i den samme raden, kolonnen eller kvadratet.
#   Brukeren skal kunne slette et tall fra en celle.
#   Hver gang brukeren fyller inn eller sletter et tall skal det nye brettet skrives ut på en fin måte. Et eksempel kan være som vist under (tallene over og ved siden av brettet angir her henholdsvis kolonne- og radnummer).
#   Brukeren skal kunne laste inn et brett fra en tekstfil.
#   Et halvutfylt brett skal kunne lagres til fil, slik at man kan fullføre det senere.
#   Spillet skal skrive ut en hyggelig gratulasjonsmelding dersom man har klart brettet.
#   Alt skal utføres gjennom et brukervennlig grensesnitt. Det vil si at brukeren ikke skal trenge å kalle på funksjonene selv, men at alt gjøres via input eller ved å lese fra/skrive til fil.

boardInfo = []

def readFromFile(filename):
    openFile = open(filename,"r")
    size = int(openFile.readline())
    board = [[0 for i in range(size)]for i in range(size)]
    stringMatrix = []
    for line in openFile.readlines():
        stringMatrix.append(line.strip())
    print(stringMatrix)
    for i in range(9):
        for j in range(9):
            board[i][j] = int(stringMatrix[i][j])
    openFile.close()
    return board

boardInfo = readFromFile("sudoku.txt")
print(boardInfo)

# Oppgave 2.3
#Lag en funksjon som printer brettet/sudokuen på en ryddig måte:
""" f.ek.
     0   1   2   3
   ------------------
0  | 3 | 4 # 1 | 0 |
   ------------------
1  | 0 | 2 # 0 | 0 |
   ==================
2  | 0 | 0 # 2 | 0 |
   ------------------
3  | 0 | 1 # 4 | 3 |
   ------------------
"""

def boardPrint():
    print("     0   1   2   3")
    print("   ------------------")
    print("0  |",boardInfo[0][0],"|",boardInfo[0][1],"#",boardInfo[0][2],"|",boardInfo[0][3],"|")
    print("   ------------------")
    print("1  |",boardInfo[1][0],"|",boardInfo[1][1],"#",boardInfo[1][2],"|",boardInfo[1][3],"|")
    print("   ==================")
    print("2  |",boardInfo[2][0],"|",boardInfo[2][1],"#",boardInfo[2][2],"|",boardInfo[2][3],"|")
    print("   ------------------")
    print("3  |",boardInfo[3][0],"|",boardInfo[3][1],"#",boardInfo[3][2],"|",boardInfo[3][3],"|")
    print("   ------------------")

boardPrint()


# Oppgave 2.4
#Lag en funksjon getHorizontalList(x,y) som returnerer en liste med alle tallene som finnes på samme linje som koordinaten i argumentet (parameteren)

def getHorizontalList(x,y):
    return boardInfo[y]


# Oppgave 2.5
#Lag en funksjon getVerticalList(x,y) som returnerer en liste med alle tallene som finnes på samme rad som koordinaten i argumentet (parameteren)

def getVerticalList(x,y):
    vertList = []
    for i in range(4):
        vertList.append(boardInfo[i][x])
    return vertList


#Oppgave 2.6
#Lag en funksjon getSquareList(x,y) som returnerer en liste med alle tallene som finnes i samme «rute» som koordinaten i argumentet (parameteren)

def getSquareList(x,y):
    xSquare = x // 2
    ySquare = y // 2
    sqList = []
    for i in range(2):
        for j in range(2):
            sqList.append(boardInfo[2*ySquare+j][2*xSquare+i])
    return sqList

# Oppgave 2.7
# Lag en funksjon getConflictNumbers(x,y) som kombinerer de tre forrige funksjonene
#getHorizontalList(x,y)
#getVerticalList(x,y)
#getSquareList(x,y)
#for å finne alle tall som IKKE kan brukes i den gitte koordinaten


def getConflictNumbers(x,y):
    notPossible = set()
    for element in getHorizontalList(x,y):
        notPossible.add(element)
    for element in getVerticalList(x,y):
        notPossible.add(element)
    for element in getSquareList(x,y):
        notPossible.add(element)
    return notPossible




# Oppgave 2.8
# Lag en funksjon checkMove(number,x,y): som sjekker om tallet «number»
# kan plasseres i koordinate x,y uten å lage noen nye konflikter med andre tall.




def checkMove(number,x,y):
    if boardInfo[y][x] is not 0:
        return False
    possibe = {1,2,3,4}
    notPossible = getConflictNumbers(x,y)
    print(notPossible)
    possibe.difference_update(notPossible)
    print(possibe)
    return number in possibe

def doMove(number,x,y):
    if checkMove(number,x,y):
        boardInfo[y][x] = number
        boardPrint()
    else:
        print("Invalid number or location")

