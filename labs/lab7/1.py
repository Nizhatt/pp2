import pygame
import datetime
screen=pygame.display.set_mode((800, 600))
running=True
cloc = pygame.time.Clock()

while running:
    now = datetime.datetime.now()
    seconds = now.second #+ now.microsecond / 1000000  -12
    minutes = (now.minute + seconds / 60) -10
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    clock=pygame.image.load("clock.png")
    min_hand=pygame.image.load("min_hand.png")
    sec_hand=pygame.image.load("sec_hand.png")
    screen.blit(clock, (0, 0))
            # screen.blit(min_hand, (0, 0))
            # screen.blit(sec_hand, (0, 0))
    angle_s=-seconds*6
    angle_m=-minutes*6
    r_m=pygame.transform.rotate(min_hand, angle_s)
    r_s=pygame.transform.rotate(sec_hand, angle_m)
    rect_sec = r_s.get_rect(center=(400, 300))
    rect_min = r_m.get_rect(center=(400, 300))

    screen.blit(r_s, rect_sec.topleft)
    screen.blit(r_m, rect_min.topleft)
       

      
    cloc.tick(60)
    pygame.display.flip()