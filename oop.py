import pygame
pygame.init()
w_width=900
w_height=600
screen=pygame.display.set_mode((w_width,w_height))
screen.fill("white")
pygame.display.set_caption("sprites animation")

clock=pygame.time.Clock()

bg_img= pygame.image.load("img/backrou.jpeg")
bg_img=pygame.transform.scale(bg_img,(w_width,w_height))

walkright=[pygame.image.load(f'sprites/r{i}.png')for i in range(1,10)]
walkleft=[pygame.image.load(f'sprites/{i}.png')for i in range(1,10)]
char=pygame.image.load('sprites/0.png')


class player():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.is_jump=False
        self.jump_count=10
        self.left=False
        self.right=False
        self.walkcount=0
    def draw(self,screen):
            if self.walkcount +1>=27:
                self.walkcount=0
            if self.left:
                screen.blit(walkleft[self.walkcount//3],(self.x,self.y))
                self.walkcount +=1
            
            elif self.right:
                screen.blit(walkright[self.walkcount//3],(self.x,self.y))
                self.walkcount +=1
            else:
                screen.blit(char,(self.x,self.y))




def drawingameloop():
    screen.blit(bg_img,(0,0))
    clock.tick(25)
    soldier.draw(screen) 
    pygame.display.flip()



soldier=player(50,435,64,64)
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and soldier.x>0:
        soldier.x-=soldier.vel
        soldier.left=True
        soldier.right=False
    elif keys[pygame.K_RIGHT] and soldier.x<w_width-soldier.width:
        soldier.x+=soldier.vel
        soldier.right=True
        soldier.left=False
    else:
        soldier.left=False
        soldier.right=False
        soldier.walkcount=0
        
    if not (soldier.is_jump):
        if keys[pygame.K_UP] and soldier.y>0:
            soldier.y-=soldier.vel
        if keys[pygame.K_DOWN]and soldier.y<w_height-soldier.height:
            soldier.y+=soldier.vel
   
        if keys[pygame.K_SPACE]:
            soldier.is_jump=True
    else:
        if soldier.is_jump:
            if soldier.jump_count>=10:
                neg=1
                if soldier.jump_count<0:
                    neg=-1
                soldier.y-=(soldier.jump_count**2)*neg*0.5
                soldier.jump_count-=1
            else:
                soldier.jump_count=10
                soldier.is_jump=False
            
        
        
    drawingameloop()