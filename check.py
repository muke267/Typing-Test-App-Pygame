
import pygame
x=pygame.init()
game=pygame.display.set_mode((1200,500))
pygame.display.set_caption("first game")
exit_game= False


while not exit_game:
 for event in pygame.event.get():
     print(event)


 pygame.quit()
 quit()