import pygame
from datetime import datetime
import os
import time

width,height = 950,230
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Clock")
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 20)

zero = [True,True,True,True,True,False,True]
one = [False,True,True,False,False,False,False]
two = [True,True,False,True,True,True,False]
three = [True,True,True,True,False,True,False]
four = [False,True,True,False,False,True,True]
five = [True,False,True,True,False,True,True]
six = [True,False,True,True,True,True,True]
seven = [True,True,True,False,False,False,False]
eight = [True,True,True,True,True,True,True]
nine = [True,True,True,False,False,True,True]

class SSD():
    def __init__(self,x):
        self.x = x
        self.y = 20
        self.n = 0
        self.lines = [True,True,True,True,True,True,True]

    def draw(self,win):
        if self.lines[0]:
            pygame.draw.rect(win,(255,255,255),(self.x+20-1,self.y+10-1,60,10),3)
            pygame.draw.rect(win,(255,0,0),(self.x+20,self.y+10,60,10))
        if self.lines[1]:
            pygame.draw.rect(win,(255,255,255),(self.x+80-1,self.y+20-1,10,60),3)
            pygame.draw.rect(win,(255,0,0),(self.x+80,self.y+20,10,60))
        if self.lines[2]:
            pygame.draw.rect(win,(255,255,255),(self.x+80-1,self.y+90-1,10,60),3)
            pygame.draw.rect(win,(255,0,0),(self.x+80,self.y+90,10,60))
        if self.lines[3]:
            pygame.draw.rect(win,(255,255,255),(self.x+20-1,self.y+150-1,60,10),3)
            pygame.draw.rect(win,(255,0,0),(self.x+20,self.y+150,60,10))
        if self.lines[4]:
            pygame.draw.rect(win,(255,255,255),(self.x+10-1,self.y+90-1,10,60),3)
            pygame.draw.rect(win,(255,0,0),(self.x+10,self.y+90,10,60))
        if self.lines[5]:
            pygame.draw.rect(win,(255,255,255),(self.x+20-1,self.y+80-1,60,10),3)
            pygame.draw.rect(win,(255,0,0),(self.x+20,self.y+80,60,10))
        if self.lines[6]:
            pygame.draw.rect(win,(255,255,255),(self.x+10-1,self.y+20-1,10,60),3)
            pygame.draw.rect(win,(255,0,0),(self.x+10,self.y+20,10,60))

    def set(self,num):
        if num == 1:
            self.lines = one
        elif num == 2:
            self.lines = two
        elif num == 3:
            self.lines = three
        elif num == 4:
            self.lines = four
        elif num == 5:
            self.lines = five
        elif num == 6:
            self.lines = six
        elif num == 7:
            self.lines = seven
        elif num == 8:
            self.lines = eight
        elif num == 9:
            self.lines = nine
        elif num == 0:
            self.lines = zero

clock = pygame.time.Clock()
ssds = []
for i in range(6):
    ssd = SSD(i*150+50)
    ssds.append(ssd)

now = datetime.now()

scount = int(now.strftime("%S"))
mcount = int(now.strftime("%M"))
hcount = int(now.strftime("%H"))
run = True
while run:
    time.sleep(0.5)
    now = datetime.now()
    scount = int(now.strftime("%S"))
    mcount = int(now.strftime("%M"))
    hcount = int(now.strftime("%H"))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    ssds[0].set(hcount//10)
    ssds[1].set(hcount%10)
    ssds[2].set(mcount//10)
    ssds[3].set(mcount%10)
    ssds[4].set(scount//10)
    ssds[5].set(scount%10)

    for ssd in ssds:
        ssd.draw(win)

    pygame.draw.circle(win,(255,255,255),(325,90),10)
    pygame.draw.circle(win,(255,255,255),(325,150),10)

    pygame.draw.circle(win,(255,255,255),(625,90),10)
    pygame.draw.circle(win,(255,255,255),(625,150),10)
    
    text = font.render(time.strftime("%Y-%m-%d"), True, (255, 255, 255))
    win.blit(text, (width-text.get_width()-10,height-text.get_height()-10))

    pygame.display.update()

pygame.quit()
exit()