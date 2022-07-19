import turtle
import pygame
 
step = int(input("按空格退出\n01 = 慢\n10 = 超快\n游戏速度:"))
t = turtle.Pen()
turtle.setup(1000,1000)
 
pygame.init()
pygame.display.set_mode((100, 100))
pygame.display.set_caption("贪吃蛇")
pygame.display.update()
 
pygame.display.update()
 
t.pensize(20)
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                t.setheading(180)
            if event.key == pygame.K_RIGHT:
                t.setheading(0)
            if event.key == pygame.K_UP:
                t.setheading(90)
            if event.key == pygame.K_DOWN:
                t.setheading(-90)
            if event.key == pygame.K_SPACE:
                running = False
    t.forward(step)
t.down()
