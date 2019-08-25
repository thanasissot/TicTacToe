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
gameStarted = False
check = ''
# winning conditions alist
alist = [''] * 9
# rectangles coords
boxes = [[pygame.Rect(lineY1 - 225, 280, 200, 200), True],
        [pygame.Rect(lineY1 + 25, 280, 200, 200), True],
        [pygame.Rect(lineY1 + 275, 280, 200, 200), True],
        [pygame.Rect(lineY1 - 225, 520, 200, 200), True],
        [pygame.Rect(lineY1 + 25, 520, 200, 200), True],
        [pygame.Rect(lineY1 + 275, 520, 200, 200), True],
        [pygame.Rect(lineY1 - 225, 760, 200, 200), True],
        [pygame.Rect(lineY1 + 25, 760, 200, 200), True],
        [pygame.Rect(lineY1 + 275, 760, 200, 200), True]]
# image drawing coords
imageCoords = [(lineY1 - 225, 280),
                (lineY1 + 25, 280),
                (lineY1 + 275, 280),
                (lineY1 - 225, 520),
                (lineY1 + 25, 520),
                (lineY1 + 275, 520),
                (lineY1 - 225, 760),
                (lineY1 + 25, 760),
                (lineY1 + 275, 760)]
# app settings
pygame.init()
fpsClock = pygame.time.Clock()
FPS = 30
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe!')
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GOLDGREY = pygame.Color(140, 132, 115)

# wrapper and helper functions
def drawImg(surface, img, x, y):
    return surface.blit(img, (x, y))

def drawRect(surface, color, box):
    return pygame.draw.rect(surface, color, box)

def mainDrawRect():
    for box in boxes:
        drawRect(DISPLAYSURF, WHITE, box[0])

def resetBoxes(boxes):
    """Helper function, these boxes contain the if clicked boolean value,
    Resets them when game needs to restast, draw or win"""
    for x in boxes:
        x[1] = True

def changeTurns(index):
    global img
    global alist
    global turn
    if img == xIMG:
        alist[index] = 'X'
        turn = (OturnFont, OturnRect)
        img = oIMG
    else:
        alist[index] = 'O'
        turn = (XturnFont, XturnRect)
        img = xIMG

def winningConditions(alist):
    """ when called checking the winning conditions
        or returns 'Draw' in case of all the spots filled
        and there is no winner """
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
    turn = (XturnFont, XturnRect)
    img = xIMG
    alist = [''] * 9
    endgame = False
    resetBoxes(boxes)
    mainFrameDraw()

def mainFrameDraw():
    """ draw the # on the main window"""
    # horizontal lines
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, BLACK, (lineX1, 500), (lineX2, 500), 15)
    pygame.draw.line(DISPLAYSURF, BLACK, (lineX1, 740), (lineX2, 740), 15)
    # vertical lines
    pygame.draw.line(DISPLAYSURF, BLACK, (lineY1, 270), (lineY1, 960), 15)
    pygame.draw.line(DISPLAYSURF, BLACK, (lineY2, 270), (lineY2, 960), 15)
    # blit
    DISPLAYSURF.blit(X, XRect)
    DISPLAYSURF.blit(O, ORect)

def startingScreenDraw():
    """ Draws the starting screen and returns pygame.Rect object
    with coords for the button New Game or Start game as to check
    for the collidepoint(event.pos) to start the game"""
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(welcome, welcomeRect)
    DISPLAYSURF.blit(tictactoe, tictactoeRect)
    pygame.draw.rect(DISPLAYSURF, GOLDGREY,(350, 560, 700, 160))
    DISPLAYSURF.blit(newgamebutton, newgamebuttonRect)
    return pygame.Rect(350, 560, 700, 160)
    
# FONT OBJECT
#############################
## welcome object
fontObj = pygame.font.Font('freesansbold.ttf', 120)
welcome = fontObj.render('welcome to', True, BLACK)
welcomeRect = welcome.get_rect()
welcomeRect.center = (WIDTH // 2, 160)
## tictactoe object
fontObj2 = pygame.font.Font('freesansbold.ttf', 200)
tictactoe = fontObj2.render('Tic Tac Toe', True, BLACK)
tictactoeRect = tictactoe.get_rect()
tictactoeRect.center = (WIDTH // 2, 340)
## new game button object same font with welcome object
newgamebutton = fontObj.render('New Game', True, BLACK)
newgamebuttonRect = newgamebutton.get_rect()
newgamebuttonRect.center = (WIDTH // 2, 640)
## create X font Object
playerFontObj = pygame.font.Font('freesansbold.ttf', 60)
X = playerFontObj.render('Player (X)', True, BLACK, WHITE)
XRect = X.get_rect()
XRect.center = (WIDTH // 4 + 30, 80)
## create O font Object
O = playerFontObj.render('Player (O)', True, BLACK, WHITE)
ORect = O.get_rect()
ORect.center = ((WIDTH // 4) * 3 - 30, 80)
## create X Turn Object
XturnFont = playerFontObj.render('X'.join(['TURN ( ' , ' )']), True, BLACK, WHITE)
XturnRect = XturnFont.get_rect()
XturnRect.center = (WIDTH // 2, 180)
## create O Turn Object
OturnFont = playerFontObj.render('O'.join(['TURN ( ' , ' )']), True, BLACK, WHITE)
OturnRect = OturnFont.get_rect()
OturnRect.center = (WIDTH // 2, 180)
## create Score text
def displayScore(scoreX, scoreO):
    score = playerFontObj.render(' : '.join([str(scoreX), str(scoreO)]), True, BLACK, WHITE)
    scoreRect = score.get_rect()
    scoreRect.center = (WIDTH // 2, 85)
    return score, scoreRect
# IMAGES
#############################
## load X, O images
xIMG = pygame.image.load('x.png')
oIMG = pygame.image.load('o.png')
# set img variabble to xIMG, used for starting turn of X player
img = xIMG
# set turn variable to X as first player always
turn = (XturnFont, XturnRect)

# MUSIC
pygame.mixer.music.load('Background Beat1.wav')
pygame.mixer.music.play(-1)

startingScreenRECT = startingScreenDraw()
# mainFrameDraw()


# main game loop
while True:

    if gameStarted:
        # score
        score, scoreRect = displayScore(scoreX, scoreO)
        # drawing
        DISPLAYSURF.blit(turn[0], turn[1])
        DISPLAYSURF.blit(score, scoreRect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and not endgame and gameStarted:
                for box, coords in zip(boxes, imageCoords):
                    if box[0].collidepoint(event.pos) and box[1]:
                        drawImg(DISPLAYSURF, img, coords[0], coords[1])
                        box[1] = False
                        changeTurns(imageCoords.index(coords))
            if event.button == 1 and endgame:
                if check[1] == 'X':
                    scoreX += 1
                elif check[1] == 'O':
                    scoreO += 1
                newRound()
            if not gameStarted and event.button == 1:
                if startingScreenRECT.collidepoint(event.pos):
                    mainFrameDraw()
                    gameStarted = True


            check = winningConditions(alist)
            if check[0]:
                endgame  = True

    fpsClock.tick(FPS)
    pygame.display.update()