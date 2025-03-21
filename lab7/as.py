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