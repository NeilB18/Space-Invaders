import pygame 
from random import randint as rt
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

scores = [] #to keep track of scores

bg = pygame.image.load('space-galaxy-background.jpg')

player1 = pygame.image.load('X-wing.png')
playerx = 370
playery = 480
playerx_change = 0

enemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =    []  
num_of_enemies = 6



for x in range(num_of_enemies):
    enemy.append(pygame.image.load('Alien.png'))
    enemyX.append(rt(0,735))
    enemyY.append(rt(0,50))
    enemyX_change.append(2)
    enemyY_change.append(40)

bullet = pygame.image.load('001-bullet.png')

bulletX = 500 
bulletY = 480
bulletX_change = 0
bulletY_change =  10
# Bullet State
bullet_state = "ready"

def player(a,x,y):
    screen.blit(a,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"   
    screen.blit(bullet,(x+16,y+10))

def check_collision(x1,y1,x2,y2):
    d = math.sqrt((math.pow(x2-x1 ,2))+(math.pow(y2-y1,2)))
    if d < 27:
        return True
    else: 
        return False


score_value =0
font = pygame.font.Font('freesansbold.ttf',22)
game = pygame.font.Font('freesansbold.ttf',64)

textx = 10
texty = 0




def show_score(x,y):
    score = font.render("Score : "+str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))



def game_over_text(x,y):
   
    over_text = game.render("GAME OVER!",True,(255,255,255))
    
    screen.blit(over_text,(x,y)) 




running = True
while running is True:
    screen.fill((0, 0, 55))   
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -2
            if event.key == pygame.K_RIGHT:
                playerx_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerx
                    fire_bullet(bulletX,bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change=0
              
    playerx += playerx_change

    if playerx <=0:
        playerx = 0
        
    elif playerx >= 736:
        playerx = 736
        
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyY[i]>300:
            for j in range(num_of_enemies):
                enemyY[j] =200000000000000
                
        
                game_over_text(200,250)
                

            break



        if enemyX[i] <=0:
            enemyX_change[i]= 2
            enemyY[i] +=enemyY_change[i]
        elif  enemyX[i]>= 736:
            enemyX_change[i]= -2    
            enemyY[i] +=enemyY_change[i]
        collision = check_collision(enemyX[i],enemyY[i],bulletX,bulletY)

        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            scores.append(score_value)
            enemyX[i] = rt(0,735)  
            enemyY[i] = rt(0,50)
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
        player(enemy[i],enemyX[i],enemyY[i])
    if bulletY<=0:
        bulletX = playerx
        bulletY = 480
        bullet_state ="ready"
    
    if bullet_state == "Fire":
        
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change



    player(player1,playerx,playery)
    show_score(textx,texty)

    pygame.display.update()
 