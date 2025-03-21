import pygame
pygame.init()
screen = pygame.display.set_mode((200,200))
sounds = [
    pygame.mixer.Sound('s1.mp3'),
    pygame.mixer.Sound('s2.mp3'),
    pygame.mixer.Sound('s3.mp3'),
    pygame.mixer.Sound('s4.mp3'),
]
a = 0
running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        sounds[a].play()
    elif keys[pygame.K_s]:
        sounds[a].stop()
    elif keys[pygame.K_RIGHT]:
        if a == 3:
            a = 0
        else:
            a += 1
    elif keys[pygame.K_LEFT]:
        if a == 0:
            a = 3
        else: 
            a-=1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
