import pygame
import random
pygame.init()

widthDisplay = 500
heightDisplay = 500
 
back = (200, 255, 255)
mw = pygame.display.set_mode((widthDisplay, heightDisplay))
mw.fill(back)
clock = pygame.time.Clock()
 
game = True
class Area():
    def __init__(self, x=0, y=0, widht=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, widht, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def collidepoint(self, rect):
        return self.rect.collidepoint(rect)
#5
bird = Picture("bird.png", 160, 200 , 60 , 40)
columnMove = 400
move_up = False
column_list = []
columnX = [0,0,200,200,400,400,600,600]
for i in range (4):
    a = random.randint(100,300)
    columnDownY = widthDisplay - a
    columnUpY =  widthDisplay - a - 450
    column = Picture("column.png",i*200+500, columnDownY,100,300)
    column = Picture("column.png",i*200+500, columnUpY,100,300,180)
    column_list.append(column)
    column_list.append(columnl)


     
     
