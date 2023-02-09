import pygame
import random
import time
from math import *
def rotate(surface, angle, pivot, offset): 
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  
    rotated_offset = offset.rotate(angle) 
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect 
massive1 = []
a = 0
speed = -400
class BULLET():
    def __init__(self, x, y, speed, spaw) -> None:
         self.x = x
         self.y = y
         self.speedx = speed
         self.speedy = speed
         self.spaw = spaw
    def spawn(self):
        pygame.draw.circle(screen, "WHITE", (self.x, self.y), 25)
    def move(self):
        self.x += self.speedx; self.y += self.speedy

class PVOBULLET():
        def __init__(self, x, y, speedx, sppedy, angle) -> None:
         self.x = x
         self.y = y
         self.speedx = speedx
         self.speedy = sppedy
         self.angle = angle
        def spawn(self):
            pygame.draw.circle(screen, "WHITE", (self.x, self.y), 10)
        def update(self):
            self.speedy += 3
            self.x += ((self.speedx) * cos(radians(self.angle))) / 60; self.y += ((self.speedy) * sin(radians(self.angle)) + 30 ) / 60
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BG_COLOR = (250, 100, 50)
PADDLE_COLOR = (20, 20, 20)
STAND_COLOR = (46, 102, 159)

field = pygame.Rect(0, SCREEN_HEIGHT - 100,  SCREEN_WIDTH, 100)
stand = pygame.Rect((SCREEN_WIDTH / 2 - 100),SCREEN_HEIGHT - 140 , 200, 40)

offset = pygame.math.Vector2(0, -25)
pivot = [(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 120]
angle = 0


player_img = pygame.image.load("gun3.png")
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AirDefense")
run = True
BULLET.x = random.randint(100, 1500); BULLET.y = random.randint(50, 500)
bullet2 = PVOBULLET((0 / 2 + (sin(radians(angle)) * 120)), (0 - (120 + cos(radians(angle)) * 120)),0, 0, 0)
#print((SCREEN_WIDTH / 2 + (sin(radians(90 + angle)) * 120)), (SCREEN_HEIGHT -  (100 + (cos(radians(90 + angle)) * 120))))
massive1 = [BULLET(random.randint(200 , 1400), 100, random.randint(1, 3), False) for i in range(4)]
while run:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and angle <= 75:
            angle += 5
    elif keys[pygame.K_a] and angle >= -75:
            angle -= 5            
    if keys[pygame.K_SPACE]:
        bullet2 = PVOBULLET((SCREEN_WIDTH / 2 + (sin(radians(angle)) * 120)), (SCREEN_HEIGHT - (120 + cos(radians(angle)) * 120)),speed, speed, angle + 90)
        bullet2.spawn()
    rotated_image, rect = rotate(player_img, angle, pivot, offset)
    screen.fill(BG_COLOR)
    bullet2.spawn()
    bullet2.update()
    screen.blit(rotated_image, rect)
    pygame.draw.rect(screen, PADDLE_COLOR, field)
    pygame.draw.rect(screen, STAND_COLOR, stand)
    for i in range(4):
        if a % 60 == 0:
            if a == 180:
                a = 0
            if a % 60 == 0 and massive1[a // 60].spaw != True:
                massive1[a // 60].spaw = True
                massive1[a // 60].spawn()
                massive1[a // 60].move()
        if ((abs(bullet2.x - massive1[i].x) <= 25) and(abs(abs(bullet2.y - massive1[i].y) <= 25)) ):
            bullet2 = PVOBULLET((0 / 2 + (sin(radians(angle)) * 120)), (0 - (120 + cos(radians(angle)) * 120)),speed, speed, angle + 90)            
            massive1[i] = BULLET(random.randint(200 , 1400), 100, random.randint(1, 3), False)
            print(True) 
        if massive1[i].y >= 800 or massive1[i].x <= 0 or massive1[i].x >= 1600:

            massive1[1] = BULLET(random.randint(200 , 1400), 100, random.randint(1, 3), False)
        elif massive1[i].spaw == True:
            massive1[i].spawn()
            massive1[i].move()
            continue
    a += 1 
    print(a)   
    clock.tick(60)
    #print(cos(radians(angle)))
    pygame.display.flip()