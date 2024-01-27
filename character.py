import pygame
pygame.init()
w_width=900
w_height=600
screen=pygame.display.set_mode((w_width,w_height))
screen.fill("white")
pygame.display.set_caption("sprites animation")
#jump variables
is_jump=False
jump_count=10
x=0
y=100
width=64
height=64
vel=5
clock=pygame.time.Clock()

bg_img= pygame.image.load("img/backrou.jpeg")
bg_img=pygame.transform.scale(bg_img,(w_width,w_height))
left=False
right=False
walkcount=0
walkright=[pygame.image.load(f'sprites/r{i}.png')for i in range(1,10)]
walkleft=[pygame.image.load(f'sprites/{i}.png')for i in range(1,10)]
char=pygame.image.load('sprites/0.png')


def drawingameloop():
    screen.blit(bg_img,(0,0))
    clock.tick(25)
    global walkcount
    
    if walkcount +1>=27:
        walkcount=0
    if left:
        screen.blit(walkleft[walkcount//3],(x,y))
        walkcount +=1
    
    elif right:
        screen.blit(walkright[walkcount//3],(x,y))
        walkcount +=1
    else:
        screen.blit(char,(x,y))
    
    pygame.display.flip()




done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and x>0:
        x-=vel
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x<w_width-width:
        x+=vel
        right=True
        left=False
    else:
        left=False
        right=False
        walkcount=0
        
    if not (is_jump):
        if keys[pygame.K_UP] and y>0:
            y-=vel
        if keys[pygame.K_DOWN]and y<w_height-height:
            y+=vel
   
        if keys[pygame.K_SPACE]:
            is_jump=True
    else:
        if is_jump:
            if jump_count>=10:
                neg=1
                if jump_count<0:
                    neg=-1
                y-=(jump_count**2)*neg*0.5
                jump_count-=1
            else:
                jump_count=10
                is_jump=False
            
        
        
    drawingameloop()