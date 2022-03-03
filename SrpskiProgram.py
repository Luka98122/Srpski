import pygame
import random

pygame.init()
width = 1000
height = 617
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kosovski Ciklus Igrica")
health = 5

Macevi = []
kreditivi = pygame.image.load("Images\\Krediti.png")
Pravila = pygame.image.load("Images\\Pravila.png")
# LOAD IMAGES
pozadina = pygame.image.load("Images\\Sl1.png")
pozadinaALT1 = pygame.image.load("Images\\Sl2.jpg")
pozadinaALT2 = pygame.image.load("Images\\Sl3.jpg")
Buttons = []
MacWidth = 128
MacHeight = 92
# TEKSTOVI ============================================================================#
Nivoi = []
Filler = pygame.image.load("Images\\Filler1.png")
# NIVO JEDAN #
Nivo1 = [[]]
Nivoi.append(Nivo1)
Pitanje1 = pygame.image.load("Images\\Pitanje1.png")
Resenja1A = pygame.image.load("Images\\Resenja1A.png")
Resenja1B = pygame.image.load("Images\\Resenja1B.png")
Pitanje2 = pygame.image.load("Images\\Pitanje11.png")
Resenja2A = pygame.image.load("Images\\Resenja1A1.png")
Resenja2B = pygame.image.load("Images\\Resenja1B1.png")

# NIVO DVA #
Pitanje3 = pygame.image.load("Images\\Pitanje2.png")
Pitanje3 = pygame.transform.scale(Pitanje3, (290, 100))
Resenja3A = pygame.image.load("Images\\Resenja2A.png")
Resenja3A = pygame.transform.scale(Resenja3A, (290, 100))
Resenja3B = pygame.image.load("Images\\Resenja2B.png")
Resenja3B = pygame.transform.scale(Resenja3B, (290, 100))
Pitanje4 = pygame.image.load("Images\\Pitanje21.png")
Pitanje4 = pygame.transform.scale(Pitanje4, (290, 100))
Resenja4A = pygame.image.load("Images\\Resenja2A1.png")
Resenja4A = pygame.transform.scale(Resenja4A, (290, 100))
Resenja4B = pygame.image.load("Images\\Resenja2B1.png")
Resenja4B = pygame.transform.scale(Resenja4B, (290, 100))
# NIVO TRI #
Pitanje5 = pygame.image.load("Images\\Pitanje3.png")
Resenja5B = pygame.image.load("Images\\Resenja3B.png")
Resenja5A = pygame.image.load("Images\\Resenja3A.png")
Pitanje5 = pygame.transform.scale(Pitanje5, (310, 100))
Resenja5A = pygame.transform.scale(Resenja5A, (290, 100))
Resenja5B = pygame.transform.scale(Resenja5B, (290, 100))
Pitanje6 = pygame.image.load("Images\\Pitanje31.png")
Resenja6A = pygame.image.load("Images\\Resenja3A1.png")
Resenja6B = pygame.image.load("Images\\Resenja3B1.png")
Pitanje6 = pygame.transform.scale(Pitanje6, (310, 100))
Resenja6A = pygame.transform.scale(Resenja6A, (290, 100))
Resenja6B = pygame.transform.scale(Resenja6B, (290, 100))
Pitanje7 = pygame.image.load("Images\\Pitanje4.png")
Resenja7A = pygame.image.load("Images\\Resenja4A.png")
Resenja7B = pygame.image.load("Images\\Resenja4B.png")
Pitanje7 = pygame.transform.scale(Pitanje7, (310, 100))
Resenja7A = pygame.transform.scale(Resenja7A, (290, 100))
Resenja7B = pygame.transform.scale(Resenja7B, (290, 100))
Pitanje8 = pygame.image.load("Images\\Pitanje41.png")
Resenja8A = pygame.image.load("Images\\Resenja4A1.png")
Resenja8B = pygame.image.load("Images\\Resenja4B1.png")
Pitanje8 = pygame.transform.scale(Pitanje8, (310, 100))
Resenja8A = pygame.transform.scale(Resenja8A, (290, 100))
Resenja8B = pygame.transform.scale(Resenja8B, (290, 100))
Pitanje9 = pygame.image.load("Images\\Pitanje5.png")
Resenja9B = pygame.image.load("Images\\Resenja5B.png")
Resenja9A = pygame.image.load("Images\\Resenja5a.png")
Pitanje9 = pygame.transform.scale(Pitanje9, (310, 100))
Resenja9A = pygame.transform.scale(Resenja9A, (290, 100))
Resenja9B = pygame.transform.scale(Resenja9B, (290, 100))

