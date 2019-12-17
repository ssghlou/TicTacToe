import pygame.font
import sys

sys.dont_write_bytecode = True
class Button():
    def __init__(self,screen,msg,rect_x,rect_y):
        self.screen = screen
        
        self.width,self.height = 100, 30
        self.button_color = (66,66,66)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,30)
        
        self.rect = pygame.Rect(rect_x,rect_y,self.width,self.height)
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

    
            
        
