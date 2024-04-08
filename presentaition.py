import pygame
import math
import random
from enum import Enum

pygame.init()
FPS = 60
clock = pygame.time.Clock()
title = True
battle = False
pturn = False
bturn = False
clash = False
dmg = 0
atk = 0
dispaly = False
drop = False

# status of game
#   0 -> title
#   1 -> battle
status = 0

# 0 -> bot
# 1 -> rollskill
# 2 -> plact
# 3 -> drop
# 4 -> clash
# 5 -> patk
# 6 -> batk
process = -1

#class status_screen(Enum):
#    title = 0
#    battle = 1

mouse_status = 0




##################################################
#                                                #
#               pygame settings                  #
#                                                #
##################################################

screen = pygame.display.set_mode(size=(2048, 1200))
pygame.display.set_caption("This is a game")

bg = pygame.Surface(screen.get_size())
bg.fill(color=(255, 255,255), rect=None, special_flags=0)
title_bg = pygame.Surface(screen.get_size())
title_bg.fill(color=(255, 255,255), rect=None, special_flags=0)
titletext = pygame.font.Font('freesansbold.ttf', 256)
titletextsurf = titletext.render("Siea vs Izuna", True, (0, 0, 0), (255, 255, 255))
titletextrect = titletextsurf.get_rect()
titletextrect.center = (1024, 500)
start = pygame.font.Font('freesansbold.ttf', 64)
startsurf = start.render("start", True, (0, 0, 0), (0, 0, 255))
blank  = pygame.image.load(".\image\white.png")
p1dis = blank
p2dis = blank



##################################################
#                                                #
#                   ELEMENTS                     #
#                                                #
##################################################

class chr:
    def __init__(self):
        self.image = 0
        self.hp = 50
        self.x = 0
        self.y = 0
        self.point = 0

class skill:
    def __init__(self):
        self.x = 0
        self.y = 1000
        self.image = 0
        self.kind = 0


# siea statement
sy = chr()
sy.image = pygame.image.load(".\image\sy.png")
sy.x = 0
sy.y = 400

# Izuna statement
fox = chr()
fox.image = pygame.image.load(".\image\gox1.jpg")
fox.x = 1600
fox.y = 400
foxsize = fox.image.get_size()
foxsize = (int(foxsize[0] / (3/2)), int(foxsize[1] / (3/2)))
fox.image = pygame.transform.scale(fox.image, foxsize)

#skills

skill_icon = [
    "",
    pygame.image.load(".\image\pierce.png"),
    pygame.image.load(".\image\lunt.png"),
    pygame.image.load(".\image\slash.png"),
    pygame.image.load(".\image\defense.png")
]
skill_dis = [
    '',
    pygame.image.load(".\image\piercedis.png"),
    pygame.image.load(".\image\luntdis.png"),
    pygame.image.load(".\image\slashdis.png"),
    pygame.image.load(".\image\defensedis.png")
]
bskill = skill()
skill_1 = skill()
skill_2 = skill()
skill_2.x = 400
bskill.x = 1000


#sywait = pygame.image.load("C:\屁眼\gay\sysaber")
#sysaber = pygame.image.load("C:\屁眼\gay\螢幕擷取畫面 2024-03-12 185519.png")
#sy = sywait
#syhp = 50
#syx = 0
#syy = 400
#
#fox = pygame.image.load("C:\屁眼\gay\gox1.jpg")
#foxattack = pygame.image.load("C:\屁眼\gay\gox2.png")
#
#foxhp = 50
#
#foxx = 1600
#foxy = 400

#pierce = pygame.image.load("C:\屁眼\gay\pierce.png")
#pierx = -0
#piery = -1000
#pierrect = pierce.get_rect()
#pwidth, pheight = pierce.get_size()
#blunt = pygame.image.load("C:\屁眼\gay\\blunt.png")
#blux = -400
#bluy = -1000
#blurect = blunt.get_rect()
#bwidth, bheight = blunt.get_size()
#slash = pygame.image.load("C:\屁眼\gay\slash.png")
#slax = -400
#slay = -400
#slawidth, sheight = slash.get_size()
#defense = pygame.image.load("C:\屁眼\gay\defense.png")
#defx = -400
#defy = -1000
#dwidth, dheight = defense.get_size()

