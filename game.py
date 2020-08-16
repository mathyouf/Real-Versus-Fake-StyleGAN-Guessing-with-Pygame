import pygame
import os, random, time

pygame.init()
score  = 0
IsItReal = True

colors = {
    "black": (255,255,255),
    "grey": (155,155,155)
}

allGuesses = []
correctGuesses = []
wrongGuesses = []

def createArrows(colors, highlight):
    x = 600
    y = 660
    for color in colors:
        highlighted = 1
        if highlight:
            highlighted = 1.5
        if color == 'green':
            # Create Green Arrow
            font = pygame.font.Font('C:/Users/MatthewFisher/Desktop/DeepLearning/RealVFake/fonts/OpenSans-Bold.ttf', 70)
            text = font.render('REAL', True, (255,255,255), (0,100*highlighted,0)) 
            pygame.draw.polygon(screen, (0, 100*highlighted, 0), ((x+0, y+100), (x+0, y+200), (x+200, y+200), (x+200, y+250), (x+300, y+150), (x+200, y+50), (x+200, y+100)))
            screen.blit(text, (x+25,y+100))
        if color == 'red':
            x = x-150
            y = y+300
            # Create Red Arrow
            font = pygame.font.Font('C:/Users/MatthewFisher/Desktop/DeepLearning/RealVFake/fonts/OpenSans-Bold.ttf', 70)
            text = font.render('FAKE', True, (255,255,255), (100*highlighted,0,0)) 
            pygame.draw.polygon(screen, (100*highlighted, 0, 0), ((x-0, y-100), (x-0, y-200), (x-200, y-200), (x-200, y-250), (x-300, y-150), (x-200, y-50), (x-200, y-100)))
            screen.blit(text, (x-200,y-200))
    pygame.display.flip()

def renderNewFace():
    global IsItReal
    IsItReal = random.choice([True, False])
    if IsItReal == True:
        path = "C:/Users/MatthewFisher/Desktop/DeepLearning/RealVFake/pictures/real/"
    else:
        path = "C:/Users/MatthewFisher/Desktop/DeepLearning/RealVFake/pictures/fake/5veryhard/"
    face = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
    faceimg = pygame.image.load(path + face)
    allGuesses.append(faceimg)
    faceimg = pygame.transform.scale(faceimg, (600,600))
    screen.blit(faceimg, (225,100))

def checkResult(MyGuess):
    global score
    global IsItReal
    time.sleep(0.2)
    if MyGuess == IsItReal:
        score += 1
        correctGuesses.append(allGuesses[-1])
    else:
        score -= 1
        wrongGuesses.append(allGuesses[-1])

def renderScore():
    newString = 'Score: ' + str(score)
    writeText(string=newString, location=(430, 0), font_color=colors["black"],bg_color=colors["grey"], font="OpenSans", size=70)

def resetScreen():
    screen.fill((155,155,155))
    renderNewFace()
    createArrows(['green','red'],highlight=False)
    for index, guess in enumerate(allGuesses):
        face = pygame.transform.scale(guess, (100,100))
        pos = 110*index+10
        print(pos)
        screen.blit(face,(pos, 10))
    # renderScore()

def writeText(string, location, font_color, bg_color, font, size):
    if font == 'OpenSans':
        font = pygame.font.Font('C:/Users/MatthewFisher/Desktop/DeepLearning/RealVFake/fonts/OpenSans-Bold.ttf', size)
    else:
        font = pygame.font.Font('C:/Users/MatthewFisher/Desktop/DeepLearning/RealVFake/fonts/proxima_nova.ttf', size)
    print(string)
    text = font.render(string, True, font_color, bg_color) 
    screen.blit(text, location)

GameOn = True
screen = pygame.display.set_mode(size=(1080,920))
screen.fill((155,155,155))
resetScreen()
while GameOn:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOn = False
        if event.type == pygame.KEYDOWN:
            # Left Key (Fake)
            if event.key == 276:
                createArrows(['red'],highlight=True)
                checkResult(False)
                resetScreen()
            # Right Key (Real)
            if event.key == 275:
                createArrows(['green'],highlight=True)
                checkResult(True)
                resetScreen()
            # Escape Key
            if event.key == 27:
                GameOn = False
pygame.display.quit()