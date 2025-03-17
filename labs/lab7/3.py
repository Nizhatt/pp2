import pygame
pygame.init()
screen=pygame.display.set_mode((800, 600))
color="white"
screen.fill(color)
cx=400
cy=300
pygame.draw.circle(screen, "red", (cx, cy), 25)
running=True
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                if cx+25+20<=800:
                    cx+=20
            if event.key==pygame.K_LEFT:
                if cx-25-20>=0:
                    cx-=20
            if event.key==pygame.K_UP:
                if cy-25-20>0:
                    cy-=20
            if event.key==pygame.K_DOWN:
                if cy+25+20<=600:
                    cy+=20
    pygame.draw.circle(screen, "red", (cx, cy), 25)
 
    pygame.display.flip()