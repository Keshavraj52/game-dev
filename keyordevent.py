import pygame
pygame.init()
w_width=500
w_height=500
screen=pygame.display.set_mode((w_width,w_height))
screen.fill("white")
pygame.display.set_caption("my first pygame")
#creating object
x=0
y=0
width=50
height=50
vel=1
clock=pygame.time.Clock()



done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_UP] and y>0:
        y-=vel
    if keys[pygame.K_DOWN]and y<w_height-height:
        y+=vel
    if keys[pygame.K_LEFT]and x>0:
        x-=vel
    if keys[pygame.K_RIGHT] and x<w_width-width:
        x+=vel
    screen.fill("white")
    clock.tick(60)

    pygame.draw.rect(screen,"black",(x,y,width,height))
    pygame.display.flip()