Pitanje10 = pygame.image.load("Images\\Pitanje51.png")
Resenja10B = pygame.image.load("Images\\Resenja5B1.png")
Resenja10A = pygame.image.load("Images\\Resenja5A1.png")
Pitanje10 = pygame.transform.scale(Pitanje10, (310, 100))
Resenja10A = pygame.transform.scale(Resenja10A, (290, 100))
Resenja10B = pygame.transform.scale(Resenja10B, (290, 100))

Pitanje11 = pygame.image.load("Images\\Pitanje6.png")
Resenja11B = pygame.image.load("Images\\Resenja6B.png")
Resenja11A = pygame.image.load("Images\\Resenja6A.png")
Pitanje11 = pygame.transform.scale(Pitanje11, (310, 100))
Resenja11A = pygame.transform.scale(Resenja11A, (290, 100))
Resenja11B = pygame.transform.scale(Resenja11B, (290, 100))

Pitanje12 = pygame.image.load("Images\\Pitanje61.png")
Resenja12B = pygame.image.load("Images\\Resenja6B1.png")
Resenja12A = pygame.image.load("Images\\Resenja6A1.png")
Pitanje12 = pygame.transform.scale(Pitanje12, (310, 100))
Resenja12A = pygame.transform.scale(Resenja12A, (290, 100))
Resenja12B = pygame.transform.scale(Resenja12B, (290, 100))

# Nivo1[0].append(Pitanje1)

# Nivo1[0].append(Resenja1)

doneLever = 0

# MACEVI ===============================================================================#
Macevi1 = pygame.image.load("Images\\Macevi.png")
Macevi1 = pygame.transform.scale(Macevi1, (MacWidth, MacHeight))
Macevi.append([Macevi1, 100, 100])
Buttons.append(pygame.Rect((100, 100), (MacWidth, MacHeight)))
Macevi.append([Macevi1, 330, 100])
Buttons.append(pygame.Rect((330, 100), (MacWidth, MacHeight)))
Macevi.append([Macevi1, 603, 83])
Buttons.append(pygame.Rect((603, 83), (MacWidth, MacHeight)))
Macevi.append([Macevi1, 800, 325])
Buttons.append(pygame.Rect((800, 325), (MacWidth, MacHeight)))
Macevi.append([Macevi1, 600, 407])
Buttons.append(pygame.Rect((600, 407), (MacWidth, MacHeight)))
Macevi.append([Macevi1, 350, 520])
Buttons.append(pygame.Rect((350, 520), (MacWidth, MacHeight)))

# ===========================================#
font = pygame.font.Font("freesansbold.ttf", 32)
text = font.render("Poeni: ", True, pygame.Color("Black"), pygame.Color("White"))
textRect = text.get_rect()
textRect.center = (890, 20)

text1 = font.render("", True, pygame.Color("Black"), pygame.Color("White"))
textRect1 = text1.get_rect()
textRect1.center = (950, 20)


def CheckCollision(rectangle, posy):
    if (
        posy[0] >= rectangle.x
        and posy[0] <= rectangle.x + rectangle.width
        and posy[1] > rectangle.y
        and posy[1] < rectangle.y + rectangle.height
    ):
        return 1
    return 0


