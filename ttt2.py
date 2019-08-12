import pygame, sys
from pygame.locals import *
# VARIABLES
WIDTH = 1400
HEIGHT = 1100
scoreX = scoreO = 0
middleX = WIDTH // 2
lineX1 = middleX - 370
lineX2 = middleX + 370
lineY1 = middleX - 125
lineY2 = middleX + 125
endgame = False
turn = 'X'
check = ''
# winning conditions alist
alist = [''] * 9
# rectangles coords
boxes = [[pygame.Rect(lineY1 - 225, 340, 200, 200), True],
        [pygame.Rect(lineY1 + 25, 340, 200, 200), True],
        [pygame.Rect(lineY1 + 275, 340, 200, 200), True],
        [pygame.Rect(lineY1 - 225, 580, 200, 200), True],
        [pygame.Rect(lineY1 + 25, 580, 200, 200), True],
        [pygame.Rect(lineY1 + 275, 580, 200, 200), True],
        [pygame.Rect(lineY1 - 225, 820, 200, 200), True],
        [pygame.Rect(lineY1 + 25, 820, 200, 200), True],
        [pygame.Rect(lineY1 + 275, 820, 200, 200), True]]
# image drawing coords
imageCoords = [(lineY1 - 225, 340),
                (lineY1 + 25, 340),
                (lineY1 + 275, 340),
                (lineY1 - 225, 580),
                (lineY1 + 25, 580),
                (lineY1 + 275, 580),
                (lineY1 - 225, 820),
                (lineY1 + 25, 820),
                (lineY1 + 275, 820)]
# app settings
pygame.init()
fpsClock = pygame.time.Clock()
FPS = 30
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe!')
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
# wrapper and helper functions
def drawImg(surface, img, x, y):
    return surface.blit(img, (x, y))

def drawRect(surface, color, box):
    return pygame.draw.rect(surface, color, box)

def mainDrawRect():
    for box in boxes:
        drawRect(DISPLAYSURF, WHITE, box[0])

def changeTurns(index):
    global img
    global alist
    global turn
    if img == xIMG:
        alist[index] = 'X'
        turn = 'O'
        img = oIMG
    else:
        alist[index] = 'O'
        turn = 'X'
        img = xIMG

def winningConditions(alist):
    if alist[0] == alist[1] == alist[2] and alist[0] != '':
        return (True, alist[0])
    elif alist[3] == alist[4] == alist[5] and alist[3] != '':
        return (True, alist[3])
    elif alist[6] == alist[7] == alist[8] and alist[6] != '':
        return (True, alist[6])
    elif alist[0] == alist[3] == alist[6] and alist[0] != '':
        return (True, alist[0])
    elif alist[1] == alist[4] == alist[7] and alist[1] != '':
        return (True, alist[1])
    elif alist[2] == alist[5] == alist[8] and alist[2] != '':
        return (True, alist[2])
    elif alist[0] == alist[4] == alist[8] and alist[0] != '':
        return (True, alist[0])
    elif alist[2] == alist[4] == alist[6] and alist[2] != '':
        return (True, alist[2])
    elif '' not in alist:
        return (True, 'Draw')

    return (False, None)

def newRound():
    global turn, img, alist, endgame
    turn = 'X'
    img = xIMG
    alist = [''] * 9
    endgame = False
    resetBoxes(boxes)
    mainFrameDraw()

def mainFrameDraw():
    # horizontal lines
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, BLACK, (lineX1, 560), (lineX2, 560), 15)
    pygame.draw.line(DISPLAYSURF, BLACK, (lineX1, 800), (lineX2, 800), 15)
    # vertical lines
    pygame.draw.line(DISPLAYSURF, BLACK, (lineY1, 330), (lineY1, 1020), 15)
    pygame.draw.line(DISPLAYSURF, BLACK, (lineY2, 330), (lineY2, 1020), 15)
    # blit
    DISPLAYSURF.blit(welcome, welcomeRect)
    DISPLAYSURF.blit(X, XRect)
    DISPLAYSURF.blit(O, ORect)

def resetBoxes(boxes):
    for x in boxes:
        x[1] = True
        
# create Font Object
fontObj = pygame.font.Font('freesansbold.ttf', 80)
welcome =  fontObj.render('Welcome to Tic Tac Toe Game!', True, BLACK, WHITE)
welcomeRect = welcome.get_rect()
welcomeRect.center = (WIDTH // 2, 60)
# create X,O font Object
playerFontObj = pygame.font.Font('freesansbold.ttf', 60)
X = playerFontObj.render('Player (X)', True, BLACK, WHITE)
XRect = X.get_rect()
O = playerFontObj.render('Player (O)', True, BLACK, WHITE)
ORect = O.get_rect()
turnFont = playerFontObj.render(str(turn).join(['TURN ( ' , ' )']), True, BLACK, WHITE)
turnRect = turnFont.get_rect()
turnRect.center = (WIDTH // 2, 260)
XRect.center = (WIDTH // 4 + 30, 160)
ORect.center = ((WIDTH // 4) * 3 - 30, 160)
# create Score text
score = playerFontObj.render(' : '.join([str(scoreX), str(scoreO)]), True, BLACK, WHITE)
scoreRect = score.get_rect()
scoreRect.center = (WIDTH // 2, 165)
# load X, O images
xIMG = pygame.image.load('x.png')
oIMG = pygame.image.load('o.png')
img = xIMG

mainFrameDraw()
# main game loop
while True:
    # drawing

    DISPLAYSURF.blit(score, scoreRect)
    DISPLAYSURF.blit(turnFont, turnRect)
    turnFont = playerFontObj.render(str(turn).join(['  TURN   ' , '   ']), True, BLACK, WHITE)
    score = playerFontObj.render(' : '.join([str(scoreX), str(scoreO)]), True, BLACK, WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and not endgame:
                for box, coords in zip(boxes, imageCoords):
                    if box[0].collidepoint(event.pos) and box[1]:
                        print('area clicked')
                        drawImg(DISPLAYSURF, img, coords[0], coords[1])
                        box[1] = False
                        changeTurns(imageCoords.index(coords))
                        print(box[1])
            if event.button == 1 and endgame:
                if check[1] == 'X':
                    scoreX += 1
                elif check[1] == 'O':
                    scoreO += 1
                newRound()


            check = winningConditions(alist)
            if check[0]:
                endgame  = True

    fpsClock.tick(FPS)
    pygame.display.update()
