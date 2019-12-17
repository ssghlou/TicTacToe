import pygame
import sys

import chess
def check_keydown(chess,screen,st,retract_button,replay_button):
    '''检测按键'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_position(mouse_x,mouse_y,chess,st)
            check_button(screen,retract_button,replay_button,  
                chess,mouse_x,mouse_y)

def check_position(mouse_x,mouse_y,chess,st):
    '''产生点击的坐标'''
    a = ''
    position1 = ''
    position2 = []
    
    if mouse_x >= st.center_x - 142.5 and mouse_x <= st.center_x - 52.5:
        a += '1'
    elif mouse_x >= st.center_x - 45 and mouse_x <= st.center_x + 45:
        a += '2'
    elif mouse_x >= st.center_x + 52.5 and mouse_x <= st.center_x + 142.5:
        a += '3'

    if mouse_y >= st.center_y - 142.5 and mouse_y <= st.center_y - 52.5:
        a += '4'
    elif mouse_y >= st.center_y - 45 and mouse_y <= st.center_y + 45:
        a += '5'
    elif mouse_y >= st.center_y + 52.5 and mouse_y <= st.center_y + 142.5:
        a += '6'
        
    if len(a) > 1:
        if a[0] == '1':
            if mouse_x >= st.center_x - 142.5 and mouse_x <= st.center_x - 113.5:
                position1 += '1'
                position2.append(str(st.center_x - 142))
            elif mouse_x >= st.center_x - 112 and mouse_x <= st.center_x - 83:
                position1 += '2'
                position2.append(str(st.center_x - 111.5))
            elif mouse_x >= st.center_x - 81.5 and mouse_x <= st.center_x - 52.5:
                position1 += '3'
                position2.append(str(st.center_x - 81))
            
        elif a[0] == '2' :
            if mouse_x >= st.center_x - 45 and mouse_x <= st.center_x - 16:
                position1 += '4'
                position2.append(str(st.center_x - 44.5))
            elif mouse_x >= st.center_x - 14.5 and mouse_x <= st.center_x + 14.5:
                position1 += '5'
                position2.append(str(st.center_x - 14))
            elif mouse_x >= st.center_x + 16 and mouse_x <= st.center_x + 45:
                position1 += '6'
                position2.append(str(st.center_x + 16.5))
                
        elif a[0] == '3':
            if mouse_x >= st.center_x + 52.5 and mouse_x <= st.center_x + 81.5:
                position1 += '7'
                position2.append(str(st.center_x + 53))
            elif mouse_x >= st.center_x + 83 and mouse_x <= st.center_x + 112:
                position1 += '8'
                position2.append(str(st.center_x + 83.5))
            elif mouse_x >= st.center_x + 113.5 and mouse_x <= st.center_x + 142.5:
                position1 += '9'
                position2.append(str(st.center_x + 114))
        
        if a[1] == '4':
            if mouse_y >= st.center_y - 142.5 and mouse_y <= st.center_y - 113.5:
                position1 += '1'
                position2.append(str(st.center_y - 142))
            elif mouse_y >= st.center_y - 112 and mouse_y <= st.center_y - 83:
                position1 += '2'
                position2.append(str(st.center_y - 111.5))
            elif mouse_y >= st.center_y - 81.5 and mouse_y <= st.center_y - 52.5:
                position1 += '3'
                position2.append(str(st.center_y - 81))
            
        elif a[1] == '5' :
            if mouse_y >= st.center_y - 45 and mouse_y <= st.center_y - 16:
                position1 += '4'
                position2.append(str(st.center_y - 44.5))
            elif mouse_y >= st.center_y - 14.5 and mouse_y <= st.center_y + 14.5:
                position1 += '5'
                position2.append(str(st.center_y - 14))
            elif mouse_y >= st.center_y + 16 and mouse_y <= st.center_y + 45:
                position1 += '6'
                position2.append(str(st.center_y + 16.5))
                
        elif a[1] == '6':
            if mouse_y >= st.center_y + 52.5 and mouse_y <= st.center_y + 81.5:
                position1 += '7'
                position2.append(str(st.center_y + 53))
            elif mouse_y >= st.center_y + 83 and mouse_y <= st.center_y + 112:
                position1 += '8'
                position2.append(str(st.center_y + 83.5))
            elif mouse_y >= st.center_y + 113.5 and mouse_y <= st.center_y + 142.5:
                position1 += '9'
                position2.append(str(st.center_y + 114))

        if len(position1) > 1 and len(position2) > 1:
            chess.save(position1,position2)

def check_button(screen,retract_button,replay_button,chess,mouse_x,mouse_y):
    '''检查是否点击按钮'''
    if retract_button.rect.collidepoint(mouse_x,mouse_y):
        chess.retract()
    elif replay_button.rect.collidepoint(mouse_x,mouse_y):
        chess.O1.clear()
        chess.O2.clear()
        chess.X1.clear()
        chess.X2.clear()

def draw(chess,screen,st):
	'''绘制图形'''
	imageX = pygame.image.load('images/X.bmp')
	imageO = pygame.image.load('images/O.bmp')
	imageXr = pygame.image.load('images/Xr.bmp')
	imageOr = pygame.image.load('images/Or.bmp')
	image_frame = pygame.image.load('images/frame.gif')
	image_big_frame = pygame.image.load('images/big_frame.gif')

	#绘制普通棋子
	for position2 in chess.O2:
		screen.blit(imageO,(float(position2[0]),float(position2[1])))
	for position2 in chess.X2:
		screen.blit(imageX,(float(position2[0]),float(position2[1])))
	
	#绘制最后一颗棋子
	if len(chess.X1) > len(chess.O1) :
		screen.blit(imageXr,(float(chess.X2[-1][0]),float(chess.X2[-1][1])))
	elif len(chess.X1) == len(chess.O1) and len(chess.X1) > 0:
		screen.blit(imageOr,(float(chess.O2[-1][0]),float(chess.O2[-1][1])))
	
	#绘制下棋区域
	last_position = ''  #上一个棋的位置，若无，则空
	if len(chess.X1) > len(chess.O1):
		last_position = chess.X1[-1]
	elif len(chess.X1) == len(chess.O1) and len(chess.X1) > 0:
		last_position = chess.O1[-1]
	if last_position:
		x = (int(last_position[0])-1)%3+1   #x,y为上一个棋对应的宫的相对位置
		y = (int(last_position[1])-1)%3+1
		x_position = st.top_left_corner[0]+(x-1)*97.5     #这两个变量为绘制的框的绝对位置
		y_position = st.top_left_corner[1]+(y-1)*97.5     #97.5为棋盘的宫的宽度加上粗边的宽度
		screen.blit(image_frame,(x_position,y_position))
	else:
		screen.blit(image_big_frame,(st.top_left_corner[0],st.top_left_corner[1]))
