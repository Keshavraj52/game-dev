import pygame
pygame.init()
screen=pygame.display.set_mode((300,300))
screen.fill("white")
pygame.display.set_caption("my first pygame")
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
pygame.display.flip()