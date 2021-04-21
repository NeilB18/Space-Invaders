import pygame, sys
import random 
from random import choice

def ball_restart():
    global ball,ball_speed_Y,ball_speed_X,screen_width,screen_height
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_Y *=choice((1,-1))
    ball_speed_X *= choice((1,-1))

pygame.init()
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((1000,600))

screen_width = 1000
screen_height = 600
pygame.display.set_caption("Pong")
icon = pygame.image.load('001-ping-pong.png')
pygame.display.set_icon(icon)
running = True
paddle1X = 10
paddle1Y = 10

player1 = 0
player2 = 0

ball = pygame.Rect(490,290,20,20)
paddle1 = pygame.Rect(0,255,10,90)
paddle2 = pygame.Rect(990,255,10,90)

player1_score = 0
player2_score = 0
game_font = pygame.font.Font('freesansbold.ttf',22)
def show_score(x,y):
    main =game_font.render(f"{str(player1_score)}", True, (255,255,255))
    screen.blit(main,(x,y))

def player2_show_score(x,y):
    main2 = game_font.render(f"{str(player2_score)}",True, (255,255,255))
    screen.blit(main2,(x,y))

paddle1_speed = 0
paddle2_speed = 0
ball_speed_X = 5
ball_speed_Y = 5
while running:
    screen.fill((44,44,44))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_speed-=8
            if event.key == pygame.K_o:
                paddle2_speed-=8
            if event.key == pygame.K_s:
                paddle1_speed +=8
            if event.key == pygame.K_k:
                paddle2_speed +=8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1_speed+=8
            if event.key == pygame.K_o:
                paddle2_speed+=8
            if event.key == pygame.K_s:
                paddle1_speed -=8
            if event.key == pygame.K_k:
                paddle2_speed -=8
      
    paddle1.y +=paddle1_speed
    paddle2.y +=paddle2_speed
    ball.x += ball_speed_X
    ball.y += ball_speed_Y
    if ball.top <= 0 or ball.bottom>=screen_height:
        ball_speed_Y*=-1
    if ball.left<= 0:
        player2_score+=1
        ball_restart()
    if ball.right>=screen_width:
        player1_score+=1
        ball_restart()
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_X*=-1
    if paddle1.y <=0:
        paddle1.y = 0
    if paddle1.y >=510:
        paddle1.y = 510
    if paddle2.y <=0:
        paddle2.y = 0
    if paddle2.y >=510:
        paddle2.y = 510
    pygame.draw.ellipse(screen,(255,255,255),ball)
    pygame.draw.rect(screen,(255,255,255),paddle1)
    pygame.draw.rect(screen,(255,255,255),paddle2)
    pygame.draw.aaline(screen,(255,255,255),(screen_width/2,0),(screen_width/2,screen_height))
    show_score(460,270)
    player2_show_score(528,270)
    pygame.display.flip()
    clock.tick(FPS)
