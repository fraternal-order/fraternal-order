import pygame
 
限制高度 = int(input('\n>限制高度\n\n>'))
 
pygame.init()
 
pygame.display.set_caption('飞机模拟器')
 
screen = pygame.display.set_mode([1000,700])
 
飞行高度 = 0
 
X坐标 = 500
 
Y坐标 = 350
 
实际Y坐标 = 350
 
飞行高度 = 实际Y坐标 * 3
 
c_color = (0,255,0)
 
keep_going = True
 
screen.fill((0,0,0))
 
危险距离线Y坐标 = 350 - (( 限制高度 / 3 ) -350 )
开始线 = (0,危险距离线Y坐标)
结束线 = (1000,危险距离线Y坐标)
pygame.draw.line(screen,(0,0,255),开始线,结束线,10)
 
pygame.draw.circle(screen, c_color, (500,350), 10)
largeText = pygame.font.Font('simkai.ttf',60)
实质话语 = '目前高度:' + str(飞行高度)
largeText = largeText.render(实质话语, True, (255,255,255))
screen.blit(largeText,(0,0))
 
pygame.display.update()
 
while keep_going == True: #如果满足[重复是否允许 - 是]就开始循环
 
    for event in pygame.event.get(): #启动监听
             
        if event.type == pygame.KEYDOWN: #监听判断是否按下键盘
            if event.key == pygame.K_DELETE:#监听判断是否按下键盘中的Delete/删除
                keep_going = False #重复是否允许 - 否/退出循环
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if(飞行高度 > 限制高度):
                    Y坐标 -= 1
                    实际Y坐标 += 1
                    飞行高度 = 实际Y坐标 * 3
                    screen.fill((0,0,0))
                    pygame.draw.line(screen,(0,0,255),开始线,结束线,10)
                    pygame.draw.circle(screen, c_color, (X坐标,Y坐标), 10)
                    largeText = pygame.font.Font('simkai.ttf',60)
                    实质话语 = '目前高度:' + str(飞行高度)
                    largeText = largeText.render(实质话语, True, (255,0,0))
                    screen.blit(largeText,(0,0))
                    pygame.display.update()
                else:
                    Y坐标 -= 1
                    实际Y坐标 += 1
                    飞行高度 = 实际Y坐标 * 3
                    screen.fill((0,0,0))
                    pygame.draw.line(screen,(0,0,255),开始线,结束线,10)
                    pygame.draw.circle(screen, c_color, (X坐标,Y坐标), 10)
                    largeText = pygame.font.Font('simkai.ttf',60)
                    实质话语 = '目前高度:' + str(飞行高度)
                    largeText = largeText.render(实质话语, True, (255,255,255))
                    screen.blit(largeText,(0,0))
                    pygame.display.update()
                 
            if event.key == pygame.K_DOWN:
                if(飞行高度 > 限制高度):
                    Y坐标 += 1
                    实际Y坐标 -= 1
                    飞行高度 = 实际Y坐标 * 3
                    screen.fill((0,0,0))
                    pygame.draw.line(screen,(0,0,255),开始线,结束线,10)
                    pygame.draw.circle(screen, c_color, (X坐标,Y坐标), 10)
                    largeText = pygame.font.Font('simkai.ttf',60)
                    实质话语 = '目前高度:' + str(飞行高度)
                    largeText = largeText.render(实质话语, True, (255,0,0))
                    screen.blit(largeText,(0,0))
                    pygame.display.update()
                else:
                    Y坐标 += 1
                    实际Y坐标 -= 1
                    飞行高度 = 实际Y坐标 * 3
                    screen.fill((0,0,0))
                    pygame.draw.line(screen,(0,0,255),开始线,结束线,10)
                    pygame.draw.circle(screen, c_color, (X坐标,Y坐标), 10)
                    largeText = pygame.font.Font('simkai.ttf',60)
                    实质话语 = '目前高度:' + str(飞行高度)
                    largeText = largeText.render(实质话语, True, (255,255,255))
                    screen.blit(largeText,(0,0))
                    pygame.display.update()
 
            if event.key == pygame.K_RETURN:
                限制高度 = int(input('\n>限制高度\n\n>'))
                if 限制高度 > 2000 :
                    print('限制高度无法超过2000!!!')
                     
                else:
                     
                    if(飞行高度 > 限制高度):
                        screen.fill((0,0,0))
 
                        危险距离线Y坐标 = 350 - (( 限制高度 / 3 ) -350 )
                        开始线 = (0,危险距离线Y坐标)
                        结束线 = (1000,危险距离线Y坐标)
                        pygame.draw.line(screen,(0,0,255),开始线,结束线,10)
                        pygame.display.update()
                     
                        pygame.draw.circle(screen, c_color, (X坐标,Y坐标), 10)
                        largeText = pygame.font.Font('simkai.ttf',60)
                        实质话语 = '目前高度:' + str(飞行高度)
                        largeText = largeText.render(实质话语, True, (255,0,0))
                        screen.blit(largeText,(0,0))
                        pygame.display.update()
                    else:
                        screen.fill((0,0,0))  
                        危险距离线Y坐标 = 350 - (( 限制高度 / 3 ) -350 )
                        开始线 = (0,危险距离线Y坐标)
                        结束线 = (1000,危险距离线Y坐标)
                        pygame.draw.line(screen,(0,0,255),开始线,结束线,10)
                        pygame.display.update()
                     
                        pygame.draw.circle(screen, c_color, (X坐标,Y坐标), 10)
                        largeText = pygame.font.Font('simkai.ttf',60)
                        实质话语 = '目前高度:' + str(飞行高度)
                        largeText = largeText.render(实质话语, True, (255,255,255))
                        screen.blit(largeText,(0,0))
                        pygame.display.update()
pygame.quit()