#skill_1 = slash
#psk1 = 0
#sk_1x = 0
#sk_1y = 1000
#sk_1width, sk_1height=0, 0
#skill_2 = blunt
#psk2 = 0
#sk_2x = 400
#sk_2y = 1000
#sk_2width, sk_2height=0, 0
#bskill = blunt
#bsk = 0
#bskx = 2000
#bsky = 1000
#bskwidth, bskheight = 0, 0
#useskill = False
#p1 = 0
#p2 = 0

numbers = [
    "you're not allow here!!!",
    titletext.render("1", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("2", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("3", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("4", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("5", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("6", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("7", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("8", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("9", True, (0, 0, 0), (255, 255, 255)),
    titletext.render("10", True, (0, 0, 0), (255, 255, 255))
]

# one = titletext.render("1", True, (0, 0, 0), (255, 255, 255))
# two = titletext.render("2", True, (0, 0, 0), (255, 255, 255))
# thr = titletext.render("3", True, (0, 0, 0), (255, 255, 255))
# four = titletext.render("4", True, (0, 0, 0), (255, 255, 255))
# five = titletext.render("5", True, (0, 0, 0), (255, 255, 255))
# six = titletext.render("6", True, (0, 0, 0), (255, 255, 255))
# sev = titletext.render("7", True, (0, 0, 0), (255, 255, 255))
# eig = titletext.render("8", True, (0, 0, 0), (255, 255, 255))
# nine = titletext.render("9", True, (0, 0, 0), (255, 255, 255))
# ten = titletext.render("10", True, (0, 0, 0), (255, 255, 255))

#sladis = pygame.image.load("C:\屁眼\gay\slashdis.png")
#bludis = pygame.image.load("C:\屁眼\gay\luntdis.png")
#piedis = pygame.image.load("C:\屁眼\gay\piercedis.png")
#defdis = pygame.image.load("C:\屁眼\gay\defensedis.png")
#dis    = pygame.image.load("C:\屁眼\gay\white.png")
#p1dis  = pygame.image.load("C:\屁眼\gay\white.png")

#p2dis  = blank

def isInRect(p, rect):
    x1, y1 = p
    x2, y2, len, width = rect
    if(x1 < x2 or x1 > x2 + len) : return False
    elif (y1 < y2 or y1 > y2 + width) : return False
    else: return True

# skill = []

#def skill(s):
#    if s == 1:
#        print('1')
#        return pierce
#    elif s == 2:
#        print(2)
#        return blunt
#    elif s == 3:
#        print('3')
#        return slash
#    elif s == 4:
#        print('4')
#        return defense

# def count(a):
#     if a == 1:
#         return one
#     if a == 2:
#         return two
#     if a == 3:
#         return thr
#     if a == 4:
#         return four
#     if a == 5:
#         return five
#     if a == 6:
#         return six
#     if a == 7:
#         return sev
#     if a == 8:
#         return eig
#     if a == 9:
#         return nine
#     if a == 10:
#         return ten

    
running = True
while running:
    clock.tick(30)
    key_p = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if status == 0:
            screen.blit(title_bg, (0, 0))
            pygame.draw.rect(title_bg, (0, 0, 255), (824, 600, 400, 250))
            screen.blit(titletextsurf, (256, 30))
            screen.blit(startsurf, (950, 680))
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                width, height = 400, 250
                x, y = 824, 600
                if isInRect((mx,my),(x,y,width,height)):
                    status = 1
                    process = 0
        if status == 1:
            if process == 0:
                bskill.kind = random.randint(1, 4)
                bskill.image = skill_icon[bskill.kind]
                #bskwidth, bskheight = bskill.get_size()
                process = 1
                if bskill.kind == 1:
                    fox.point = random.randint(1, 9)
                elif bskill.kind == 2:
                    fox.point = random.randint(5, 7)
                elif bskill.kind == 3:
                    fox.point = random.randint(3, 5)
                elif bskill.kind == 4:
                    fox.point = random.randint(5, 10)
            if process == 1:
                skill_1.kind, skill_2.kind = random.randint(1, 4), random.randint(1, 4)
                skill_1.image = skill_icon[skill_1.kind]
                #sk_1width, sk_1height = skill_1.get_size()
                skill_2.image = skill_icon[skill_2.kind]
                #sk_2width, sk_2height = skill_2.get_size()
                process = 2
            if process == 2:
                dispaly = True
                mx, my = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] and mouse_status == 0:
                    mouse_status = 1
                    mx, my = pygame.mouse.get_pos()
                    if isInRect((mx,my),(0,1000,200,200)):
                        sk_1x, sk_1y = -400, -250
                        useskill = skill_1.kind
                        process = 3
                    elif isInRect((mx,my),(400,1000 ,200,200)):
                        sk_2x, sk_2y = -400, -250
                        useskill = skill_2.kind
                        process = 3
            if process == 3: #drop
                #skill_1 = pygame.image.load("C:\屁眼\gay\white.png")
                #skill_2 = pygame.image.load("C:\屁眼\gay\white.png")
                #bskill = pygame.image.load("C:\屁眼\gay\white.png")
                dispaly = False
                if useskill == 3:
                    sy.point = random.randint(3, 5)
                elif useskill == 1:
                    sy.point = random.randint(1, 9)
                elif useskill == 2:
                    sy.point = random.randint(5, 7)
                elif useskill == 4:
                    sy.point = random.randint(5, 10)
                process = 4
            if process == 4: #clash
                # p1dis = count(p1)
                # p2dis = count(p2)
                p1dis = numbers[sy.point]
                p2dis = numbers[fox.point]
                if useskill == 4 and bskill.kind == 4:
                    process = 0
                elif useskill == 4:
                    process = 6
                elif bskill.kind == 4:
                    process = 5
                elif sy.point > fox.point:
                    process = 5
                elif sy.point == fox.point:
                    process = 0
                elif sy.point < fox.point:
                    process = 6
            if process == 5:
                if useskill == 3:
                    dmg = random.randint(3, 5) + random.randint(3, 5)
                elif useskill == 1:
                    dmg = random.randint(1, 9)
                elif useskill == 2:
                    dmg = random.randint(5, 7)
                if bskill.kind == 4:
                    if fox.point >= dmg:
                        process = 0
                    else:
                        fox.hp -= dmg - fox.point
                        process = 0
                else:
                    fox.hp -= dmg
                    process = 0
            elif process == 6:
                if bskill.kind == 3:
                    dmg = random.randint(3, 5) + random.randint(3, 5)
                elif bskill.kind == 2:
                    dmg = random.randint(1, 9)
                elif bskill.kind == 1:
                    dmg = random.randint(5, 7)
                if useskill == 4:
                    if sy.point >= dmg:
                        clash = False
                        process = True
                    else:
                        sy.hp -= dmg - sy.point
                        process = 0
                else:
                    sy.hp -= dmg
                    process = 0
                atk = 0 
            if sy.hp <= 0 or fox.hp <= 0:
                status = 2
            if dispaly == True:
                if isInRect((mx,my), (0,1000,200,200)):
                    dis = skill_dis[skill_1.kind]
                elif isInRect((mx,my),(400,1000,200,200)):
                    dis = skill_dis[skill_2.kind]
                elif isInRect((mx,my),(1600,1000,200,200)):
                    dis = skill_dis[bskill.kind]
                else:
                    dis = pygame.image.load(".\image\white.png")

            pygame.draw.rect(bg, (255, 0, 0), (0, 300, 400, 20))
            pygame.draw.rect(bg, (0, 255, 0), (0, 300, 8*sy.hp, 20))
            pygame.draw.rect(bg, (255, 0, 0), (1648, 300, 400, 20))
            pygame.draw.rect(bg, (0, 255, 0), (1648+400-8*fox.hp, 300, 8*fox.hp, 20))
            screen.blit(bg, (0, 0))
            screen.blit(fox.image, (fox.x, fox.y))
            screen.blit(sy.image, (0, 400))
            screen.blit(skill_1.image, (0, 1000))
            screen.blit(skill_2.image, (400, 1000))
            screen.blit(bskill.image, (1600, 1000))
            screen.blit(p1dis , (500, 50))
            screen.blit(p2dis, (1200, 50))
            screen.blit(dis, (900, 800))

            if not pygame.mouse.get_pressed()[0] and mouse_status == 1:
                mouse_status = 0
    pygame.display.update()
#你這坨大便


pygame.quit