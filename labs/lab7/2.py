import pygame
pygame.init()
pygame.mixer.init()
running=True
screen=pygame.display.set_mode((800, 600))
# sound=pygame.mixer.Sound(C:\Users\irresible\Desktop\pp2labs)
# sound.play()
arr=[r"C:\Users\irresible\Desktop\pp2labs\s1.mp3", 
     r"C:\Users\irresible\Desktop\pp2labs\s2.mp3",
     r"C:\Users\irresible\Desktop\pp2labs\s3.mp3",
     r"C:\Users\irresible\Desktop\pp2labs\s4.mp3",
     ]
photo=["img1.png", "img2.png", "try.jpg", "img4.png"]
cur=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
               pygame.mixer.music.load(arr[cur])
               image=pygame.image.load(photo[cur])
               screen.blit(image, (0, 0))
               pygame.mixer.music.play()
            if event.key==pygame.K_RIGHT:
                cur+=1
                if cur>len(arr)-1:
                    cur-=1
                    pass
                else: 
                   pygame.mixer.music.load(arr[cur])
                   pygame.mixer.music.play()
                   image=pygame.image.load(photo[cur])
                   screen.fill((0, 0, 0))
                   screen.blit(image, (0, 0))
            if event.key==pygame.K_LEFT:
                cur-=1
                if cur<0:
                    cur+=1
                    pass
                else: 
                    pygame.mixer.music.load(arr[cur])
                    pygame.mixer.music.play()
                    image=pygame.image.load(photo[cur])
                    screen.fill((0, 0, 0))
                    screen.blit(image, (0, 0))
            if event.key==pygame.K_q:
                pygame.mixer.music.stop()
           
        pygame.display.flip()
pygame.quit()