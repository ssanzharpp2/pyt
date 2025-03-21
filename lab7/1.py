import pygame
import datetime
pygame.init()
clx = 800
cly = 600
screen = pygame.display.set_mode((clx,cly))
body = pygame.image.load('mickey_clock.png')
clrec = body.get_rect(center=(clx/2,cly/2))
hand = pygame.image.load('hp2.webp')
handrec = hand.get_rect(center=(200, 200))
hand1 = pygame.image.load('hp2.webp')
handrec1 = hand1.get_rect(center=(250, 366))
def rotate_hand(image, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    rotated_rect.move_ip(offset)
    return rotated_image, rotated_rect
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -((minutes % 60) / 60) * 360  
    second_angle = -((seconds % 60) / 60) * 360  

    rotated_right_hand, right_hand_rect = rotate_hand(hand, minute_angle, clrec.center, (-90, -10))
    rotated_left_hand, left_hand_rect = rotate_hand(hand1, second_angle, clrec.center, (-90, -10))
    screen.blit(body, clrec)
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)
    pygame.display.flip()



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
    


import pygame
pygame.init()
screen = pygame.display.set_mode((500,500)) 
bx = 250
by = 250
bm = 20
running = True
while running:
    screen.fill((225, 225, 225))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and by > 30:
                by -= bm
            elif event.key == pygame.K_DOWN and by < 470:
                by += bm
            elif event.key == pygame.K_LEFT and bx > 30:
                bx -= bm
            elif event.key == pygame.K_RIGHT and bx < 470:
                bx += bm
        if event.type == pygame.QUIT:
            running = False 
    pygame.draw.circle(screen, 'red', (bx, by), 25)
    pygame.display.update()