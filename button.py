# -*- coding=utf-8 -*-

'''参考了这篇文章：https://blog.csdn.net/zhangenter/article/details/89609946'''

import pygame

class Button():
    def __init__(self,parent,rect,text):
        #self.screen = screen
        self.parent = parent
        self.bg_color = (225,225,225)
        self.surface = parent.subsurface(rect)
        self.x,self.y,self.width,self.height = rect
        self._text = text
        self.is_hover = False
        self.is_press = False
        self.init_font()
        self.mouse_pos = []
    
    def init_font(self):
        font = pygame.font.SysFont('arial',28)
        white = 100, 100, 100
        self.textImage = font.render(self._text, True, white)
        w, h = self.textImage.get_size()
        self._tx = (self.width - w) / 2
        self._ty = (self.height - h) / 2

    def check_mouse_event(self,event):
        x,y = pygame.mouse.get_pos()
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            self.is_hover = True
        else:
            self.is_hover = False
        #只有鼠标按下和鼠标松开的时候光标都在按钮范围内才触发按下事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_,y_ = pygame.mouse.get_pos()
            if x_ > self.x and x_ < self.x + self.width and y_ > self.y and y_ < self.y + self.height:
                self.is_press = True
                self.mouse_pos = [True]
            else:self.mouse_pos = [False]
        if event.type == pygame.MOUSEBUTTONUP:
            self.is_press = False
            x_,y_ = pygame.mouse.get_pos()
            if x_ > self.x and x_ < self.x + self.width and y_ > self.y and y_ < self.y + self.height and self.mouse_pos[-1]:
                self.mouse_pos = []
                return True
            else:
                self.mouse_pos = []
                return False
        
    def draw_button(self):
        if self.is_press:
            r,g,b = self.bg_color
            k = 0.99
            self.surface.fill((r*k, g*k, b*k))
        else:
            self.surface.fill(self.bg_color)
        if self.is_hover:
            pygame.draw.rect(self.surface, (0,0,0), (0,0,self.width,self.height), 1)
            pygame.draw.rect(self.surface, (100,100,100), (0,0,self.width-1,self.height-1), 1)
            layers = 5
            r_step = (100-55)/layers
            g_step = (100-55)/layers
            for i in range(layers):
                pygame.draw.rect(self.surface, (170+r_step*i, 205+g_step*i, 255), (i, i, self.width - 2 - i*2, self.height - 2 - i*2), 1)
        else:
            self.surface.fill(self.bg_color)
            pygame.draw.rect(self.surface, (0,0,0), (0,0,self.width,self.height), 1)
            pygame.draw.rect(self.surface, (100,100,100), (0,0,self.width-1,self.height-1), 1)
            pygame.draw.rect(self.surface, self.bg_color, (0,0,self.width-2,self.height-2), 1)
            
        self.surface.blit(self.textImage, (self._tx, self._ty))
                
