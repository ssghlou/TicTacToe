import pygame.font

from button import Button

class Windows():
    def __init__(self,screen,msg1,msg2,msg3,left,top):
        self.screen = screen
        self.width, self.height = 200,200
        self.text_color = (255, 255, 255)
        self.bg_color = (20,40,150)
        self.font = pygame.font.SysFont(None, 60)
        self.rect = pygame.Rect(left,top,self.width, self.height)
        self.msg2_button = Button(screen, (170,300,160,40),text='Yes')
        self.msg3_button = Button(screen, (170,350,160,40),text='No')
        self.prep_msg(msg1)
        
    def prep_msg(self,msg1):
        self.msg_image = self.font.render(msg1, True, self.text_color,self.bg_color)
        
    def draw_windows(self):
        pygame.draw.rect(self.screen,self.bg_color,self.rect,0)
        self.screen.blit(self.msg_image, (170,220))
        self.msg2_button.draw_button()
        self.msg3_button.draw_button()