lever = 0
tempButtons = []
miniLever = 0
stage = 0
start = 0
while True:
    text1 = font.render(str(health), True, pygame.Color("Black"), pygame.Color("White"))
    ev = pygame.event.get()
    mPos = 0
    for event in ev:
        if start == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mPos = pygame.mouse.get_pos()
                if CheckCollision(pygame.Rect(0, 0, 838, 629), mPos) == True:
                    start = 1
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mPos = pygame.mouse.get_pos()
            if lever == 0:
                for i in range(len(Buttons)):
                    if CheckCollision(Buttons[i], mPos) == True:
                        lever = i + 1
            else:
                for i in range(len(tempButtons)):
                    if CheckCollision(tempButtons[i], mPos) == True:
                        miniLever = i + 1

    screen.fill(pygame.Color("Green"))
    screen.blit(pozadina, (0, 0))
    if start == 0:
        screen.blit(Pravila, (0, 0))
    if start == 1:
        for i in range(len(Macevi)):
            screen.blit(Macevi[i][0], (Macevi[i][1], Macevi[i][2]))
        if lever == 1:
            if stage == 0:
                screen.blit(Pitanje1, (150, 150))
                screen.blit(Resenja1A, (500, 210))
                screen.blit(Resenja1B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
            if stage == 1:
                screen.blit(Pitanje2, (150, 150))
                screen.blit(Resenja2A, (500, 210))
                screen.blit(Resenja2B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
        if lever == 2:
            if stage == 0:
                screen.blit(Pitanje3, (150, 150))
                screen.blit(Resenja3A, (500, 210))
                screen.blit(Resenja3B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
                if miniLever == 2:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
            if stage == 1:
                screen.blit(Pitanje4, (150, 150))
                screen.blit(Resenja4A, (500, 210))
                screen.blit(Resenja4B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
        if lever == 3:
            if stage == 0:
                screen.blit(Pitanje5, (150, 150))
                screen.blit(Resenja5A, (500, 210))
                screen.blit(Resenja5B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
            if stage == 1:
                screen.blit(Pitanje6, (150, 150))
                screen.blit(Resenja6A, (500, 210))
                screen.blit(Resenja6B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
                if miniLever == 2:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
        if lever == 4:
            if stage == 0:
                screen.blit(Pitanje7, (150, 150))
                screen.blit(Resenja7A, (500, 210))
                screen.blit(Resenja7B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
            if stage == 1:
                screen.blit(Pitanje8, (150, 150))
                screen.blit(Resenja8A, (500, 210))
                screen.blit(Resenja8B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
                if miniLever == 2:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
        if lever == 5:
            if stage == 0:
                screen.blit(Pitanje9, (150, 150))
                screen.blit(Resenja9A, (500, 210))
                screen.blit(Resenja9B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
            if stage == 1:
                screen.blit(Pitanje10, (150, 150))
                screen.blit(Resenja10A, (500, 210))
                screen.blit(Resenja10B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
                if miniLever == 2:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
        if lever == 6:
            if stage == 0:
                screen.blit(Pitanje11, (150, 150))
                screen.blit(Resenja11A, (500, 210))
                screen.blit(Resenja11B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 1
            if stage == 1:
                screen.blit(Pitanje12, (150, 150))
                screen.blit(Resenja12A, (500, 210))
                screen.blit(Resenja12B, (500, 310))
                tempButtons = [
                    pygame.Rect((500, 210), (270, 90)),
                    pygame.Rect((500, 310), (270, 90)),
                ]
                if miniLever == 1:
                    health = health + 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
                    doneLever = 1
                if miniLever == 2:
                    health = health - 1
                    lever = 0
                    miniLever = 0
                    print(health)
                    stage = 0
                    doneLever = 1
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    if doneLever == 1:
        screen.blit(kreditivi, (250, 150))
    pygame.display.flip()

    if health < 1:
        exit()
